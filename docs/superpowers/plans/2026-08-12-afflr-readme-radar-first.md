# AFFLR Radar-First README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the root README so AFFLR presents the live issue radar first, removes outdated AFF case/archive front-page material, and shows the real hourly `:17 UTC` trigger schedule near the top.

**Architecture:** This is a documentation-only change. `README.md` becomes the concise public landing page; the existing workflow, watchlist, scripts, tests, historical case files, and methodology remain untouched. The timer is a static schedule/status block derived from the existing GitHub Actions cron rather than a fake live countdown or external service.

**Tech Stack:** GitHub Markdown, existing GitHub Actions workflow metadata.

## Global Constraints

- Modify only `README.md` in the implementation PR.
- Title must remain `# AFFLR — Anthropic Failure Forensics Live Radar`.
- Automatic scan schedule must be described as hourly at `:17 UTC`.
- Manual trigger through GitHub Actions must be mentioned.
- Link directly to `.github/workflows/afflr.yml` and `watchlist/candidates.md`.
- Show the three objective Top-25 views: Most reacted, Most discussed, Recently active.
- State that open and closed issues are included.
- Remove the legacy `AFF-001` through `AFF-005` case index from the README.
- Remove the L0–L5 evidence ladder table from the README.
- Remove the dedicated legacy upstream-report list and `Adding another finding` section.
- Do not delete or rewrite historical `cases/`, methodology, workflow, scripts, tests, or watchlist files.
- Do not introduce an external countdown service, dynamic SVG, JavaScript, or hourly README rewrite.
- Keep `Evidence before attribution.` as the operating principle.
- Preserve the existing Ko-fi support badge and MIT license link.

---

### Task 1: Replace README with radar-first landing page

**Files:**
- Modify: `README.md`
- Test: content assertions against `README.md`

**Interfaces:**
- Consumes: existing workflow schedule `.github/workflows/afflr.yml` with cron `17 * * * *`; existing radar output `watchlist/candidates.md`.
- Produces: a concise GitHub landing page whose links and schedule text match those existing files.

- [ ] **Step 1: Capture the current README and verify legacy material is present before the rewrite**

Run equivalent content checks against the current `README.md`:

```python
from pathlib import Path
text = Path("README.md").read_text(encoding="utf-8")
assert "AFF-001" in text
assert "## Evidence levels" in text
assert "## Adding another finding" in text
```

Expected: PASS on the pre-change README. These assertions establish the exact legacy material the rewrite removes.

- [ ] **Step 2: Replace `README.md` with the approved radar-first copy**

Use this complete target content:

```markdown
# AFFLR — Anthropic Failure Forensics Live Radar

AFFLR watches the public [`anthropics/claude-code`](https://github.com/anthropics/claude-code/issues) issue space and surfaces the strongest GitHub activity signals so interesting failures, regressions, and weird behavior are harder to miss.

> **Automation for productive laziness.** The radar does the repetitive watching; humans still decide what the evidence means.

## 🛰️ Live radar status

**⏱ Next automatic trigger:** every hour at **`:17 UTC`**  
**🔁 Schedule:** hourly  
**▶️ Manual trigger:** available in [GitHub Actions](../../actions/workflows/afflr.yml)  
**📡 Current radar output:** [`watchlist/candidates.md`](watchlist/candidates.md)

AFFLR currently exposes three objective Top-25 views:

- 🔥 **Most reacted**
- 💬 **Most discussed**
- 🆕 **Recently active**

Open and closed issues are included. The radar records useful public metadata such as the issue link, author, state, reactions, comments, timestamps, and labels.

## How it works

```text
public Claude Code issues
        ↓
hourly scan
        ↓
objective GitHub metadata
        ↓
review PR
        ↓
human review
```

The radar is discovery infrastructure, not an automatic truth machine.

## What AFFLR does not do

- No AI-generated importance score.
- No automatic root-cause claims.
- No automatic forensic conclusions.
- No rewriting reviewed findings just because an issue is popular.

> **Evidence before attribution.**

## Support

If AFFLR saves you debugging time or helps you spot something worth investigating, you can support the forensic hamster maintenance here:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?style=flat&logo=kofi&logoColor=white)](https://ko-fi.com/keilerhirsch)

## License

MIT. See [`LICENSE`](LICENSE).
```

- [ ] **Step 3: Run positive acceptance checks**

Run:

```python
from pathlib import Path
text = Path("README.md").read_text(encoding="utf-8")
required = [
    "# AFFLR — Anthropic Failure Forensics Live Radar",
    "every hour at **`:17 UTC`**",
    "GitHub Actions",
    "watchlist/candidates.md",
    "Most reacted",
    "Most discussed",
    "Recently active",
    "Open and closed issues are included",
    "Evidence before attribution.",
    "ko-fi.com/keilerhirsch",
    "LICENSE",
]
for item in required:
    assert item in text, item
```

Expected: PASS with no assertion failures.

- [ ] **Step 4: Run negative legacy-content checks**

Run:

```python
from pathlib import Path
text = Path("README.md").read_text(encoding="utf-8")
for forbidden in [
    "AFF-001",
    "AFF-002",
    "AFF-003",
    "AFF-004",
    "AFF-005",
    "## Evidence levels",
    "## Adding another finding",
    "## Public upstream reports",
    "| **L0** |",
    "| **L5** |",
]:
    assert forbidden not in text, forbidden
```

Expected: PASS with no assertion failures.

- [ ] **Step 5: Verify the implementation diff contains only `README.md`**

Run the equivalent of:

```bash
git diff --name-only main...HEAD
```

Expected output:

```text
README.md
```

No workflow, script, test, watchlist, case, methodology, or planning file may appear in the implementation PR.

- [ ] **Step 6: Commit the README rewrite**

```bash
git add README.md
git commit -m "docs: make AFFLR README radar-first"
```

- [ ] **Step 7: Fresh-fetch the committed README and repeat Steps 3–5 before opening the PR**

Expected: all positive assertions pass, all legacy assertions pass, and the implementation branch remains a one-file diff against `main`.
