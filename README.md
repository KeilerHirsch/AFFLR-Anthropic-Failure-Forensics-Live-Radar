# Anthropic Failure Forensics

This repository documents reproducible failures, regressions, unsafe generated code, and broken or misleading behavior in Anthropic's Claude products — especially Claude Code and Claude models — using public issues, measurements, system artifacts, and forensic evidence.

> **Project codename: AAGOCCFS**  
> **Anthropic AI-Generated Operational Claude Code Failures & Slop**  
> Yes, the acronym is intentionally painful. It started as a joke after too many debugging sessions turned into forensic investigations. **The joke stayed; the evidence standard did not.**

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

| ID | Case | Area | Current evidence |
|---|---|---|---|
| [AFF-001](cases/AFF-001-windows-wildcard-permission-resolver/README.md) | Windows wildcard / permission resolver failure | Claude Code / Windows / permissions | Public upstream report + preserved forensic evidence; HackerOne disclosure reference |
| [AFF-002](cases/AFF-002-hook-exit-code-2-collision/README.md) | Hook launch failure collides with deny exit code 2 | Claude Code / hooks | Minimal reproduction reported upstream |
| [AFF-003](cases/AFF-003-gen5-quality-regression/README.md) | Claude Gen-5 quality regression measurements | Models / quality | Reproducible benchmark measurements reported upstream |
| [AFF-004](cases/AFF-004-model-pinning-overrides/README.md) | Model pinning / resolution overrides | Claude Code / configuration / architecture | Multiple measured resolution paths reported upstream |
| [AFF-005](cases/AFF-005-epson-bx635fwd-false-success/README.md) | Epson BX635FWD generated repair script | Generated operational code / Windows | Artifact + provenance confirmed; false-success defects confirmed; outage causality open |

See [`cases/README.md`](cases/README.md) for the compact case format.

## Evidence levels

Cases use a deliberately small evidence ladder:

| Level | Meaning |
|---|---|
| **L0** | Hypothesis only |
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

No database, dashboard, required GitHub Action, or generated site is needed.

## Scope and tone

The repository may contain criticism, but technical claims should remain falsifiable and source-backed. Black humor is permitted in small doses; evidence claims are not punchlines.

Corrections are welcome. If a claim is disproved, superseded, or better explained by another root cause, the case should say so explicitly.

## License

MIT. See [`LICENSE`](LICENSE).
