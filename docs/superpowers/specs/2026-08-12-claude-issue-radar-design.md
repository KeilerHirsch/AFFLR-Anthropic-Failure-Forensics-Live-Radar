# Claude Issue Radar — Design

Date: 2026-08-12

## Purpose

Add a lightweight automated discovery layer to `anthropic-failure-forensics` that scans all issues in `anthropics/claude-code`, including open and closed issues, and produces a reviewable candidate list without making forensic judgments or creating AFF cases automatically.

The radar is discovery metadata only. It must not convert popularity, labels, or activity into evidence levels, causal attribution, or AFF approval.

## Core principle

> **Collect and sort observable GitHub signals; do not automate forensic judgment.**

`Evidence before attribution` remains the repository rule. A radar entry is not evidence and is not an accepted case.

## Scope

The radar monitors all issues in `anthropics/claude-code`:

- open issues;
- closed issues;
- closed/not-planned issues;
- duplicates and other closed lifecycle states when exposed by GitHub metadata.

Pull requests returned by issue-list endpoints must be excluded explicitly.

No external AI or LLM is used for discovery, ranking, summarization, or classification.

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
- comments;
- updated date;
- created date;
- labels.

If the API exposes reliable per-reaction counts in the implementation path, the renderer may additionally display reaction types such as `👍`, `❤️`, or `🚀`; the total reaction count remains the required field.

## Rankings

There is no AFF score, forensic score, AI score, HOT/STRONG/WATCH classification, or inferred quality score.

The document contains three objective views, each limited to the top 25 issues:

### Most reacted

Sort keys, in order:

1. reactions descending;
2. comments descending;
3. `updated_at` descending;
4. issue number descending as deterministic final tie-breaker.

### Most discussed

Sort keys, in order:

1. comments descending;
2. reactions descending;
3. `updated_at` descending;
4. issue number descending.

### Recently active

Sort keys, in order:

1. `updated_at` descending;
2. reactions descending;
3. comments descending;
4. issue number descending.

Open and closed issues are ranked together. Lifecycle state is displayed, not used as a hidden popularity penalty.

The same issue may appear in more than one view because the views answer different questions.

## NEW marker

An issue receives `NEW` when it appears in a top-25 view in the newly generated result but was absent from that same view in the baseline result on `main`.

If an issue drops out and later re-enters a view after the previous result has been merged to `main`, it may be marked `NEW` again.

The marker is purely a change indicator, not a quality signal.

## Workflow architecture

GitHub Actions runs the radar on:

- a scheduled cadence twice per day;
- `workflow_dispatch` for manual runs.

The implementation should use non-round cron minutes to reduce scheduled-run congestion; the implementation plan may choose the exact minute while preserving the twice-daily cadence.

Data flow:

```text
anthropics/claude-code issues
        ↓
collector
        ↓
exclude pull requests
        ↓
normalize observable metadata
        ↓
three deterministic rankings
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

1. fetches the current upstream issue data;
2. renders the new candidate file;
3. compares it with the current generated file;
4. exits without a commit if there is no content change;
5. updates the persistent automation branch if content changed;
6. creates the radar PR if none is open, otherwise updates the existing PR through the branch.

The workflow must not create a fresh PR on every scheduled run.

Merging the PR establishes the new `main` baseline for future `NEW` detection.

The radar must never create `AFF-###` directories, edit existing case evidence claims, or auto-promote an issue into the case index.

## README change

The root `README.md` must receive a small, non-promotional section explaining the radar.

It should state that:

- the repository has an automated Claude issue radar;
- the radar scans open and closed `anthropics/claude-code` issues;
- it sorts candidates by reactions, discussion, and recent activity;
- radar entries are discovery metadata only;
- AFF inclusion still requires manual evidence review.

The README should link to `watchlist/candidates.md`.

This README change must preserve the existing `Evidence before attribution` framing and must not imply that GitHub popularity is evidence.

## Permissions and security

No repository or third-party secret is required beyond GitHub's workflow token.

Use explicit least-privilege workflow permissions. The expected maximum permissions are:

```yaml
permissions:
  contents: write
  pull-requests: write
```

If implementation can reduce either permission further while retaining the persistent-branch PR model, prefer the narrower permission set.

No external executable downloads, AI services, analytics endpoints, or telemetry are required.

## Failure behavior

The workflow must fail closed.

If collection, pagination, API parsing, normalization, or rendering fails:

- do not overwrite the existing watchlist;
- do not commit a partial result;
- do not report success;
- leave the last known-good generated output untouched.

Rate-limit errors and incomplete pagination are failures, not successful partial scans.

## Determinism

Given identical GitHub metadata, the renderer must produce byte-stable output.

Requirements:

- deterministic tie-breakers;
- stable label ordering;
- stable date formatting;
- Markdown escaping for titles/authors/labels where required;
- no generated timestamps that cause meaningless diffs unless they represent actual source data.

## Tests and acceptance criteria

The implementation is acceptable only when tests demonstrate all of the following:

1. Pull requests returned by issue endpoints are excluded.
2. Open and closed issues are both included.
3. Closed/not-planned or duplicate states are preserved when available.
4. Reaction ranking uses the documented tie-breakers.
5. Comment ranking uses the documented tie-breakers.
6. Recent-activity ranking uses the documented tie-breakers.
7. The top-25 limit is applied independently per view.
8. `NEW` is calculated independently per view against the `main` baseline.
9. An issue may appear in multiple views.
10. Markdown-special characters in upstream metadata cannot corrupt the table.
11. Pagination handles repositories with more than one API page of issues.
12. An unchanged render produces no content commit.
13. API/rate-limit/parsing failure cannot replace the last known-good watchlist.
14. Output is deterministic for identical input.
15. No workflow path creates or edits `AFF-###` case content automatically.
16. README describes the radar as discovery metadata and links the generated watchlist.

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
