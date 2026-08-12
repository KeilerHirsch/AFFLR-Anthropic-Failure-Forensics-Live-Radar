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
        self.assertEqual(text.count(afflr.TABLE_HEADER), 6)
        self.assertEqual(text.count(afflr.TABLE_RULE), 6)
        for number in range(1, 6):
            self.assertIn(f"[#{number}]", text)
        self.assertIn("[#6]", text)
        self.assertIn("[#25]", text)
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_afflr.RenderingTests -v
```

Expected: failure because `render_readme_fragment` and the table constants do not exist.

- [ ] **Step 3: Extract one canonical row renderer**

Add to `scripts/afflr.py`:

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

Refactor `render_markdown()` to use these constants and `render_table_rows()` without changing its output bytes for identical views.

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

```bash
python -m unittest tests.test_afflr.RenderingTests -v
python -m unittest tests.test_afflr -v
```

Expected: all rendering tests and the full suite pass.

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
- Extends CLI with optional `--readme`; `--output` remains required for the full snapshot.

- [ ] **Step 1: Add failing marker-safety tests**

Append to `RenderingTests`:

```python
    def test_inject_readme_fragment_preserves_outside_content(self):
        original = "before\n<!-- AFFLR-RADAR:START -->\nold\n<!-- AFFLR-RADAR:END -->\nafter\n"
        updated = afflr.inject_readme_fragment(original, "new\n")
        self.assertEqual(
            updated,
            "before\n<!-- AFFLR-RADAR:START -->\nnew\n<!-- AFFLR-RADAR:END -->\nafter\n",
        )

    def test_inject_readme_fragment_rejects_invalid_markers(self):
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

Expected: marker helper failures.

- [ ] **Step 3: Implement exact marker validation and injection**

Add:

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

Keep all hand-written content outside the generated region.

- [ ] **Step 5: Add a failing dual-output preservation test**

Append to `HttpAndCliTests`:

```python
    def test_cli_failure_preserves_watchlist_and_readme(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "radar.md"
            readme = Path(tmp) / "README.md"
            output.write_text("last known watchlist\n", encoding="utf-8")
            readme.write_text(
                "before\n<!-- AFFLR-RADAR:START -->\nold\n<!-- AFFLR-RADAR:END -->\nafter\n",
                encoding="utf-8",
            )
            before_output = output.read_bytes()
            before_readme = readme.read_bytes()

            with patch.object(
                afflr, "collect_live_views", side_effect=afflr.RadarError("boom")
            ):
                with self.assertRaises(afflr.RadarError):
                    afflr.main([
                        "--output", str(output),
                        "--readme", str(readme),
                    ])

            self.assertEqual(output.read_bytes(), before_output)
            self.assertEqual(readme.read_bytes(), before_readme)
```

- [ ] **Step 6: Extend CLI to render and validate both outputs before replacing either destination**

Argument parsing:

```python
parser.add_argument("--output", required=True)
parser.add_argument("--readme")
```

Single collection/render phase:

```python
views = collect_live_views()
rendered_watchlist = render_markdown(views)
rendered_fragment = render_readme_fragment(views)
```

If `--readme` is supplied, read it and build `rendered_readme = inject_readme_fragment(existing, rendered_fragment)` before opening either destination. Write requested outputs to adjacent `.tmp` files first. After every collection, validation, rendering, and temp write succeeds, replace the destinations. Rendering/validation failure must occur before any tracked destination is replaced.

- [ ] **Step 7: Run GREEN and compilation checks**

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
- Consumes current `main`, current README marker pair, and `scripts/afflr.py` dual-output CLI.
- Produces no commit on unchanged bytes; otherwise one normal bot commit containing only generated `README.md` and/or `watchlist/candidates.md`, then a normal push to `main`.

- [ ] **Step 1: Replace the old workflow contract test with Direct-Live assertions**

Use:

```python
class WorkflowContractTests(unittest.TestCase):
    def test_workflow_contract(self):
        text = Path(".github/workflows/afflr.yml").read_text(encoding="utf-8")
        self.assertIn("name: AFFLR", text)
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("contents: write", text)
        self.assertNotIn("pull-requests: write", text)
        self.assertNotIn("automation/afflr", text)
        self.assertNotIn("gh pr", text)
        self.assertNotIn("--force-with-lease", text)
        self.assertNotIn("git push --force", text)
        self.assertNotIn("cases/AFF-", text)
        self.assertIn("README.md", text)
        self.assertIn("watchlist/candidates.md", text)
        self.assertIn("git diff --quiet", text)
        self.assertIn("git push origin HEAD:main", text)
        self.assertIn("3d3c42e5aac5ba805825da76410c181273ba90b1", text)
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_afflr.WorkflowContractTests -v
```

Expected: failure because old PR/automation-branch behavior is still present.

- [ ] **Step 3: Rewrite `.github/workflows/afflr.yml`**

Use this complete target structure:

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

The parent-SHA check ensures a generated commit is pushed only if remote `main` is still the exact parent it was rendered from. No rebase, merge, or force push is permitted in this workflow.

- [ ] **Step 4: Run GREEN and static workflow checks**

```bash
python -m unittest tests.test_afflr.WorkflowContractTests -v
python - <<'PY'
from pathlib import Path
text = Path('.github/workflows/afflr.yml').read_text(encoding='utf-8')
assert text.count("cron: '17 * * * *'") == 1
assert 'workflow_dispatch:' in text
assert 'permissions:\n  contents: write' in text
assert 'pull-requests: write' not in text
assert 'automation/afflr' not in text
assert 'gh pr' not in text
assert '--force-with-lease' not in text
assert 'git push --force' not in text
assert 'git push origin HEAD:main' in text
print('workflow contract ok')
PY
```

Expected: both commands pass. No new parser dependency is introduced.

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
- Consumes one successful live `collect_live_views()` result.
- Produces README Top-5/details region and complete watchlist generated from that same views object.

- [ ] **Step 1: Render both outputs from one live collection without touching tracked files**

```bash
cp README.md /tmp/AFFLR-README.md
python3 scripts/afflr.py \
  --output /tmp/afflr-candidates.md \
  --readme /tmp/AFFLR-README.md
```

Expected: exit 0.

- [ ] **Step 2: Validate generated structure**

```bash
python - <<'PY'
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
print('generated structure ok')
PY
```

- [ ] **Step 3: Apply both generated files together**

```bash
cp /tmp/AFFLR-README.md README.md
cp /tmp/afflr-candidates.md watchlist/candidates.md
```

- [ ] **Step 4: Verify hand-written README content survived outside the generated region**

```bash
python - <<'PY'
from pathlib import Path
text = Path('README.md').read_text(encoding='utf-8')
for required in [
    '# AFFLR — Anthropic Failure Forensics Live Radar',
    'every hour at **`:17 UTC`**',
    'GitHub Actions',
    '## How it works',
    '## What AFFLR does not do',
    'Evidence before attribution.',
    'ko-fi.com/keilerhirsch',
    'MIT. See [`LICENSE`](LICENSE).',
]:
    assert required in text, required
print('hand-written README content preserved')
PY
```

- [ ] **Step 5: Run full test and compile checks**

```bash
python -m unittest tests.test_afflr -v
python -m py_compile scripts/afflr.py tests/test_afflr.py
```

Expected: zero failures.

- [ ] **Step 6: Commit Task 4**

```bash
git add README.md watchlist/candidates.md
git commit -m "chore: seed AFFLR Direct-Live snapshot"
```

---

### Task 5: Adversarial completion gate

**Files:**
- Verify only; create no new implementation files.

**Interfaces:**
- Confirms the branch is safe to present for integration.

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

- [ ] **Step 3: Verify implementation scope against `main`**

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

- [ ] **Step 4: Verify forbidden workflow behavior is absent**

```bash
python - <<'PY'
from pathlib import Path
text = Path('.github/workflows/afflr.yml').read_text(encoding='utf-8')
for forbidden in [
    'pull-requests: write',
    'automation/afflr',
    'gh pr',
    '--force-with-lease',
    'git push --force',
    'cases/AFF-',
]:
    assert forbidden not in text, forbidden
print('forbidden workflow behavior absent')
PY
```

- [ ] **Step 5: Verify generated README safety properties**

```bash
python - <<'PY'
from pathlib import Path
text = Path('README.md').read_text(encoding='utf-8')
assert text.count('<!-- AFFLR-RADAR:START -->') == 1
assert text.count('<!-- AFFLR-RADAR:END -->') == 1
assert text.count('<details>') == 3
assert 'Evidence before attribution.' in text
for legacy in ['AFF-001', 'AFF-002', 'AFF-003', 'AFF-004', 'AFF-005']:
    assert legacy not in text, legacy
print('README safety properties ok')
PY
```

- [ ] **Step 6: Add and run an idempotence test before final integration**

Add to `RenderingTests`:

```python
    def test_readme_injection_is_idempotent_for_same_fragment(self):
        issue = afflr.normalize_issue(self.sample_issue())
        views = {name: [issue] for name in afflr.VIEW_ORDER}
        fragment = afflr.render_readme_fragment(views)
        original = (
            "before\n"
            f"{afflr.README_START}\n"
            "old\n"
            f"{afflr.README_END}\n"
            "after\n"
        )
        once = afflr.inject_readme_fragment(original, fragment)
        twice = afflr.inject_readme_fragment(once, fragment)
        self.assertEqual(once, twice)
```

Run:

```bash
python -m unittest tests.test_afflr.RenderingTests.test_readme_injection_is_idempotent_for_same_fragment -v
python -m unittest tests.test_afflr -v
```

Expected: idempotence test and full suite pass.

Commit this final test with:

```bash
git add tests/test_afflr.py
git commit -m "test: verify AFFLR README idempotence"
```

- [ ] **Step 7: Review commit history**

```bash
git log --oneline main..HEAD
```

Expected: only Direct-Live implementation/test commits; no `docs/superpowers/` files on the implementation branch.

- [ ] **Step 8: Stop at integration gate**

Do not merge automatically. Present the verified branch state and wait for explicit user authorization to integrate into `main`.
