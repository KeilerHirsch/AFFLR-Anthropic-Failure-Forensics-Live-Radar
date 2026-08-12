# AFFLR — Anthropic Failure Forensics Live Radar

This repository documents reproducible failures, regressions, unsafe generated code, and broken or misleading behavior in Anthropic's Claude products — especially Claude Code and Claude models — using public issues, measurements, system artifacts, and forensic evidence.

> **AFFLR — Anthropic Failure Forensics Live Radar**  
> A live discovery radar backed by a manually reviewed forensic case archive. **The name changed; the evidence standard did not.**

## Why this repository exists

This repository is a lightweight evidence hub. It links public upstream issues, preserves concise case summaries, records what was actually observed, and separates confirmed findings from hypotheses.

It is **not** a general collection of funny model mistakes and it is **not** an attribution-by-vibes archive. A suspicious artifact is not automatically an Anthropic-caused failure.

The operating rule is simple:

> **Evidence before attribution.**

Each case distinguishes, where applicable:

- the observed artifact or behavior;
- provenance;
- confirmed execution or occurrence;
- reproducibility or measurement;
- causal attribution;
- known limits and alternative explanations.

## Case index

| ID | Upstream issue | Case | Area | Current evidence |
|---|---|---|---|---|
| [AFF-001](cases/AFF-001-windows-wildcard-permission-resolver/README.md) | [#34866](https://github.com/anthropics/claude-code/issues/34866) | Windows wildcard / permission resolver failure | Claude Code / Windows / permissions | Public upstream report + preserved forensic evidence; HackerOne disclosure reference |
| [AFF-002](cases/AFF-002-hook-exit-code-2-collision/README.md) | [#80697](https://github.com/anthropics/claude-code/issues/80697) | Hook launch failure collides with deny exit code 2 | Claude Code / hooks | Minimal reproduction reported upstream |
| [AFF-003](cases/AFF-003-gen5-quality-regression/README.md) | [#83510](https://github.com/anthropics/claude-code/issues/83510) | Claude Gen-5 quality regression measurements | Models / quality | Reproducible benchmark measurements reported upstream |
| [AFF-004](cases/AFF-004-model-pinning-overrides/README.md) | [#83795](https://github.com/anthropics/claude-code/issues/83795) | Model pinning / resolution overrides | Claude Code / configuration / architecture | Multiple measured resolution paths reported upstream |
| [AFF-005](cases/AFF-005-epson-bx635fwd-false-success/README.md) | — | Epson BX635FWD generated repair script | Generated operational code / Windows | Artifact + provenance confirmed; false-success defects confirmed; outage causality open |

See [`cases/README.md`](cases/README.md) for the compact case format.

## AFFLR live radar

[`watchlist/candidates.md`](watchlist/candidates.md) is the automated discovery layer over public `anthropics/claude-code` issues. AFFLR checks the full issue search space hourly and exposes three objective Top-25 views: **most reacted**, **most discussed**, and **recently active**, including both open and closed issues. Changes are proposed through a review pull request rather than written directly into the case archive.

The live radar is **discovery metadata, not evidence**. Reactions, comments, labels, and activity are useful signals for deciding what to inspect next, but inclusion does not assign an AFF evidence level or establish attribution. A finding enters the case archive only after manual review under **Evidence before attribution**.

For the automated review-PR step, the repository's GitHub Actions workflow permissions must allow Actions to create pull requests. AFFLR does not require a personal access token or other third-party secret.

## Evidence levels

Cases use a deliberately small evidence ladder:

| Level | Meaning |
|---|---|
| **L0** | Hypothesis only — e.g. [VCST — VibeCoderSlopTourette hypothesis/context](https://github.com/anthropics/claude-code/issues/83510#issuecomment-5176435504) |
| **L1** | Artifact or behavior observed |
| **L2** | Relevant AI / Anthropic provenance established |
| **L3** | Execution or occurrence established |
| **L4** | Failure reproduced or quantitatively measured |
| **L5** | Causal chain established |

The level is **not a severity score**. A severe incident can still have low attribution confidence. Details: [`methodology/evidence-levels.md`](methodology/evidence-levels.md).

## Public upstream reports

The starting set includes these reports filed by `KeilerHirsch` in `anthropics/claude-code`:

- [#34866 — Windows drive-letter change / wildcard permission resolver / out-of-workspace `.claude/` creation](https://github.com/anthropics/claude-code/issues/34866)
- [#80697 — PreToolUse hook launch failure vs. exit-code 2 deny collision](https://github.com/anthropics/claude-code/issues/80697)
- [#83510 — measurable Claude generation-5 quality regression](https://github.com/anthropics/claude-code/issues/83510)
- [#83795 — model pinning silently overridden / model resolution architecture](https://github.com/anthropics/claude-code/issues/83795)

Historical private-disclosure references are recorded only at the level needed to connect the timeline. This repository does not publish private HackerOne contents, credentials, personal data, or unreleased sensitive evidence.

## Adding another finding

Maintenance is intentionally boring:

1. Copy the structure from an existing case or use the issue template.
2. Assign the next sequential `AFF-###` identifier.
3. Write only six things: **Summary, Impact, Evidence level, What is proven, What is not proven, References**.
4. Add one row to the case index.

No database, generated site, or automated case promotion is needed. AFFLR automation is deliberately limited to refreshing discovery metadata through a review PR.

## Scope and tone

The repository may contain criticism, but technical claims should remain falsifiable and source-backed. Black humor is permitted in small doses; evidence claims are not punchlines.

Corrections are welcome. If a claim is disproved, superseded, or better explained by another root cause, the case should say so explicitly.

## Support

If this archive saves you debugging time, helps reproduce a failure, or provides useful evidence, you can support the ongoing forensic hamster maintenance here:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?style=flat&logo=kofi&logoColor=white)](https://ko-fi.com/keilerhirsch)

## License

MIT. See [`LICENSE`](LICENSE).
