# AFFLR Direct-Live README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make AFFLR genuinely live by rendering Top-5 radar rows directly in the README, placing rows 6–25 under native `<details>` blocks, and letting the hourly/manual GitHub Actions workflow update only generated radar metadata directly on `main`.

**Architecture:** `scripts/afflr.py` remains the single source of truth for normalization and ordering. It gains reusable row/table rendering plus a marker-safe README fragment/injection path; the workflow renders both README and `watchlist/candidates.md` from the same live views, validates the generated region, commits only generated radar metadata when bytes changed, and pushes normally to `main` without PR creation or force pushing.

**Tech Stack:** Python 3 standard library, `unittest`, GitHub Markdown/HTML `<details>`, GitHub Actions, git.

## Global Constraints

- The README must contain exactly one `<!-- AFFLR-RADAR:START -->` and one `<!-- AFFLR-RADAR:END -->` marker in the correct order.
- Each of the three views displays exactly the first 5 rows directly.
- Rows 6–25 are available under a native `<details>` block for the same view.
- `watchlist/candidates.md` remains the complete Top-25 × 3 snapshot.
- README and watchlist are rendered from the same normalized issue views.
- Identical input must produce byte-identical output.
- Existing escaping of untrusted issue/title/author/label text must remain intact.
- Workflow schedule remains `17 * * * *` plus `workflow_dispatch`.
- Workflow permissions are reduced to `contents: write`; `pull-requests: write` is removed.
- No `automation/afflr` branch, `gh pr`, PR closing, force-with-lease, or force push remains in the live path.
- Changed generated radar content commits only `README.md` and/or `watchlist/candidates.md` directly to `main`.
- Unchanged generated radar content creates no commit.
- Missing/duplicate/inverted README markers are a hard failure before tracked files are modified.
- Search/API/JSON/normalization/rendering failure preserves the last known-good README and watchlist.
- A normal push conflict is a hard failure; the workflow must never force-push `main`.
- Automation must never modify `cases/`, methodology/evidence levels, forensic conclusions, attribution, root-cause statements, or issue acceptance/promotion decisions.
- `Evidence before attribution.` remains visible on the front page.

---

## File Structure

- Modify `scripts/afflr.py`: reusable table-row rendering, compact README radar fragment rendering, marker validation/injection, and CLI support for rendering both outputs before touching tracked files.
- Modify `tests/test_afflr.py`: TDD for Top-5/details behavior, marker safety, byte stability, README outside-region preservation, dual-output failure behavior, and Direct-Live workflow contract.
- Modify `.github/workflows/afflr.yml`: replace automation-branch/PR lifecycle with direct safe commit/push to `main`.
- Modify `README.md`: add the two generated markers and initial radar region.
- Modify `watchlist/candidates.md`: seed `main` with the current complete snapshot.

---

### Task 1: Reusable radar table rendering and compact README fragment

**Files:**
- Modify: `scripts/afflr.py`
- Modify: `tests/test_afflr.py`

**Interfaces:**
- Consumes: existing `IssueRecord`, `VIEW_ORDER`, `VIEW_TITLES`, `escape_cell()`, `state_label()`, `reaction_label()`.
- Produces: `render_table_rows(issues: list[IssueRecord]) -> list[str]`, `render_readme_fragment(views: dict[str, list[IssueRecord]]) -> str`.

- [ ] **Step 1: Add failing tests for Top-5 visible rows and collapsed remainder**

Append to `RenderingTests`:

```python
    def test_readme_fragment_shows_top_five_and_collapses_rest(self):
        issues = [
            afflr.normalize_issue(
                self.sample_issue(
                    number=n,
                    comments=100 - n,
                    updated_at=f"2026-08-{(n % 9) + 1:02d}T10:00:00Z",
                )
            )
            for n in range(1, 26)
        ]
        views = {name: issues for name in afflr.VIEW_ORDER}

        text = afflr.render_readme_fragment(views)

        self.assertEqual(text.count("<details>"), 3)
        self.assertEqual(text.count("<summary>Show remaining 20</summary>"), 3)
        for number in range(1, 6):
            self.assertIn(f"[#{number}]", text)
        self.assertIn("[#{6}]".format(6), text)
        self.assertIn("[#{25}]".format(25), text)
```

Also add a structural assertion that each view contains one visible table before its `<details>` and one remainder table inside it.

- [ ] **Step 2: Run RED**

Run:

```bash
python -m unittest tests.test_afflr.RenderingTests -v
```

Expected: failure because `render_readme_fragment` does not exist.

- [ ] **Step 3: Extract one canonical row renderer**

In `scripts/afflr.py`, add:

```python
TABLE_HEADER = "| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |"
TABLE_RULE = "|---:|---|---|---|---:|---:|---|---|---|"


def render_table_rows(issues: list[IssueRecord]) -> list[str]:
    rows: list[str] = []
    for issue in issues:
        labels = ", ".join(issue.labels) if issue.labels else "—"
        rows.append(
            "| [#{number}]({url}) | {title} | {author} | {state} | {reactions} | "
            "{comments} | {updated} | {created} | {labels} |".format(
                number=issue.number,
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
    return rows
```

Refactor `render_markdown()` to use `TABLE_HEADER`, `TABLE_RULE`, and `render_table_rows()` without changing its existing output contract.

- [ ] **Step 4: Implement `render_readme_fragment()`**

Add:

```python
README_VIEW_TITLES = {
    "most-reacted": "🔥 Most reacted",
    "most-discussed": "💬 Most discussed",
    "recently-active": "🆕 Recently active",
}


def render_readme_fragment(views: dict[str, list[IssueRecord]]) -> str:
    if set(views) != set(VIEW_ORDER):
        raise RadarError("missing or unexpected radar view")

    lines = [
        "> Automated discovery metadata from public `anthropics/claude-code` issues. "
        "Popularity is a discovery signal, not evidence.",
        "",
    ]

    for name in VIEW_ORDER:
        issues = views[name][:25]
        visible = issues[:5]
        hidden = issues[5:25]
        lines.extend([
            f"### {README_VIEW_TITLES[name]}",
            "",
            TABLE_HEADER,
            TABLE_RULE,
            *render_table_rows(visible),
            "",
        ])
        if hidden:
            lines.extend([
                "<details>",
                f"<summary>Show remaining {len(hidden)}</summary>",
                "",
                TABLE_HEADER,
                TABLE_RULE,
                *render_table_rows(hidden),
                "",
                "</details>",
                "",
            ])

    return "\n".join(lines).rstrip() + "\n"
```

- [ ] **Step 5: Run GREEN and regression checks**

Run:

```bash
python -m unittest tests.test_afflr.RenderingTests -v
python -m unittest tests.test_afflr -v
```

Expected: all existing rendering tests remain green and new fragment tests pass.

- [ ] **Step 6: Commit Task 1**

```bash
git add scripts/afflr.py tests/test_afflr.py
git commit -m "feat: render compact AFFLR README radar"
```

---

### Task 2: Marker-safe README injection and dual-output CLI

**Files:**
- Modify: `scripts/afflr.py`
- Modify: `tests/test_afflr.py`
- Modify: `README.md`

**Interfaces:**
- Produces: `README_START`, `README_END`, `inject_readme_fragment(readme: str, fragment: str) -> str`.
- Extends CLI with `--readme` and keeps `--output` for the full snapshot.

- [ ] **Step 1: Add failing marker-safety tests**

Append tests:

```python
    def test_inject_readme_fragment_preserves_outside_content(self):
        original = "before\n<!-- AFFLR-RADAR:START -->\nold\n<!-- AFFLR-RADAR:END -->\nafter\n"
        updated = afflr.inject_readme_fragment(original, "new\n")
        self.assertEqual(
            updated,
            "before\n<!-- AFFLR-RADAR:START -->\nnew\n<!-- AFFLR-RADAR:END -->\nafter\n",
        )

    def test_inject_readme_fragment_rejects_missing_duplicate_or_inverted_markers(self):
        invalid = [
            "no markers\n",
            "<!-- AFFLR-RADAR:START -->\nonly start\n",
            "<!-- AFFLR-RADAR:END -->\n<!-- AFFLR-RADAR:START -->\n",
            "<!-- AFFLR-RADAR:START -->\na\n<!-- AFFLR-RADAR:START -->\nb\n<!-- AFFLR-RADAR:END -->\n",
        ]
        for text in invalid:
            with self.subTest(text=text):
                with self.assertRaises(afflr.RadarError):
                    afflr.inject_readme_fragment(text, "new\n")
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_afflr.RenderingTests -v
```

Expected: failure because marker helpers do not exist.

- [ ] **Step 3: Implement exact marker validation and injection**

Add to `scripts/afflr.py`:

```python
README_START = "<!-- AFFLR-RADAR:START -->"
README_END = "<!-- AFFLR-RADAR:END -->"


def inject_readme_fragment(readme: str, fragment: str) -> str:
    if readme.count(README_START) != 1 or readme.count(README_END) != 1:
        raise RadarError("README must contain exactly one AFFLR radar marker pair")

    start = readme.index(README_START)
    end = readme.index(README_END)
    if start >= end:
        raise RadarError("AFFLR README markers are inverted")

    before = readme[: start + len(README_START)]
    after = readme[end:]
    return before + "\n" + fragment.rstrip() + "\n" + after
```

- [ ] **Step 4: Add the marker pair to `README.md`**

Immediately after the live-status metadata and before `## How it works`, insert:

```markdown
<!-- AFFLR-RADAR:START -->
> Radar snapshot has not been refreshed on `main` yet.
<!-- AFFLR-RADAR:END -->
```

Keep `Evidence before attribution.` and all hand-written content outside the generated region.

- [ ] **Step 5: Add a failing dual-output CLI preservation test**

Extend `HttpAndCliTests` with a temporary directory containing both a full-output file and README. Patch `collect_live_views` to raise `RadarError` and assert both files remain byte-identical after `main(["--output", ..., "--readme", ...])` fails.

- [ ] **Step 6: Extend CLI to render both outputs before replacing either tracked destination**

Update argument parsing:

```python
parser.add_argument("--output", required=True)
parser.add_argument("--readme")
```

After collecting live views once:

```python
views = collect_live_views()
rendered_watchlist = render_markdown(views)
rendered_fragment = render_readme_fragment(views)
```

If `--readme` is supplied, read and validate the existing README and build `rendered_readme = inject_readme_fragment(existing, rendered_fragment)` before opening any tracked destination. Write both outputs to adjacent temporary files first; only after both writes succeed, atomically replace the requested destinations.

- [ ] **Step 7: Run GREEN and full suite**

```bash
python -m unittest tests.test_afflr -v
python -m py_compile scripts/afflr.py tests/test_afflr.py
```

Expected: all tests pass and compilation succeeds.

- [ ] **Step 8: Commit Task 2**

```bash
git add scripts/afflr.py tests/test_afflr.py README.md
git commit -m "feat: inject AFFLR radar safely into README"
```

---

### Task 3: Replace PR lifecycle with safe direct-to-main workflow

**Files:**
- Modify: `.github/workflows/afflr.yml`
- Modify: `tests/test_afflr.py`

**Interfaces:**
- Consumes: `python3 scripts/afflr.py --output /tmp/afflr-candidates.md --readme /tmp/README.md` only after copying current README to `/tmp/README.md`.
- Produces: no commit when bytes are unchanged; otherwise a normal bot commit containing only `README.md` and/or `watchlist/candidates.md`, pushed normally to `main`.

- [ ] **Step 1: Replace the old workflow contract test with Direct-Live assertions**

Update `WorkflowContractTests.test_workflow_contract` to require:

```python
self.assertIn("cron: '17 * * * *'", text)
self.assertIn("workflow_dispatch:", text)
self.assertIn("contents: write", text)
self.assertNotIn("pull-requests: write", text)
self.assertNotIn("automation/afflr", text)
self.assertNotIn("gh pr", text)
self.assertNotIn("--force-with-lease", text)
self.assertNotIn("git push --force", text)
self.assertIn("README.md", text)
self.assertIn("watchlist/candidates.md", text)
self.assertIn("git diff --quiet", text)
self.assertIn("git push origin HEAD:main", text)
self.assertIn("3d3c42e5aac5ba805825da76410c181273ba90b1", text)
```

Also assert the workflow has no reference to `cases/AFF-`.

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_afflr.WorkflowContractTests -v
```

Expected: failure because the workflow still contains the old automation branch and PR logic.

- [ ] **Step 3: Rewrite `.github/workflows/afflr.yml`**

Target structure:

```yaml
name: AFFLR — Anthropic Failure Forensics Live Radar

on:
  schedule:
    - cron: '17 * * * *'
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: afflr-live-radar
  cancel-in-progress: false

jobs:
  update-radar:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          ref: main
          fetch-depth: 0

      - name: Render AFFLR outputs
        shell: bash
        run: |
          set -euo pipefail
          cp README.md /tmp/README.md
          python3 scripts/afflr.py \
            --output /tmp/afflr-candidates.md \
            --readme /tmp/README.md

      - name: Apply generated outputs
        shell: bash
        run: |
          set -euo pipefail
          cp /tmp/afflr-candidates.md watchlist/candidates.md
          cp /tmp/README.md README.md

      - name: Commit and push changes
        shell: bash
        run: |
          set -euo pipefail

          if git diff --quiet -- README.md watchlist/candidates.md; then
            echo "AFFLR snapshot unchanged; nothing to commit."
            exit 0
          fi

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add README.md watchlist/candidates.md
          git commit -m "chore: refresh AFFLR live radar"

          git fetch origin main
          if [ "$(git rev-parse HEAD^)" != "$(git rev-parse origin/main)" ]; then
            echo "main moved during AFFLR render; refusing to overwrite concurrent changes" >&2
            exit 1
          fi

          git push origin HEAD:main
```

The parent-SHA check is deliberate: the generated commit must be directly based on the same remote `main` that was checked out. If `main` moved after checkout, fail instead of rebasing/merging generated data over an unrelated concurrent change.

- [ ] **Step 4: Run GREEN plus YAML parse check**

```bash
python -m unittest tests.test_afflr.WorkflowContractTests -v
python - <<'PY'
from pathlib import Path
import yaml
with Path('.github/workflows/afflr.yml').open(encoding='utf-8') as f:
    yaml.safe_load(f)
print('yaml ok')
PY
```

If PyYAML is unavailable in the execution environment, use the repository's existing YAML parser/check from the previous AFFLR verification instead; do not add a runtime dependency to the project.

- [ ] **Step 5: Commit Task 3**

```bash
git add .github/workflows/afflr.yml tests/test_afflr.py
git commit -m "feat: update AFFLR radar directly on main"
```

---

### Task 4: Seed the first Direct-Live README and watchlist from one verified snapshot

**Files:**
- Modify: `README.md`
- Modify: `watchlist/candidates.md`

**Interfaces:**
- Consumes: one successful live `collect_live_views()` result.
- Produces: README Top-5/details region and complete watchlist generated from that same in-memory views object.

- [ ] **Step 1: Render both outputs in one local command**

Run:

```bash
cp README.md /tmp/AFFLR-README.md
python3 scripts/afflr.py \
  --output /tmp/afflr-candidates.md \
  --readme /tmp/AFFLR-README.md
```

Expected: exit 0; no tracked file has changed yet.

- [ ] **Step 2: Inspect generated structure before applying**

Run checks equivalent to:

```python
from pathlib import Path
readme = Path('/tmp/AFFLR-README.md').read_text(encoding='utf-8')
watch = Path('/tmp/afflr-candidates.md').read_text(encoding='utf-8')
assert readme.count('<!-- AFFLR-RADAR:START -->') == 1
assert readme.count('<!-- AFFLR-RADAR:END -->') == 1
assert readme.count('<details>') == 3
assert readme.count('<summary>Show remaining 20</summary>') == 3
assert '## Most reacted' in watch
assert '## Most discussed' in watch
assert '## Recently active' in watch
```

- [ ] **Step 3: Apply both generated files together**

```bash
cp /tmp/AFFLR-README.md README.md
cp /tmp/afflr-candidates.md watchlist/candidates.md
```

- [ ] **Step 4: Verify README hand-written content survived unchanged outside the marker region**

Assert the title, live schedule `:17 UTC`, manual-trigger link, `How it works`, `What AFFLR does not do`, `Evidence before attribution.`, Ko-fi badge, and MIT license are still present.

- [ ] **Step 5: Run full test suite and compile check**

```bash
python -m unittest tests.test_afflr -v
python -m py_compile scripts/afflr.py tests/test_afflr.py
```

Expected: all tests pass.

- [ ] **Step 6: Commit Task 4**

```bash
git add README.md watchlist/candidates.md
git commit -m "chore: seed AFFLR Direct-Live snapshot"
```

---

### Task 5: Adversarial completion gate

**Files:**
- Verify all implementation files; do not add new files.

**Interfaces:**
- Confirms the branch is safe to integrate.

- [ ] **Step 1: Run the complete test suite fresh**

```bash
python -m unittest tests.test_afflr -v
```

Expected: zero failures.

- [ ] **Step 2: Run compilation fresh**

```bash
python -m py_compile scripts/afflr.py tests/test_afflr.py
```

Expected: exit 0.

- [ ] **Step 3: Verify scope against `main`**

```bash
git diff --name-only main...HEAD
```

Expected exactly:

```text
.github/workflows/afflr.yml
README.md
scripts/afflr.py
tests/test_afflr.py
watchlist/candidates.md
```

No `cases/`, methodology, design-plan, or unrelated file may appear on the implementation branch.

- [ ] **Step 4: Verify forbidden workflow behavior is absent**

Search `.github/workflows/afflr.yml` and assert absence of:

```text
pull-requests: write
automation/afflr
gh pr
--force-with-lease
git push --force
cases/AFF-
```

- [ ] **Step 5: Verify generated README safety properties**

Assert exactly one marker pair, exactly three `<details>` blocks, `Evidence before attribution.`, and that `README.md` contains no `AFF-001`…`AFF-005` legacy case index.

- [ ] **Step 6: Verify no-op determinism**

Using mocked fixed views, render the full watchlist and README fragment twice and assert byte equality. Then inject the same fragment into an already-generated README twice and assert the second output is byte-identical to the first.

- [ ] **Step 7: Review commit history**

```bash
git log --oneline main..HEAD
```

Expected: only Direct-Live implementation commits; no design/spec documents on the implementation branch.

- [ ] **Step 8: Stop at integration gate**

Do not merge automatically. Present the verified branch state and wait for explicit user authorization to integrate into `main`.
