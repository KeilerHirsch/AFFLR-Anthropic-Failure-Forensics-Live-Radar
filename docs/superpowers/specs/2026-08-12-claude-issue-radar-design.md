# Claude Issue Radar — Design

Date: 2026-08-12

## Purpose

Add a lightweight automated discovery layer to `anthropic-failure-forensics` that searches the full public `anthropics/claude-code` issue corpus, including open and closed issues, and proposes objective candidate-list updates through one reviewable pull request.

The radar is discovery metadata only. It must not convert popularity, labels, reactions, comments, or activity into evidence levels, causal attribution, or AFF approval.

## Core principle

> **Collect and sort observable GitHub signals; do not automate forensic judgment.**

`Evidence before attribution` remains the repository rule. A radar entry is not evidence and is not an accepted case.

## Search scope

All three views use this corpus-wide qualifier:

`repo:anthropics/claude-code is:issue`

This includes open and closed issues and excludes pull requests by query semantics.

No external AI or LLM is used.

## Retrieval strategy

The upstream corpus is too large for an hourly full REST crawl. GitHub's search service therefore performs the corpus-wide sorting and the radar retrieves only the rows needed for each view.

Exactly three public, unauthenticated search requests are made per run:

1. `repo:anthropics/claude-code is:issue sort:reactions-desc` with `per_page=25`;
2. `repo:anthropics/claude-code is:issue sort:comments-desc` with `per_page=25`;
3. `repo:anthropics/claude-code is:issue sort:updated-desc` with `per_page=25`.

Each response must report `incomplete_results: false`. Any HTTP, rate-limit, parse, or validation failure aborts the run without replacing the last known-good watchlist.

The upstream requests are deliberately unauthenticated. `GITHUB_TOKEN` is never sent to `api.github.com/search/issues`; it is used only for writes and pull-request operations inside `KeilerHirsch/anthropic-failure-forensics`.

## Generated output

The generated file is:

`watchlist/candidates.md`

Each row contains only observable GitHub metadata:

- issue number with direct upstream link;
- title;
- author;
- state and state reason when available;
- total reaction count;
- reaction breakdown when returned by GitHub;
- comments;
- updated date;
- created date;
- labels.

The file begins with a visible disclaimer that radar inclusion is not AFF acceptance, an evidence level, or causal attribution.

## Objective views

There is no AFF score, forensic score, AI score, HOT/STRONG/WATCH classification, or inferred quality score.

The generated file contains three Top-25 sections:

### Most reacted

GitHub query sort: `sort:reactions-desc`.

### Most discussed

GitHub query sort: `sort:comments-desc`.

### Recently active

GitHub query sort: `sort:updated-desc`.

Open and closed issues are ranked together. Lifecycle state is displayed, not used as a hidden penalty. The same issue may appear in more than one view.

Changes are communicated by the normal Git pull-request diff. No persistent `NEW` marker is stored in the generated file; this avoids stale markers and cleanup-only pull requests.

## Workflow cadence

GitHub Actions runs:

- exactly once per hour at a non-round cron minute;
- manually through `workflow_dispatch`.

Hourly checks do not imply hourly commits. If the generated file is byte-identical to the current `main` snapshot, the workflow exits without a commit or PR update.

## PR model

Use one persistent automation branch:

`automation/claude-issue-radar`

Use at most one open pull request against `main` with a stable title such as:

`chore: update Claude issue radar`

Each changed run starts from current `main`, writes the new radar snapshot onto the persistent branch, and creates the PR only if no open radar PR already exists. Subsequent changed runs update that same branch and therefore the same PR.

Merging remains a human review gate. The radar must never create `AFF-###` directories, edit case evidence claims, or auto-promote an issue into the case index.

## README change

The root `README.md` receives a small section that:

- links to `watchlist/candidates.md`;
- states that the radar checks the public Claude issue corpus hourly;
- explains the three objective Top-25 views;
- states that updates are proposed through a review PR;
- explicitly says that reactions/comments/activity are discovery signals, not evidence;
- preserves the existing `Evidence before attribution` framing.

## Permissions and security

No PAT, GitHub App credential, or third-party secret is required.

Workflow permissions are explicitly limited to:

```yaml
permissions:
  contents: write
  pull-requests: write
```

No external AI service, telemetry, analytics endpoint, third-party Python package, or third-party GitHub Action is required. A GitHub-maintained checkout action is acceptable.

## Determinism

For identical GitHub search responses, the renderer must produce byte-stable output.

Requirements:

- stable label ordering;
- stable date formatting;
- safe Markdown table escaping;
- deterministic local tie-breaking when fixture/test inputs contain equal primary sort values;
- no generated timestamp or total-corpus counter that creates meaningless diffs.

## Acceptance criteria

1. All three queries use `repo:anthropics/claude-code is:issue`.
2. The reacted view requests `sort:reactions-desc&per_page=25`.
3. The discussed view requests `sort:comments-desc&per_page=25`.
4. The activity view requests `sort:updated-desc&per_page=25`.
5. Open and closed issue metadata is preserved.
6. State reason is displayed when available.
7. Reactions, comments, author, dates, labels, title, and direct issue link are displayed.
8. `incomplete_results: true` is a hard failure.
9. HTTP/rate-limit/JSON/required-field failures cannot replace the last known-good snapshot.
10. Identical source responses produce identical Markdown.
11. Markdown-special characters cannot corrupt the table.
12. No persistent `NEW` marker or inferred score exists.
13. An unchanged render produces no commit or PR update.
14. At most one open radar PR exists.
15. The workflow runs once per hour at a non-round minute and also supports manual dispatch.
16. No workflow path creates or modifies `AFF-###` case content.
17. `GITHUB_TOKEN` is never sent to the public upstream search endpoint.
18. README describes the radar as discovery metadata and explains the PR review gate.

## Expected repository additions

```text
.github/workflows/claude-issue-radar.yml
scripts/claude_issue_radar.py
watchlist/candidates.md
tests/test_claude_issue_radar.py
README.md
```

## Final design invariant

The automation may decide **which objective GitHub metadata appears in each Top-25 view**.

It may not decide **whether an issue deserves to become forensic evidence**.
