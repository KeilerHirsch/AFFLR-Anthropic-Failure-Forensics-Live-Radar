# Claude Issue Radar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an hourly review-gated radar that searches the full public `anthropics/claude-code` issue corpus and proposes objective Top-25 views by reactions, comments, and recent activity.

**Architecture:** A dependency-free Python 3 script makes exactly three unauthenticated GitHub Search API requests, validates/normalizes the returned metadata, and renders deterministic Markdown. A GitHub Actions workflow checks hourly, compares the render with `main`, and only when content changed updates one persistent automation branch and one open PR. The normal PR diff communicates additions/removals; no stored `NEW` marker or inferred score exists.

**Tech Stack:** Python 3 standard library, `unittest`, GitHub Search REST API, GitHub Actions, git, GitHub CLI (`gh`) for PR lifecycle inside the workflow repository.

## Global Constraints

- Search scope: exactly `repo:anthropics/claude-code is:issue`.
- Three upstream queries only: `sort:reactions-desc`, `sort:comments-desc`, `sort:updated-desc`; each requests `per_page=25`.
- Upstream search is public and unauthenticated. Never send `GITHUB_TOKEN` to `api.github.com/search/issues`.
- `incomplete_results: true`, HTTP/rate-limit error, invalid JSON, or missing required metadata is a hard failure.
- No AFF/forensic score, no HOT/STRONG/WATCH classification, no LLM, no automatic case creation or mutation.
- Output is byte-stable for identical search responses; no generated timestamp or corpus counter.
- Schedule: once per hour at a non-round minute plus `workflow_dispatch`.
- Workflow permissions: `contents: write`, `pull-requests: write`, nothing broader.
- At most one open radar PR. Unchanged output means no commit and no PR update.
- No PAT, GitHub App secret, third-party Python package, third-party Action, telemetry, or analytics.
- README must say the radar is discovery metadata, not evidence, and that changes remain behind a PR review gate.

---

## File Structure

- Create `scripts/claude_issue_radar.py`: search URL construction, HTTP client, strict normalization, objective ordering, Markdown renderer, atomic CLI output.
- Create `tests/test_claude_issue_radar.py`: stdlib unit/contract tests.
- Create `.github/workflows/claude-issue-radar.yml`: hourly/manual orchestration and single-PR branch lifecycle.
- Create `watchlist/candidates.md`: initial live snapshot.
- Modify `README.md`: small radar section only.

---

### Task 1: Issue Model, Validation, and Objective Ordering

**Files:**
- Create: `scripts/claude_issue_radar.py`
- Create: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces `RadarError`, `IssueRecord`, `normalize_issue()`, `normalize_search_response()`, `sort_view()`.

- [ ] **Step 1: Write failing normalization tests**

Create `tests/test_claude_issue_radar.py`:

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

    def test_normalize_issue_preserves_metadata(self):
        issue = radar.normalize_issue(self.sample_issue())
        self.assertEqual(issue.number, 83510)
        self.assertEqual(issue.author, "KeilerHirsch")
        self.assertEqual(issue.reactions_total, 12)
        self.assertEqual(issue.comments, 34)
        self.assertEqual(issue.labels, ("bug", "model"))

    def test_closed_state_reason_is_preserved(self):
        issue = radar.normalize_issue(
            self.sample_issue(state="closed", state_reason="not_planned")
        )
        self.assertEqual(issue.state_reason, "not_planned")

    def test_incomplete_results_fail_closed(self):
        with self.assertRaises(radar.RadarError):
            radar.normalize_search_response(
                {"incomplete_results": True, "items": [self.sample_issue()]}
            )

    def test_missing_required_field_fails_closed(self):
        raw = self.sample_issue()
        del raw["user"]
        with self.assertRaises(radar.RadarError):
            radar.normalize_search_response(
                {"incomplete_results": False, "items": [raw]}
            )
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: import/module failure because implementation does not exist.

- [ ] **Step 3: Implement strict normalized records**

Create `scripts/claude_issue_radar.py`:

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


def _need(mapping: dict[str, Any], key: str) -> Any:
    if key not in mapping:
        raise RadarError(f"missing required field: {key}")
    return mapping[key]


def _iso(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise RadarError(f"invalid {field}")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise RadarError(f"invalid {field}: {value!r}") from exc
    return value


def normalize_issue(raw: dict[str, Any]) -> IssueRecord:
    user = _need(raw, "user")
    if not isinstance(user, dict) or not isinstance(user.get("login"), str):
        raise RadarError("invalid user.login")

    reactions = _need(raw, "reactions")
    if not isinstance(reactions, dict) or not isinstance(reactions.get("total_count"), int):
        raise RadarError("invalid reactions")

    labels_raw = _need(raw, "labels")
    if not isinstance(labels_raw, list):
        raise RadarError("invalid labels")
    labels = []
    for label in labels_raw:
        if not isinstance(label, dict) or not isinstance(label.get("name"), str):
            raise RadarError("invalid label")
        labels.append(label["name"])

    reaction_pairs = []
    for key in REACTION_KEYS:
        value = reactions.get(key, 0)
        if not isinstance(value, int):
            raise RadarError(f"invalid reaction count: {key}")
        reaction_pairs.append((key, value))

    state_reason = raw.get("state_reason")
    if state_reason is not None and not isinstance(state_reason, str):
        raise RadarError("invalid state_reason")

    number = _need(raw, "number")
    comments = _need(raw, "comments")
    if not isinstance(number, int) or not isinstance(comments, int):
        raise RadarError("invalid numeric issue metadata")

    return IssueRecord(
        number=number,
        title=str(_need(raw, "title")),
        url=str(_need(raw, "html_url")),
        author=user["login"],
        state=str(_need(raw, "state")),
        state_reason=state_reason,
        reactions_total=reactions["total_count"],
        reactions=tuple(reaction_pairs),
        comments=comments,
        created_at=_iso(_need(raw, "created_at"), "created_at"),
        updated_at=_iso(_need(raw, "updated_at"), "updated_at"),
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

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_claude_issue_radar -v
```

Expected: four tests pass.

- [ ] **Step 5: Add failing deterministic tie-break tests**

Append:

```python
    def test_objective_tie_breakers_are_deterministic(self):
        a = radar.normalize_issue(self.sample_issue(number=1, comments=4))
        b_raw = self.sample_issue(number=2, comments=5)
        b = radar.normalize_issue(b_raw)
        self.assertEqual(
            [x.number for x in radar.sort_view("most-reacted", [a, b])],
            [2, 1],
        )
```

- [ ] **Step 6: Implement view specs and deterministic sort**

Add:

```python
VIEW_SPECS = {
    "most-reacted": "sort:reactions-desc",
    "most-discussed": "sort:comments-desc",
    "recently-active": "sort:updated-desc",
}


def _ts(value: str) -> float:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def sort_view(view_name: str, issues: list[IssueRecord]) -> list[IssueRecord]:
    if view_name == "most-reacted":
        key = lambda x: (x.reactions_total, x.comments, _ts(x.updated_at), x.number)
    elif view_name == "most-discussed":
        key = lambda x: (x.comments, x.reactions_total, _ts(x.updated_at), x.number)
    elif view_name == "recently-active":
        key = lambda x: (_ts(x.updated_at), x.reactions_total, x.comments, x.number)
    else:
        raise RadarError(f"unknown view: {view_name}")
    return sorted(issues, key=key, reverse=True)
```

- [ ] **Step 7: Run GREEN and commit**

```bash
python -m unittest tests.test_claude_issue_radar -v
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: normalize Claude issue radar metadata"
```

---

### Task 2: Exact Public Search Queries and Fail-Closed HTTP Client

**Files:**
- Modify: `scripts/claude_issue_radar.py`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces `build_search_url()`, `fetch_json()`, `collect_views()`.

- [ ] **Step 1: Add failing exact-query test**

```python
    def test_search_urls_use_full_issue_scope_and_top_25(self):
        urls = {name: radar.build_search_url(name) for name in radar.VIEW_SPECS}
        for url in urls.values():
            self.assertIn("repo%3Aanthropics%2Fclaude-code", url)
            self.assertIn("is%3Aissue", url)
            self.assertIn("per_page=25", url)
        self.assertIn("sort%3Areactions-desc", urls["most-reacted"])
        self.assertIn("sort%3Acomments-desc", urls["most-discussed"])
        self.assertIn("sort%3Aupdated-desc", urls["recently-active"])
```

Run and confirm RED.

- [ ] **Step 2: Implement URL construction and unauthenticated fetch**

Add:

```python
import json
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
    return SEARCH_ENDPOINT + "?" + urlencode(
        {"q": f"{SEARCH_SCOPE} {sort_clause}", "per_page": 25}
    )


def fetch_json(url: str, opener=urlopen) -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "KeilerHirsch-anthropic-failure-forensics-radar",
        },
    )
    # Intentionally no Authorization header.
    try:
        with opener(request, timeout=30) as response:
            raw = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RadarError("GitHub search request failed") from exc
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise RadarError("GitHub search returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise RadarError("GitHub search returned non-object JSON")
    return payload


def collect_views(fetcher=fetch_json) -> dict[str, list[IssueRecord]]:
    result = {}
    for name in ("most-reacted", "most-discussed", "recently-active"):
        issues = normalize_search_response(fetcher(build_search_url(name)))
        if len(issues) > 25:
            raise RadarError(f"too many rows returned for {name}")
        result[name] = sort_view(name, issues)
    return result
```

- [ ] **Step 3: Add request-count and incomplete-result tests**

```python
    def test_collect_views_makes_exactly_three_requests(self):
        calls = []
        def fake_fetch(url):
            calls.append(url)
            return {"incomplete_results": False, "items": [self.sample_issue(number=len(calls))]}
        views = radar.collect_views(fake_fetch)
        self.assertEqual(len(calls), 3)
        self.assertEqual(set(views), set(radar.VIEW_SPECS))

    def test_collection_aborts_on_incomplete_response(self):
        def fake_fetch(_url):
            return {"incomplete_results": True, "items": []}
        with self.assertRaises(radar.RadarError):
            radar.collect_views(fake_fetch)
```

- [ ] **Step 4: Run GREEN and prove no auth header exists**

```bash
python -m unittest discover -s tests -v
grep -n "Authorization" scripts/claude_issue_radar.py && exit 1 || true
```

Expected: tests pass; grep returns no source match.

- [ ] **Step 5: Commit**

```bash
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: query public Claude issue search views"
```

---

### Task 3: Deterministic Markdown Renderer and Atomic CLI

**Files:**
- Modify: `scripts/claude_issue_radar.py`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Produces `render_markdown()`, `main()`.
- CLI: `python3 scripts/claude_issue_radar.py --output PATH`.

- [ ] **Step 1: Add failing render tests**

```python
    def test_render_contains_required_metadata_and_escapes_table_text(self):
        issue = radar.normalize_issue(self.sample_issue(title="bad | title <script>"))
        views = {name: [issue] for name in radar.VIEW_SPECS}
        text = radar.render_markdown(views)
        self.assertIn("[#83510]", text)
        self.assertIn("KeilerHirsch", text)
        self.assertIn("12 (", text)
        self.assertIn("34", text)
        self.assertIn("bad \\| title &lt;script&gt;", text)
        self.assertNotIn("<script>", text)

    def test_render_has_no_scores_or_new_marker(self):
        issue = radar.normalize_issue(self.sample_issue())
        text = radar.render_markdown({name: [issue] for name in radar.VIEW_SPECS})
        self.assertNotIn("Forensic score", text)
        self.assertNotIn("**NEW**", text)

    def test_render_is_byte_stable(self):
        issue = radar.normalize_issue(self.sample_issue())
        views = {name: [issue] for name in radar.VIEW_SPECS}
        self.assertEqual(radar.render_markdown(views), radar.render_markdown(views))
```

Run RED.

- [ ] **Step 2: Implement renderer**

Add:

```python
import html

VIEW_TITLES = {
    "most-reacted": "Most reacted",
    "most-discussed": "Most discussed",
    "recently-active": "Recently active",
}

REACTION_EMOJI = {
    "+1": "👍", "-1": "👎", "laugh": "😄", "hooray": "🎉",
    "confused": "😕", "heart": "❤️", "rocket": "🚀", "eyes": "👀",
}


def escape_cell(value: str) -> str:
    value = html.escape(value, quote=False)
    value = value.replace("\\", "\\\\").replace("|", "\\|")
    return " ".join(value.splitlines())


def state_label(issue: IssueRecord) -> str:
    label = issue.state.upper()
    if issue.state_reason:
        label += " / " + issue.state_reason.upper()
    return label


def reaction_label(issue: IssueRecord) -> str:
    detail = " · ".join(
        f"{REACTION_EMOJI[key]} {count}"
        for key, count in issue.reactions
        if count
    )
    return str(issue.reactions_total) if not detail else f"{issue.reactions_total} ({detail})"


def render_markdown(views: dict[str, list[IssueRecord]]) -> str:
    lines = [
        "# Claude Issue Radar",
        "",
        "> Automated discovery metadata from public `anthropics/claude-code` issues. "
        "Inclusion here is **not** AFF acceptance, an evidence level, or causal attribution.",
        "",
    ]
    for name in ("most-reacted", "most-discussed", "recently-active"):
        lines.extend([
            f"## {VIEW_TITLES[name]}",
            "",
            "| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |",
            "|---:|---|---|---|---:|---:|---|---|---|",
        ])
        for issue in views[name][:25]:
            labels = ", ".join(issue.labels) if issue.labels else "—"
            lines.append(
                "| [#{n}]({url}) | {title} | {author} | {state} | {reactions} | "
                "{comments} | {updated} | {created} | {labels} |".format(
                    n=issue.number,
                    url=issue.url,
                    title=escape_cell(issue.title),
                    author=escape_cell(issue.author),
                    state=escape_cell(state_label(issue)),
                    reactions=escape_cell(reaction_label(issue)),
                    comments=issue.comments,
                    updated=issue.updated_at[:10],
                    created=issue.created_at[:10],
                    labels=escape_cell(labels),
                )
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
```

- [ ] **Step 3: Add atomic CLI and failure-preservation test**

Add implementation:

```python
import argparse
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    views = collect_views()
    rendered = render_markdown(views)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".tmp")
    temp.write_text(rendered, encoding="utf-8", newline="\n")
    temp.replace(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Add test:

```python
    def test_cli_failure_does_not_replace_existing_output(self):
        from pathlib import Path
        import tempfile
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "radar.md"
            output.write_text("last known good\n", encoding="utf-8")
            with patch.object(radar, "collect_views", side_effect=radar.RadarError("boom")):
                with self.assertRaises(radar.RadarError):
                    radar.main(["--output", str(output)])
            self.assertEqual(output.read_text(encoding="utf-8"), "last known good\n")
```

- [ ] **Step 4: Run GREEN, compile, commit**

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/claude_issue_radar.py
git add scripts/claude_issue_radar.py tests/test_claude_issue_radar.py
git commit -m "feat: render deterministic Claude issue radar"
```

---

### Task 4: Hourly Single-PR GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/claude-issue-radar.yml`
- Modify: `tests/test_claude_issue_radar.py`

**Interfaces:**
- Persistent branch: `automation/claude-issue-radar`.
- Stable PR title: `chore: update Claude issue radar`.

- [ ] **Step 1: Add failing workflow contract test**

```python
    def test_workflow_contract(self):
        from pathlib import Path
        text = Path(".github/workflows/claude-issue-radar.yml").read_text(encoding="utf-8")
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("contents: write", text)
        self.assertIn("pull-requests: write", text)
        self.assertIn("automation/claude-issue-radar", text)
        self.assertNotIn("secrets.PAT", text)
```

Run RED.

- [ ] **Step 2: Create workflow**

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

      - name: Render public issue radar
        run: python3 scripts/claude_issue_radar.py --output /tmp/candidates.md

      - name: Detect content change
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

      - name: Create radar PR if none is open
        if: steps.diff.outputs.changed == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
          BRANCH: automation/claude-issue-radar
        run: |
          set -euo pipefail
          count="$(gh pr list --repo "$GITHUB_REPOSITORY" --state open --base main --head "$BRANCH" --json number --jq 'length')"
          if [ "$count" = "0" ]; then
            gh pr create \
              --repo "$GITHUB_REPOSITORY" \
              --base main \
              --head "$BRANCH" \
              --title "chore: update Claude issue radar" \
              --body "Automated hourly check of objective public GitHub issue metadata. Radar inclusion is discovery only and does not imply AFF acceptance, evidence level, or causal attribution."
          fi
```

- [ ] **Step 3: Run contract tests and static safety checks**

```bash
python -m unittest discover -s tests -v
grep -n "AFF-\|cases/" .github/workflows/claude-issue-radar.yml && exit 1 || true
grep -n "PAT\|API_KEY" .github/workflows/claude-issue-radar.yml && exit 1 || true
```

Expected: tests pass; no forbidden paths/secrets.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/claude-issue-radar.yml tests/test_claude_issue_radar.py
git commit -m "feat: automate hourly Claude issue radar PR"
```

---

### Task 5: Live Snapshot and README Integration

**Files:**
- Create: `watchlist/candidates.md`
- Modify: `README.md`
- Modify: `tests/test_claude_issue_radar.py`

- [ ] **Step 1: Run live generation to temporary output**

```bash
python3 scripts/claude_issue_radar.py --output /tmp/claude-radar.md
```

Expected: exit 0 after exactly three public search requests.

- [ ] **Step 2: Inspect live output mechanically**

```bash
head -30 /tmp/claude-radar.md
grep -c '^| \[#[0-9]' /tmp/claude-radar.md
```

Expected: disclaimer plus three sections; normally 75 issue rows when each query returns 25 rows.

- [ ] **Step 3: Install initial snapshot**

```bash
mkdir -p watchlist
cp /tmp/claude-radar.md watchlist/candidates.md
```

- [ ] **Step 4: Add README contract test**

```python
    def test_readme_explains_radar_review_gate(self):
        from pathlib import Path
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("## Claude issue radar", text)
        self.assertIn("watchlist/candidates.md", text)
        self.assertIn("discovery metadata", text)
        self.assertIn("review", text.lower())
        self.assertIn("Evidence before attribution", text)
```

Run RED before editing README.

- [ ] **Step 5: Add README section after the Case index and before Evidence levels**

Insert:

```markdown
## Claude issue radar

[`watchlist/candidates.md`](watchlist/candidates.md) is an automated discovery view over public `anthropics/claude-code` issues. The radar checks the full issue corpus hourly and exposes three objective Top-25 views: **most reacted**, **most discussed**, and **recently active**, including both open and closed issues. Changes are proposed through a review pull request rather than written directly to the case archive.

The radar is **discovery metadata, not evidence**. Reactions, comments, labels, and activity are useful signals for deciding what to inspect next, but inclusion does not assign an AFF evidence level or establish attribution. A finding enters the case archive only after manual review under **Evidence before attribution**.
```

- [ ] **Step 6: Run full tests and commit**

```bash
python -m unittest discover -s tests -v
git add README.md watchlist/candidates.md tests/test_claude_issue_radar.py
git commit -m "docs: publish Claude issue radar"
```

---

### Task 6: Final Verification and Review Gate

**Files:** verify only unless a defect is found.

- [ ] **Step 1: Fresh full test suite**

```bash
python -m unittest discover -s tests -v
```

Expected: zero failures/errors.

- [ ] **Step 2: Fresh compile**

```bash
python -m py_compile scripts/claude_issue_radar.py
```

Expected: exit 0.

- [ ] **Step 3: Prove no token can reach upstream search code**

```bash
grep -n "Authorization\|GITHUB_TOKEN\|GH_TOKEN" scripts/claude_issue_radar.py && exit 1 || true
```

Expected: no matches.

- [ ] **Step 4: Prove workflow cadence and permissions**

```bash
grep -F "cron: '17 * * * *'" .github/workflows/claude-issue-radar.yml
grep -F "contents: write" .github/workflows/claude-issue-radar.yml
grep -F "pull-requests: write" .github/workflows/claude-issue-radar.yml
```

Expected: all present.

- [ ] **Step 5: Prove no AFF mutation path exists**

```bash
grep -RInE 'cases/AFF-|AFF-[0-9]{3}' scripts .github/workflows || true
```

Expected: no matches.

- [ ] **Step 6: Verify generated file contains no score or churn marker**

```bash
grep -Ein 'forensic score|aff score|\*\*NEW\*\*|generated at|last generated' watchlist/candidates.md && exit 1 || true
```

Expected: no matches.

- [ ] **Step 7: Inspect complete branch diff**

```bash
git diff main...HEAD -- README.md scripts/claude_issue_radar.py tests/test_claude_issue_radar.py .github/workflows/claude-issue-radar.yml watchlist/candidates.md
```

Expected: radar-only changes.

- [ ] **Step 8: Working tree clean**

```bash
git status --short
```

Expected: empty.

- [ ] **Step 9: Adversarial review before merge**

Challenge at minimum:

- unauthenticated Search API rate-limit/failure handling;
- Markdown injection/table corruption;
- persistent-branch `--force-with-lease` behavior;
- duplicate PR races despite concurrency;
- workflow token scope;
- any hidden path that could mutate `cases/AFF-*`;
- whether identical metadata really produces identical output.

Resolve findings, rerun Steps 1–8, then open the implementation PR for human review.
