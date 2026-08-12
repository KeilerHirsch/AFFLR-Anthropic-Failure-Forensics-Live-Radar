# Claude Issue Radar — Design

Date: 2026-08-12

## Purpose

Add a lightweight automated discovery layer to `anthropic-failure-forensics` that searches the full `anthropics/claude-code` issue corpus, including open and closed issues, and produces a reviewable candidate list without making forensic judgments or creating AFF cases automatically.

The radar is discovery metadata only. It must not convert popularity, labels, or activity into evidence levels, causal attribution, or AFF approval.

## Core principle

> **Collect and sort observable GitHub signals; do not automate forensic judgment.**

`Evidence before attribution` remains the repository rule. A radar entry is not evidence and is not an accepted case.

## Scope

The radar search scope is all issues in `anthropics/claude-code`:

- open issues;
- closed issues;
- closed/not-planned issues;
- duplicates and other closed lifecycle states when exposed by GitHub metadata.

The implementation uses GitHub's public issue search with `repo:anthropics/claude-code is:issue`, so pull requests are excluded by the search qualifier instead of being treated as candidates.

No external AI or LLM is used for discovery, ranking, summarization, or classification.

## Retrieval strategy

The upstream corpus is too large for an hourly full REST crawl. The radar therefore asks GitHub to rank the entire issue corpus and retrieves only the rows needed for the three views.

Each run performs exactly three upstream public search requests:

1. `repo:anthropics/claude-code is:issue sort:reactions-desc` with `per_page=25`;
2. `repo:anthropics/claude-code is:issue sort:comments-desc` with `per_page=25`;
3. `repo:anthropics/claude-code is:issue sort:updated-desc` with `per_page=25`.

The upstream search requests are intentionally unauthenticated so the repository-scoped `GITHUB_TOKEN` is never sent to another repository. Each response must report `incomplete_results: false`; otherwise the run fails closed.

The workflow token is used only for operations inside `KeilerHirsch/anthropic-failure-forensics`.

## Output

The generated file is:

`watchlist/candidates.md`

The file begins with a visible disclaimer that it is automated discovery metadata only and does not represent AFF acceptance, evidence level, or causal attribution.

Each issue row contains only observable GitHub metadata:

- issue number with direct upstream link;
- title;
- author;
- state/state reason when available;
- total reactions;
- reaction breakdown when present in the search response;
- comments;
- updated date;
- created date;
- labels.

## Rankings

There is no AFF score, forensic score, AI score, HOT/STRONG/WATCH classification, or inferred quality score.

The document contains three objective views, each limited to the top 25 issues returned by GitHub's corpus-wide sort.

### Most reacted

Source query: `sort:reactions-desc`.

Display order follows GitHub's returned order. Local deterministic tie-breaking is applied only if fixture/test data contains equal upstream rank inputs: comments descending, `updated_at` descending, then issue number descending.

### Most discussed

Source query: `sort:comments-desc`.

Display order follows GitHub's returned order. Local deterministic tie-breaking for equal fixture/test inputs: reactions descending, `updated_at` descending, then issue number descending.

### Recently active

Source query: `sort:updated-desc`.

Display order follows GitHub's returned order. Local deterministic tie-breaking for equal fixture/test inputs: reactions descending, comments descending, then issue number descending.

Open and closed issues are ranked together. Lifecycle state is displayed, not used as a hidden popularity penalty.

The same issue may appear in more than one view because the views answer different questions.

## NEW marker

An issue receives `NEW` when it appears in a top-25 view in the newly generated result but was absent from that same view in the baseline result on `main`.

If an issue drops out and later re-enters a view after the previous result has been merged to `main`, it may be marked `NEW` again.

The marker is purely a change indicator, not a quality signal.

## Workflow architecture

GitHub Actions runs the radar on:

- an hourly scheduled cadence;
- `workflow_dispatch` for manual runs.

Use a non-round cron minute while preserving one run per hour.

Data flow:

```text
GitHub Search over full anthropics/claude-code issue corpus
        ↓
3 objective sorted queries × 25 rows
        ↓
validate complete responses
        ↓
normalize observable metadata
        ↓
render watchlist/candidates.md
        ↓
compare with current generated result
        ↓
no change → no commit / no PR update
changed   → update automation branch / PR
```

## PR model

Use a persistent automation branch:

`automation/claude-issue-radar`

Use at most one open radar PR against `main`, with a stable title such as:

`chore: update Claude issue radar`

Each workflow run:

1. starts from the current `main` baseline;
2. fetches the three upstream search views;
3. renders the new candidate file;
4. exits without a commit if there is no content change;
5. resets/updates the persistent automation branch from current `main` plus the generated change;
6. creates the radar PR if none is open, otherwise updates the existing PR through the branch.

The workflow must not create a fresh PR on every scheduled run.

Merging the PR establishes the new `main` baseline for future `NEW` detection.

The radar must never create `AFF-###` directories, edit existing case evidence claims, or auto-promote an issue into the case index.

## README change

The root `README.md` must receive a small, non-promotional section explaining the radar.

It should state that:

- the repository has an automated Claude issue radar;
- the radar searches open and closed `anthropics/claude-code` issues;
- it exposes top views by reactions, discussion, and recent activity;
- radar entries are discovery metadata only;
- AFF inclusion still requires manual evidence review.

The README should link to `watchlist/candidates.md`.

This README change must preserve the existing `Evidence before attribution` framing and must not imply that GitHub popularity is evidence.

## Permissions and security

No personal access token, GitHub App credential, or third-party secret is required.

The upstream search is public and unauthenticated. `GITHUB_TOKEN` is used only inside the workflow repository.

Use explicit least-privilege workflow permissions:

```yaml
permissions:
  contents: write
  pull-requests: write
```

No external AI services, analytics endpoints, telemetry, or third-party actions are required. A GitHub-maintained checkout action is acceptable for repository checkout.

## Failure behavior

The workflow must fail closed.

If an upstream HTTP request, rate limit, JSON parse, required field validation, `incomplete_results` check, normalization, rendering, git operation, or PR operation fails:

- do not replace the existing watchlist on `main`;
- do not commit a partial result;
- do not report success;
- leave the last known-good generated output untouched.

## Determinism

Given identical search responses and identical `main` baseline, the renderer must produce byte-stable output.

Requirements:

- deterministic local tie-breakers;
- stable label ordering;
- stable date formatting;
- Markdown escaping for titles/authors/labels where required;
- no generated timestamps that cause meaningless diffs.

## Tests and acceptance criteria

The implementation is acceptable only when tests demonstrate all of the following:

1. Search scope uses `repo:anthropics/claude-code is:issue` for all three views.
2. Open and closed issues are both preserved from search results.
3. Closed/not-planned or duplicate state reasons are preserved when available.
4. Most-reacted uses the reactions-sorted upstream query.
5. Most-discussed uses the comments-sorted upstream query.
6. Recently-active uses the updated-sorted upstream query.
7. Exactly 25 results are requested independently per view.
8. `NEW` is calculated independently per view against the `main` baseline.
9. An issue may appear in multiple views.
10. Markdown-special characters in upstream metadata cannot corrupt the table.
11. A response with `incomplete_results: true` fails without producing replacement output.
12. HTTP/rate-limit/JSON/required-field failure cannot replace the last known-good watchlist.
13. An unchanged render produces no content commit.
14. Output is deterministic for identical input and baseline.
15. No workflow path creates or edits `AFF-###` case content automatically.
16. README describes the radar as discovery metadata and links the generated watchlist.
17. Scheduled workflow cadence is exactly once per hour and uses a non-round cron minute.
18. No personal token or third-party secret is required.
19. The workflow never sends `GITHUB_TOKEN` to the upstream search endpoint.

## Non-goals

This feature does not:

- assign AFF evidence levels;
- infer root cause;
- determine whether an issue is true;
- summarize issue bodies with AI;
- score authors;
- auto-comment upstream;
- auto-create AFF cases;
- monitor Reddit or other external platforms;
- maintain a local mirror of the full Claude issue corpus;
- create a database, dashboard, or generated site.

## Expected repository additions

Implementation is expected to remain small and isolated, approximately:

```text
.github/workflows/claude-issue-radar.yml
scripts/claude_issue_radar.py
watchlist/candidates.md
tests/test_claude_issue_radar.py
README.md                     # small radar section only
```

Exact filenames may change in the implementation plan if the same boundaries and behavior are preserved.

## Final design invariant

The automation may decide **where an issue appears in an objective metadata view**.

It may not decide **whether the issue deserves to become forensic evidence**.
