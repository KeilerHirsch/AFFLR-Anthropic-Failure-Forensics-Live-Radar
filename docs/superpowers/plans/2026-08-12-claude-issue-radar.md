# Claude Issue Radar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an hourly GitHub Actions radar that searches the full public `anthropics/claude-code` issue corpus and maintains a review-only PR containing objective Top-25 views by reactions, comments, and recent activity.

**Architecture:** A dependency-free Python 3 script performs three unauthenticated GitHub Search API requests, validates and normalizes the returned issue metadata, compares each view with the last merged `main` baseline for `NEW`, and writes deterministic Markdown to a temporary output. A small GitHub Actions workflow runs it hourly, updates one persistent automation branch only when the rendered content changed, and creates at most one open PR. `GITHUB_TOKEN` is used only for git/PR operations inside `KeilerHirsch/anthropic-failure-forensics`.

**Tech Stack:** Python 3 standard library (`dataclasses`, `urllib`, `json`, `html`, `pathlib`, `argparse`, `unittest`), GitHub Search REST API, GitHub Actions, git, GitHub CLI (`gh`) for own-repository PR lookup/creation.

## Global Constraints

- Search scope is exactly `repo:anthropics/claude-code is:issue`; open and closed issues share the same corpus.
- Perform exactly three upstream searches per run: `sort:reactions-desc`, `sort:comments-desc`, and `sort:updated-desc`, each requesting exactly 25 rows.
- Upstream requests are public and unauthenticated; never send `GITHUB_TOKEN` to `api.github.com/search/issues`.
- `incomplete_results: true`, HTTP/rate-limit failure, invalid JSON, or missing required fields is a hard failure and must not replace the last known-good watchlist.
- No AFF/forensic score, no AI ranking, no LLM, no root-cause inference, and no automatic `AFF-###` creation or modification.
- `NEW` is view-specific and compares against the last merged `main` watchlist, not the current automation branch.
- Output must be byte-stable for identical API responses and identical baseline; no generated timestamp or corpus count may create churn.
- Scheduled cadence is exactly once per hour at a non-round minute; retain `workflow_dispatch`.
- Workflow permissions are limited to `contents: write` and `pull-requests: write`.
- Use no personal access token, GitHub App credential, analytics, telemetry, third-party action, or third-party Python package.
- README must describe the radar as discovery metadata only and link to `watchlist/candidates.md` while preserving `Evidence before attribution`.

---

## File Structure

- Create: `scripts/claude_issue_radar.py` — pure normalization/ranking/rendering functions plus the public Search API CLI.
- Create: `tests/test_claude_issue_radar.py` — stdlib `unittest` coverage for normalization, ranking, baseline parsing, Markdown safety, query construction, and fail-closed behavior.
- Create: `watchlist/candidates.md` — initial live-generated last-known-good radar snapshot.
- Create: `.github/workflows/claude-issue-radar.yml` — hourly/manual orchestration, change detection, persistent branch update, and single-PR management.
- Modify: `README.md` — concise radar section linking the watchlist and explaining its non-evidentiary role.

The Python file owns upstream data semantics and deterministic rendering. The workflow owns repository mutation and PR lifecycle. Neither layer may create or edit `cases/AFF-*`.

---

### Task 1: Normalize GitHub Search Results and Define Objective Views

**Files:**
- Create: `scripts/claude_issue_radar.py`
- Create: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces: `IssueRecord`, `VIEW_SPECS`, `normalize_issue(raw: dict) -> IssueRecord`, `normalize_search_response(payload: dict) -> list[IssueRecord]`, `sort_view(view_name: str, issues: list[IssueRecord]) -> list[IssueRecord]`.
- Consumes: raw GitHub Search API issue dictionaries.

- [ ] **Step 1: Write failing model and normalization tests**

Create `tests/test_claude_issue_radar.py` with:

```python
import unittest

from scripts import claude_issue_radar as radar


class RadarTests(unittest.TestCase):
    def sample_issue(self, **overrides):
        raw = {
            "number": 83510,
            "title": "[MODEL] quality regression | measured",
            "html_url": "https://github.com/anthropics/claude-code/issues/83510",
            "user": {"login": "KeilerHirsch"},
            "state": "open",
            "state_reason": None,
            "comments": 34,
            "created_at": "2026-08-04T10:00:00Z",
            "updated_at": "2026-08-12T10:00:00Z",
            "labels": [{"name": "model"}, {"name": "bug"}],
            "reactions": {
                "total_count": 12,
                "+1": 9,
                "-1": 0,
                "laugh": 0,
                "hooray": 0,
                "confused": 0,
                "heart": 1,
                "rocket": 2,
                "eyes": 0,
            },
        }
        raw.update(overrides)
        return raw

    def test_normalize_issue_preserves_observable_metadata(self):
        issue = radar.normalize_issue(self.sample_issue())
        self.assertEqual(issue.number, 83510)
        self.assertEqual(issue.author, "KeilerHirsch")
        self.assertEqual(issue.reactions_total, 12)
        self.assertEqual(issue.comments, 34)
        self.assertEqual(issue.labels, ("bug", "model"))
        self.assertEqual(issue.state, "open")
        self.assertIsNone(issue.state_reason)

    def test_normalize_closed_not_planned(self):
        issue = radar.normalize_issue(
            self.sample_issue(state="closed", state_reason="not_planned")
        )
        self.assertEqual(issue.state, "closed")
        self.assertEqual(issue.state_reason, "not_planned")

    def test_incomplete_search_response_is_rejected(self):
        with self.assertRaises(radar.RadarError):
            radar.normalize_search_response(
                {"incomplete_results": True, "items": [self.sample_issue()]}
            )

    def test_missing_required_field_is_rejected(self):
        raw = self.sample_issue()
        del raw["user"]
        with self.assertRaises(radar.RadarError):
            radar.normalize_search_response(
                {"incomplete_results": False, "items": [raw]}
            )
```

- [ ] **Step 2: Run the tests and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: import/module failures because `scripts/claude_issue_radar.py` does not exist.

- [ ] **Step 3: Implement the minimal data model and strict normalization**

Create `scripts/claude_issue_radar.py` beginning with:

```python
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


class RadarError(RuntimeError):
    pass


REACTION_KEYS = ("+1", "-1", "laugh", "hooray", "confused", "heart", "rocket", "eyes")


@dataclass(frozen=True)
class IssueRecord:
    number: int
    title: str
    url: str
    author: str
    state: str
    state_reason: str | None
    reactions_total: int
    reactions: tuple[tuple[str, int], ...]
    comments: int
    created_at: str
    updated_at: str
    labels: tuple[str, ...]


def _require(mapping: dict[str, Any], key: str) -> Any:
    if key not in mapping:
        raise RadarError(f"missing required field: {key}")
    return mapping[key]


def _require_iso8601(value: str, field: str) -> str:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise RadarError(f"invalid {field}: {value!r}") from exc
    return value


def normalize_issue(raw: dict[str, Any]) -> IssueRecord:
    user = _require(raw, "user")
    if not isinstance(user, dict) or not isinstance(user.get("login"), str):
        raise RadarError("invalid user.login")

    reactions = _require(raw, "reactions")
    if not isinstance(reactions, dict):
        raise RadarError("invalid reactions")

    labels_raw = _require(raw, "labels")
    if not isinstance(labels_raw, list):
        raise RadarError("invalid labels")
    labels = []
    for label in labels_raw:
        if not isinstance(label, dict) or not isinstance(label.get("name"), str):
            raise RadarError("invalid label name")
        labels.append(label["name"])

    reaction_pairs = []
    for key in REACTION_KEYS:
        value = reactions.get(key, 0)
        if not isinstance(value, int):
            raise RadarError(f"invalid reaction count: {key}")
        reaction_pairs.append((key, value))

    total = _require(reactions, "total_count")
    if not isinstance(total, int):
        raise RadarError("invalid reactions.total_count")

    state_reason = raw.get("state_reason")
    if state_reason is not None and not isinstance(state_reason, str):
        raise RadarError("invalid state_reason")

    return IssueRecord(
        number=int(_require(raw, "number")),
        title=str(_require(raw, "title")),
        url=str(_require(raw, "html_url")),
        author=user["login"],
        state=str(_require(raw, "state")),
        state_reason=state_reason,
        reactions_total=total,
        reactions=tuple(reaction_pairs),
        comments=int(_require(raw, "comments")),
        created_at=_require_iso8601(str(_require(raw, "created_at")), "created_at"),
        updated_at=_require_iso8601(str(_require(raw, "updated_at")), "updated_at"),
        labels=tuple(sorted(labels, key=str.casefold)),
    )


def normalize_search_response(payload: dict[str, Any]) -> list[IssueRecord]:
    if payload.get("incomplete_results") is not False:
        raise RadarError("GitHub search returned incomplete results")
    items = payload.get("items")
    if not isinstance(items, list):
        raise RadarError("GitHub search response has no items list")
    return [normalize_issue(item) for item in items]
```

- [ ] **Step 4: Run normalization tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: four tests pass.

- [ ] **Step 5: Add failing deterministic view-order tests**

Append to `RadarTests`:

```python
    def test_most_reacted_tie_breaks_by_comments_updated_number(self):
        raws = [
            self.sample_issue(number=1, comments=2, updated_at="2026-08-12T09:00:00Z"),
            self.sample_issue(number=2, comments=3, updated_at="2026-08-12T08:00:00Z"),
            self.sample_issue(number=3, comments=3, updated_at="2026-08-12T10:00:00Z"),
        ]
        issues = [radar.normalize_issue(x) for x in raws]
        self.assertEqual(
            [x.number for x in radar.sort_view("most-reacted", issues)],
            [3, 2, 1],
        )

    def test_most_discussed_tie_breaks_by_reactions_updated_number(self):
        a = self.sample_issue(number=1, comments=5)
        a["reactions"]["total_count"] = 4
        b = self.sample_issue(number=2, comments=5)
        b["reactions"]["total_count"] = 9
        issues = [radar.normalize_issue(a), radar.normalize_issue(b)]
        self.assertEqual(
            [x.number for x in radar.sort_view("most-discussed", issues)],
            [2, 1],
        )

    def test_recently_active_tie_breaks_by_reactions_comments_number(self):
        a = self.sample_issue(number=1, comments=20)
        a["reactions"]["total_count"] = 2
        b = self.sample_issue(number=2, comments=3)
        b["reactions"]["total_count"] = 8
        issues = [radar.normalize_issue(a), radar.normalize_issue(b)]
        self.assertEqual(
            [x.number for x in radar.sort_view("recently-active", issues)],
            [2, 1],
        )
```

- [ ] **Step 6: Run ordering tests and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: failures because `sort_view` is not defined.

- [ ] **Step 7: Implement deterministic local view ordering**

Add:

```python
VIEW_SPECS = {
    "most-reacted": "sort:reactions-desc",
    "most-discussed": "sort:comments-desc",
    "recently-active": "sort:updated-desc",
}


def _timestamp(value: str) -> float:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def sort_view(view_name: str, issues: list[IssueRecord]) -> list[IssueRecord]:
    if view_name == "most-reacted":
        key = lambda x: (x.reactions_total, x.comments, _timestamp(x.updated_at), x.number)
    elif view_name == "most-discussed":
        key = lambda x: (x.comments, x.reactions_total, _timestamp(x.updated_at), x.number)
    elif view_name == "recently-active":
        key = lambda x: (_timestamp(x.updated_at), x.reactions_total, x.comments, x.number)
    else:
        raise RadarError(f"unknown view: {view_name}")
    return sorted(issues, key=key, reverse=True)
```

- [ ] **Step 8: Run all Task 1 tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: all tests pass.

- [ ] **Step 9: Commit Task 1**

```bash
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: normalize Claude issue radar metadata"
```

---

### Task 2: Render Deterministic Markdown and Compute View-Specific NEW Markers

**Files:**
- Modify: `scripts/claude_issue_radar.py`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Consumes: `dict[str, list[IssueRecord]]` keyed by `most-reacted`, `most-discussed`, `recently-active`.
- Produces: `parse_baseline_views(markdown: str) -> dict[str, set[int]]`, `render_markdown(views, baseline_views) -> str`.

- [ ] **Step 1: Add failing baseline-marker tests**

Append:

```python
    def test_parse_baseline_views_reads_machine_markers(self):
        baseline = """# Claude Issue Radar
<!-- radar-view:most-reacted issues:10,20 -->
<!-- radar-view:most-discussed issues:20,30 -->
<!-- radar-view:recently-active issues:40 -->
"""
        self.assertEqual(
            radar.parse_baseline_views(baseline),
            {
                "most-reacted": {10, 20},
                "most-discussed": {20, 30},
                "recently-active": {40},
            },
        )

    def test_new_is_view_specific(self):
        issue = radar.normalize_issue(self.sample_issue(number=20))
        views = {
            "most-reacted": [issue],
            "most-discussed": [issue],
            "recently-active": [issue],
        }
        baseline = {
            "most-reacted": {20},
            "most-discussed": set(),
            "recently-active": {20},
        }
        rendered = radar.render_markdown(views, baseline)
        reacted = rendered.split("## Most reacted", 1)[1].split("## Most discussed", 1)[0]
        discussed = rendered.split("## Most discussed", 1)[1].split("## Recently active", 1)[0]
        self.assertNotIn("**NEW**", reacted)
        self.assertIn("**NEW**", discussed)
```

- [ ] **Step 2: Run tests and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: missing `parse_baseline_views` / `render_markdown` failures.

- [ ] **Step 3: Implement baseline markers, escaping, state labels, reactions, and renderer**

Add imports and functions:

```python
import html
import re

VIEW_TITLES = {
    "most-reacted": "Most reacted",
    "most-discussed": "Most discussed",
    "recently-active": "Recently active",
}

MARKER_RE = re.compile(r"<!-- radar-view:([a-z-]+) issues:([0-9,]*) -->")
REACTION_EMOJI = {
    "+1": "👍",
    "-1": "👎",
    "laugh": "😄",
    "hooray": "🎉",
    "confused": "😕",
    "heart": "❤️",
    "rocket": "🚀",
    "eyes": "👀",
}


def parse_baseline_views(markdown: str) -> dict[str, set[int]]:
    result = {name: set() for name in VIEW_SPECS}
    for view_name, csv_numbers in MARKER_RE.findall(markdown):
        if view_name not in result:
            continue
        result[view_name] = {
            int(part) for part in csv_numbers.split(",") if part.strip()
        }
    return result


def escape_cell(value: str) -> str:
    value = html.escape(value, quote=False)
    value = value.replace("\\", "\\\\").replace("|", "\\|")
    return " ".join(value.splitlines())


def state_label(issue: IssueRecord) -> str:
    state = issue.state.upper()
    if issue.state_reason:
        state += " / " + issue.state_reason.upper()
    return state


def reaction_label(issue: IssueRecord) -> str:
    nonzero = [
        f"{REACTION_EMOJI[key]} {count}"
        for key, count in issue.reactions
        if count
    ]
    detail = " · ".join(nonzero)
    return str(issue.reactions_total) if not detail else f"{issue.reactions_total} ({detail})"


def short_date(value: str) -> str:
    return value[:10]


def render_markdown(
    views: dict[str, list[IssueRecord]],
    baseline_views: dict[str, set[int]],
) -> str:
    lines = [
        "# Claude Issue Radar",
        "",
        "> Automated discovery metadata from public `anthropics/claude-code` issues. "
        "Inclusion here is **not** AFF acceptance, an evidence level, or causal attribution.",
        "",
        "The radar shows objective GitHub metadata only. `NEW` means an issue newly entered "
        "that specific Top-25 view relative to the last merged `main` snapshot.",
        "",
    ]

    for view_name in ("most-reacted", "most-discussed", "recently-active"):
        issues = views[view_name][:25]
        marker = ",".join(str(issue.number) for issue in issues)
        lines.extend([
            f"<!-- radar-view:{view_name} issues:{marker} -->",
            f"## {VIEW_TITLES[view_name]}",
            "",
            "| New | Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |",
            "|---|---:|---|---|---|---:|---:|---|---|---|",
        ])
        prior = baseline_views.get(view_name, set())
        for issue in issues:
            new = "**NEW**" if issue.number not in prior else ""
            labels = ", ".join(issue.labels) if issue.labels else "—"
            lines.append(
                "| {new} | [#{number}]({url}) | {title} | {author} | {state} | "
                "{reactions} | {comments} | {updated} | {created} | {labels} |".format(
                    new=new,
                    number=issue.number,
                    url=issue.url,
                    title=escape_cell(issue.title),
                    author=escape_cell(issue.author),
                    state=escape_cell(state_label(issue)),
                    reactions=escape_cell(reaction_label(issue)),
                    comments=issue.comments,
                    updated=short_date(issue.updated_at),
                    created=short_date(issue.created_at),
                    labels=escape_cell(labels),
                )
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"
```

- [ ] **Step 4: Add failing Markdown safety and determinism tests**

Append:

```python
    def test_markdown_table_escapes_pipe_and_html(self):
        issue = radar.normalize_issue(
            self.sample_issue(title="bad | title <script>")
        )
        views = {name: [issue] for name in radar.VIEW_SPECS}
        rendered = radar.render_markdown(
            views, {name: set() for name in radar.VIEW_SPECS}
        )
        self.assertIn("bad \\| title &lt;script&gt;", rendered)
        self.assertNotIn("<script>", rendered)

    def test_render_is_byte_stable_for_same_input(self):
        issue = radar.normalize_issue(self.sample_issue())
        views = {name: [issue] for name in radar.VIEW_SPECS}
        baseline = {name: {issue.number} for name in radar.VIEW_SPECS}
        self.assertEqual(
            radar.render_markdown(views, baseline),
            radar.render_markdown(views, baseline),
        )
```

- [ ] **Step 5: Run Task 2 tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit Task 2**

```bash
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: render deterministic Claude issue radar"
```

---

### Task 3: Implement the Three Public Search Requests and Fail-Closed CLI

**Files:**
- Modify: `scripts/claude_issue_radar.py`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces: `build_search_url(view_name: str) -> str`, `fetch_json(url: str, opener=urlopen) -> dict`, `collect_views(fetcher=fetch_json) -> dict[str, list[IssueRecord]]`, `main(argv=None) -> int`.
- CLI: `python scripts/claude_issue_radar.py --baseline PATH --output PATH`.

- [ ] **Step 1: Add failing exact-query tests**

Append:

```python
    def test_search_urls_scope_all_issues_and_request_exactly_25(self):
        reacted = radar.build_search_url("most-reacted")
        discussed = radar.build_search_url("most-discussed")
        recent = radar.build_search_url("recently-active")

        for url in (reacted, discussed, recent):
            self.assertIn("per_page=25", url)
            self.assertIn("repo%3Aanthropics%2Fclaude-code", url)
            self.assertIn("is%3Aissue", url)

        self.assertIn("sort%3Areactions-desc", reacted)
        self.assertIn("sort%3Acomments-desc", discussed)
        self.assertIn("sort%3Aupdated-desc", recent)
```

- [ ] **Step 2: Run query test and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar.RadarTests.test_search_urls_scope_all_issues_and_request_exactly_25 -v
```

Expected: missing `build_search_url`.

- [ ] **Step 3: Implement exact URL construction and HTTP/JSON validation without auth headers**

Add imports and code:

```python
import argparse
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SEARCH_ENDPOINT = "https://api.github.com/search/issues"
SEARCH_SCOPE = "repo:anthropics/claude-code is:issue"
API_VERSION = "2026-03-10"


def build_search_url(view_name: str) -> str:
    try:
        sort_clause = VIEW_SPECS[view_name]
    except KeyError as exc:
        raise RadarError(f"unknown view: {view_name}") from exc
    query = f"{SEARCH_SCOPE} {sort_clause}"
    return f"{SEARCH_ENDPOINT}?{urlencode({'q': query, 'per_page': 25})}"


def fetch_json(url: str, opener=urlopen) -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "KeilerHirsch-anthropic-failure-forensics-radar",
        },
    )
    # Deliberately no Authorization header: never leak the workflow token upstream.
    try:
        with opener(request, timeout=30) as response:
            body = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RadarError(f"GitHub search request failed: {url}") from exc
    try:
        payload = json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise RadarError("GitHub search returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise RadarError("GitHub search returned a non-object payload")
    return payload


def collect_views(fetcher=fetch_json) -> dict[str, list[IssueRecord]]:
    views = {}
    for view_name in ("most-reacted", "most-discussed", "recently-active"):
        payload = fetcher(build_search_url(view_name))
        issues = normalize_search_response(payload)
        if len(issues) > 25:
            raise RadarError(f"GitHub returned more than 25 rows for {view_name}")
        views[view_name] = sort_view(view_name, issues)
    return views
```

- [ ] **Step 4: Add failing tests proving three requests and fail-closed behavior**

Append:

```python
    def test_collect_views_makes_exactly_three_requests(self):
        calls = []

        def fake_fetch(url):
            calls.append(url)
            return {
                "incomplete_results": False,
                "items": [self.sample_issue(number=len(calls))],
            }

        views = radar.collect_views(fake_fetch)
        self.assertEqual(len(calls), 3)
        self.assertEqual(set(views), set(radar.VIEW_SPECS))

    def test_collection_stops_on_incomplete_result(self):
        def fake_fetch(_url):
            return {"incomplete_results": True, "items": []}

        with self.assertRaises(radar.RadarError):
            radar.collect_views(fake_fetch)
```

- [ ] **Step 5: Add CLI that writes only after every request and render succeeded**

Add:

```python

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    baseline_path = Path(args.baseline)
    output_path = Path(args.output)
    baseline_text = baseline_path.read_text(encoding="utf-8") if baseline_path.exists() else ""
    baseline_views = parse_baseline_views(baseline_text)

    # All network/validation/render work completes before the destination is touched.
    views = collect_views()
    rendered = render_markdown(views, baseline_views)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    temp_path.write_text(rendered, encoding="utf-8", newline="\n")
    temp_path.replace(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Add a CLI failure test that proves the existing output survives**

Add imports `tempfile`, `unittest.mock.patch`, `pathlib.Path` to the test file, then append:

```python
    def test_cli_failure_does_not_replace_existing_output(self):
        from pathlib import Path
        import tempfile
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline = root / "baseline.md"
            output = root / "output.md"
            baseline.write_text("old baseline\n", encoding="utf-8")
            output.write_text("last known good\n", encoding="utf-8")

            with patch.object(radar, "collect_views", side_effect=radar.RadarError("boom")):
                with self.assertRaises(radar.RadarError):
                    radar.main(["--baseline", str(baseline), "--output", str(output)])

            self.assertEqual(output.read_text(encoding="utf-8"), "last known good\n")
```

- [ ] **Step 7: Run all unit tests and verify GREEN**

Run:

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 8: Compile the script**

Run:

```bash
python -m py_compile scripts/claude_issue_radar.py
```

Expected: exit 0.

- [ ] **Step 9: Commit Task 3**

```bash
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: collect public Claude issue radar views"
```

---

### Task 4: Add Hourly GitHub Actions PR Automation

**Files:**
- Create: `.github/workflows/claude-issue-radar.yml`
- Test: existing `tests/test_claude_issue_radar.py` plus workflow text assertions.

**Interfaces:**
- Consumes: `scripts/claude_issue_radar.py`, current `main` `watchlist/candidates.md` baseline.
- Produces: persistent branch `automation/claude-issue-radar` and at most one open PR titled `chore: update Claude issue radar`.

- [ ] **Step 1: Add failing workflow contract test**

Append to the test file:

```python
    def test_workflow_contract_is_hourly_and_least_privilege(self):
        from pathlib import Path

        text = Path(".github/workflows/claude-issue-radar.yml").read_text(encoding="utf-8")
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("contents: write", text)
        self.assertIn("pull-requests: write", text)
        self.assertIn("automation/claude-issue-radar", text)
        self.assertNotIn("secrets.PAT", text)
        self.assertNotIn("Authorization: Bearer", text)
```

- [ ] **Step 2: Run the workflow contract test and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar.RadarTests.test_workflow_contract_is_hourly_and_least_privilege -v
```

Expected: file-not-found failure.

- [ ] **Step 3: Create the hourly workflow**

Create `.github/workflows/claude-issue-radar.yml`:

```yaml
name: Claude issue radar

on:
  schedule:
    - cron: '17 * * * *'
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

concurrency:
  group: claude-issue-radar
  cancel-in-progress: false

jobs:
  update-radar:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main
        uses: actions/checkout@v7
        with:
          ref: main
          fetch-depth: 0

      - name: Render radar from public GitHub search
        run: |
          python3 scripts/claude_issue_radar.py \
            --baseline watchlist/candidates.md \
            --output /tmp/candidates.md

      - name: Stop when radar content is unchanged
        id: diff
        shell: bash
        run: |
          if [ -f watchlist/candidates.md ] && cmp -s watchlist/candidates.md /tmp/candidates.md; then
            echo "changed=false" >> "$GITHUB_OUTPUT"
          else
            echo "changed=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Update persistent radar branch
        if: steps.diff.outputs.changed == 'true'
        env:
          BRANCH: automation/claude-issue-radar
        run: |
          set -euo pipefail
          git fetch origin "refs/heads/${BRANCH}:refs/remotes/origin/${BRANCH}" || true
          git checkout -B "$BRANCH" origin/main
          mkdir -p watchlist
          cp /tmp/candidates.md watchlist/candidates.md
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add watchlist/candidates.md
          git commit -m "chore: update Claude issue radar"
          git push --force-with-lease origin "HEAD:refs/heads/${BRANCH}"

      - name: Create radar PR when needed
        if: steps.diff.outputs.changed == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
          BRANCH: automation/claude-issue-radar
        run: |
          set -euo pipefail
          count="$(gh pr list \
            --repo "$GITHUB_REPOSITORY" \
            --state open \
            --base main \
            --head "$BRANCH" \
            --json number \
            --jq 'length')"
          if [ "$count" = "0" ]; then
            gh pr create \
              --repo "$GITHUB_REPOSITORY" \
              --base main \
              --head "$BRANCH" \
              --title "chore: update Claude issue radar" \
              --body "Automated hourly refresh of objective public GitHub issue metadata. Radar inclusion is discovery only and does not imply AFF acceptance, evidence level, or causal attribution."
          fi
```

The upstream Python HTTP client contains no `Authorization` header; `GH_TOKEN` exists only in the final own-repository PR step.

- [ ] **Step 4: Run the workflow contract and all unit tests**

Run:

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 5: Sanity-check the workflow text for forbidden mutation paths**

Run:

```bash
grep -n "AFF-\|cases/" .github/workflows/claude-issue-radar.yml && exit 1 || true
grep -n "PAT\|API_KEY\|TOKEN" .github/workflows/claude-issue-radar.yml
```

Expected: first command produces no matches; second may show only `GH_TOKEN: ${{ github.token }}`.

- [ ] **Step 6: Commit Task 4**

```bash
git add .github/workflows/claude-issue-radar.yml tests/test_claude_issue_radar.py
git commit -m "feat: automate hourly Claude issue radar PR"
```

---

### Task 5: Generate the Initial Radar Snapshot and Document It in README

**Files:**
- Create: `watchlist/candidates.md`
- Modify: `README.md`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces: first last-known-good watchlist baseline and public README entry point.

- [ ] **Step 1: Add failing README contract test**

Append:

```python
    def test_readme_describes_radar_without_claiming_evidence(self):
        from pathlib import Path

        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("## Claude issue radar", text)
        self.assertIn("watchlist/candidates.md", text)
        self.assertIn("discovery metadata", text)
        self.assertIn("Evidence before attribution", text)
```

- [ ] **Step 2: Run the README contract test and verify RED**

Run:

```bash
python -m unittest tests.test_claude_issue_radar.RadarTests.test_readme_describes_radar_without_claiming_evidence -v
```

Expected: failure because the radar section is not present.

- [ ] **Step 3: Run a live three-query generation into a temporary file**

Run:

```bash
python3 scripts/claude_issue_radar.py \
  --baseline /dev/null \
  --output /tmp/claude-radar.md
```

Expected: exit 0; exactly three public search calls; `/tmp/claude-radar.md` contains all three sections and 25 rows per section when GitHub returns 25 results.

- [ ] **Step 4: Inspect the live output before accepting it**

Run:

```bash
head -40 /tmp/claude-radar.md
grep -c '^| .*\[#[0-9]' /tmp/claude-radar.md
```

Expected: disclaimer visible; row count is 75 when every view returns 25 results.

- [ ] **Step 5: Install the verified live snapshot**

Run:

```bash
mkdir -p watchlist
cp /tmp/claude-radar.md watchlist/candidates.md
```

- [ ] **Step 6: Add a concise radar section to README**

Insert after the Case index / `cases/README.md` paragraph and before `## Evidence levels`:

```markdown
## Claude issue radar

[`watchlist/candidates.md`](watchlist/candidates.md) is an automated discovery view over public `anthropics/claude-code` issues. It refreshes hourly and shows three objective Top-25 views: **most reacted**, **most discussed**, and **recently active**, including both open and closed issues.

The radar is **discovery metadata, not evidence**. Reactions, comments, labels, and activity are useful signals for deciding what to inspect next, but inclusion does not assign an AFF evidence level or establish attribution. A finding enters the case archive only after manual review under **Evidence before attribution**.
```

- [ ] **Step 7: Run all tests**

Run:

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 8: Verify the generated snapshot has no accidental auth/secrets or generated timestamp churn**

Run:

```bash
grep -Ein 'token|authorization|secret|generated at|last generated' watchlist/candidates.md && exit 1 || true
```

Expected: no matches.

- [ ] **Step 9: Commit Task 5**

```bash
git add README.md watchlist/candidates.md tests/test_claude_issue_radar.py
git commit -m "docs: publish Claude issue radar"
```

---

### Task 6: End-to-End Verification and Review Gate

**Files:**
- Verify only; modify files only if verification exposes a defect.

**Interfaces:**
- Confirms every design invariant before a PR is opened/merged.

- [ ] **Step 1: Run the complete test suite fresh**

```bash
python -m unittest discover -s tests -v
```

Expected: zero failures/errors.

- [ ] **Step 2: Compile the implementation fresh**

```bash
python -m py_compile scripts/claude_issue_radar.py
```

Expected: exit 0.

- [ ] **Step 3: Prove deterministic rendering against the same live-derived fixtures/output**

Run twice using the same baseline and immediate live API state:

```bash
python3 scripts/claude_issue_radar.py --baseline watchlist/candidates.md --output /tmp/radar-a.md
cp /tmp/radar-a.md /tmp/radar-a-copy.md
python3 scripts/claude_issue_radar.py --baseline watchlist/candidates.md --output /tmp/radar-b.md
```

If upstream changed between the two calls, do not call that a determinism failure; instead capture one API response set as fixtures and render it twice in a unit test. For identical fixture input, byte comparison must pass:

```bash
cmp /tmp/radar-a-copy.md /tmp/radar-b.md
```

Expected when upstream is unchanged during the few seconds between calls: exit 0.

- [ ] **Step 4: Verify the workflow schedule and permissions mechanically**

```bash
grep -F "cron: '17 * * * *'" .github/workflows/claude-issue-radar.yml
grep -F "contents: write" .github/workflows/claude-issue-radar.yml
grep -F "pull-requests: write" .github/workflows/claude-issue-radar.yml
```

Expected: all three lines found.

- [ ] **Step 5: Verify the implementation cannot touch AFF cases**

```bash
grep -RInE 'cases/AFF-|AFF-[0-9]{3}' scripts .github/workflows tests || true
```

Expected: no mutation logic referencing `cases/AFF-*`; only a test assertion/string is acceptable if deliberately present.

- [ ] **Step 6: Verify upstream requests are unauthenticated in source**

```bash
grep -n "Authorization" scripts/claude_issue_radar.py && exit 1 || true
grep -n "GITHUB_TOKEN\|GH_TOKEN" scripts/claude_issue_radar.py && exit 1 || true
```

Expected: no matches.

- [ ] **Step 7: Review the branch diff**

```bash
git diff main...HEAD -- README.md scripts/claude_issue_radar.py tests/test_claude_issue_radar.py .github/workflows/claude-issue-radar.yml watchlist/candidates.md
```

Confirm only the radar feature, README section, tests, workflow, and generated watchlist changed.

- [ ] **Step 8: Check working tree cleanliness**

```bash
git status --short
```

Expected: empty.

- [ ] **Step 9: Request code review before merge**

Run the repository's normal adversarial review process on the final diff. Specifically challenge:

- token leakage across repository boundaries;
- fail-open behavior on GitHub Search API errors;
- `NEW` baseline semantics;
- force-with-lease behavior on the persistent automation branch;
- duplicate PR creation races;
- Markdown injection/table corruption;
- workflow permission scope.

Do not merge until review findings are resolved and Tasks 1–6 remain green.
