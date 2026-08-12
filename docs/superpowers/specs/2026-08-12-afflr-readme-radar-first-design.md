# AFFLR Radar-First README — Design

Date: 2026-08-12

## Goal

Rewrite the root `README.md` so the repository presents its current identity first: **AFFLR — Anthropic Failure Forensics Live Radar**.

The README should be short, immediately understandable, and centered on the hourly issue-discovery radar rather than the older AFF case/archive framing.

## Scope

This change modifies only `README.md`.

Existing historical files such as `cases/`, methodology documents, issue templates, the radar workflow, scripts, tests, and watchlist remain untouched in this pass.

## Remove from the README

Remove the legacy material that no longer represents the current front-page purpose:

- the `AFF-001` through `AFF-005` case index;
- the full L0–L5 evidence ladder table;
- the dedicated public-upstream-reports list;
- the `Adding another finding` instructions;
- wording that presents the project primarily as a manually curated AFF case archive;
- repeated explanation of legacy AFF promotion/acceptance mechanics.

The phrase **Evidence before attribution** remains as a compact operating principle.

## New README structure

### 1. Project header

Use:

`# AFFLR — Anthropic Failure Forensics Live Radar`

Follow with one short paragraph explaining that AFFLR watches the public `anthropics/claude-code` issue space and surfaces objective GitHub signals so important failures and regressions are easier to discover.

### 2. Live status / schedule block

Near the top, show a compact status block with the real workflow schedule:

- automatic scan: hourly;
- trigger minute: `:17` UTC;
- manual trigger: available through GitHub Actions;
- link to the AFFLR workflow;
- link to `watchlist/candidates.md`.

The README must not pretend to display a real-time countdown. It should state the deterministic schedule, for example:

`⏱ Next automatic trigger: every hour at :17 UTC`

This avoids external services, dynamic SVG dependencies, and hourly README churn.

### 3. What the radar shows

Explain the three objective Top-25 views:

- 🔥 Most reacted
- 💬 Most discussed
- 🆕 Recently active

State that both open and closed issues are included.

Mention the useful metadata only once: issue/link, author, state, reactions, comments, timestamps, and labels.

### 4. How it works

Use a compact flow:

`public Claude Code issues → hourly scan → objective metadata ranking → review PR → human review`

The automation must be described as discovery infrastructure, not an automatic truth or root-cause engine.

### 5. What AFFLR does not do

Keep this concise:

- no AI-generated importance score;
- no automatic root-cause claims;
- no automatic forensic conclusions;
- no direct rewriting of reviewed findings based only on popularity.

Close with:

`Evidence before attribution.`

### 6. Support and license

Preserve the existing Ko-fi support badge and MIT license link.

## Tone

The README should be technical, compact, and readable at a glance.

Small dry humor is acceptable, but the front page should not become a Reddit post or a wall of text.

## Acceptance criteria

The final README is acceptable when:

1. the title is AFFLR-first;
2. the old AFF case index is gone;
3. the L0–L5 table is gone;
4. legacy case-creation instructions are gone;
5. the hourly `:17 UTC` schedule is visible near the top;
6. the three Top-25 views are immediately visible;
7. the watchlist and workflow are directly linked;
8. no external countdown/timer dependency is introduced;
9. `Evidence before attribution` remains;
10. Ko-fi and MIT license information remain;
11. no files other than `README.md` are changed by the implementation PR.
