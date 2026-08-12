# AFFLR Direct-Live README — Design

Date: 2026-08-12

## Goal

Make the AFFLR front page genuinely live: each successful hourly/manual radar run should update the objective issue snapshot on `main` directly and render a compact radar preview inside `README.md`, so visitors can see the important items without opening `watchlist/candidates.md`.

The design optimizes for QoL while preserving the core trust boundary: automation may update objective public GitHub metadata only; it may not create or modify forensic conclusions, root-cause claims, case acceptance, or reviewed findings.

## Current verified state

- The radar generator successfully produces all three Top-25 views.
- A manual `workflow_dispatch` run successfully rendered the snapshot and pushed `automation/afflr`.
- That run failed only at PR creation because repository settings do not permit GitHub Actions to create/approve pull requests.
- The current README links to `watchlist/candidates.md` but does not show the radar rows inline.

Direct-Live removes the unnecessary PR dependency for generated discovery metadata.

## Architecture

### Generated outputs

A successful run produces two deterministic outputs from the same normalized `views` object:

1. `watchlist/candidates.md` — complete 3 × Top-25 radar snapshot.
2. A README radar fragment — for each view, the first 5 rows are immediately visible and rows 6–25 are inside a native GitHub Markdown `<details>` block.

The README contains a generated region delimited by unique markers:

```markdown
<!-- AFFLR-RADAR:START -->
...generated radar fragment...
<!-- AFFLR-RADAR:END -->
```

The generator may replace only the bytes between these markers. The hand-written README content outside the markers is immutable from the automated workflow.

### README presentation

The live section remains near the top. Each view is rendered in this order:

- 🔥 Most reacted
- 💬 Most discussed
- 🆕 Recently active

For each view:

- rows 1–5 are shown immediately in a compact Markdown table;
- rows 6–25 are placed under `<details><summary>Show remaining 20</summary>...`;
- the same objective metadata columns remain available: Issue, Title, Author, State, Reactions, Comments, Updated, Created, Labels;
- open and closed issues remain mixed according to the upstream ranking;
- no synthetic score, inference, `NEW` flag, or state penalty is introduced.

The existing link to `watchlist/candidates.md` remains available as the full standalone snapshot.

## Direct-to-main update model

The workflow continues to run hourly at `17 * * * *` and via `workflow_dispatch`.

On a successful run it:

1. checks out current `main`;
2. renders the complete watchlist and README fragment to temporary files;
3. validates that the README contains exactly one start marker and one end marker in the correct order;
4. replaces only the generated README region;
5. copies the complete snapshot to `watchlist/candidates.md`;
6. compares both generated files with the checked-out tree;
7. if neither changed, exits without a commit;
8. if either changed, commits only `README.md` and/or `watchlist/candidates.md` with the GitHub Actions bot identity;
9. pushes the commit directly to `main` using the normal authenticated checkout credentials.

No `automation/afflr` branch, `gh pr create`, PR search, PR closing, or force push remains in the live update path.

## Concurrency and race safety

Keep the existing single workflow concurrency group with `cancel-in-progress: false` so two scheduled/manual radar writers do not intentionally overlap.

Before pushing, the workflow must integrate the current remote `main` safely rather than force-push. A normal push failure caused by concurrent repository changes is a hard failure; the job must not overwrite unrelated commits.

No force push to `main` is permitted.

## Failure behavior

The radar remains fail-closed.

- Search/API/JSON/normalization failure: do not touch README or watchlist.
- Missing/duplicate/inverted README markers: fail before editing any tracked file.
- Rendering failure: preserve the last known-good files.
- No generated change: no commit.
- Push conflict: fail without force-pushing.

The previous successful snapshot remains visible on `main` after any failed run.

## Trust boundary

Direct-Live automation is allowed to change only generated discovery metadata.

It must not mutate:

- `cases/`;
- methodology/evidence levels;
- forensic conclusions;
- evidence attribution;
- root-cause statements;
- issue acceptance/promotion decisions.

The README keeps the operating principle:

> **Evidence before attribution.**

## Files in implementation scope

- Modify `scripts/afflr.py` — reusable table rendering, README fragment rendering, marker-safe README injection/CLI outputs.
- Modify `tests/test_afflr.py` — TDD coverage for Top-5/details rendering, marker validation, byte stability, preservation of hand-written README content, and new workflow contract.
- Modify `.github/workflows/afflr.yml` — replace persistent-branch/PR lifecycle with safe direct commit/push to `main`.
- Modify `README.md` — add the generated markers and an initial live radar region.
- Modify `watchlist/candidates.md` — seed `main` with the already successfully generated current snapshot or regenerate from the same verified snapshot data during implementation.

No case or methodology files are modified.

## Acceptance criteria

1. The README contains exactly one `AFFLR-RADAR:START` and one `AFFLR-RADAR:END` marker.
2. Each of the three views displays exactly the first 5 rows directly.
3. Rows 6–25 are available under a native `<details>` block for the same view.
4. `watchlist/candidates.md` still contains the complete Top-25 × 3 snapshot.
5. README and watchlist are rendered from the same normalized issue views.
6. Identical input produces byte-identical output.
7. Untrusted issue/title/author/label text remains escaped as before.
8. The workflow remains hourly at `:17` plus manual dispatch.
9. The workflow no longer requires `pull-requests: write` and contains no `gh pr`, persistent automation branch, or force-with-lease logic.
10. A changed radar commits only generated `README.md` and `watchlist/candidates.md` content directly to `main`.
11. An unchanged radar creates no commit.
12. A missing or malformed README marker pair fails closed and preserves the previous files.
13. The workflow never force-pushes `main`.
14. No case, methodology, forensic conclusion, or evidence attribution is automatically modified.
15. `Evidence before attribution.` remains visible on the front page.
