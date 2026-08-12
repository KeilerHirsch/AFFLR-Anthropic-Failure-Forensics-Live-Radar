# Contributing

This repository is intentionally low-maintenance. A useful contribution is a **small, falsifiable case record**, not a large process ceremony.

## Minimum standard

A finding should answer six questions:

1. **Summary** — what happened?
2. **Impact** — why does it matter?
3. **Evidence level** — how far does the evidence actually go?
4. **What is proven** — observations, artifacts, measurements, reproductions.
5. **What is not proven** — attribution gaps, alternate explanations, untested environments.
6. **References** — upstream issues, public artifacts, hashes, datasets, documentation.

Use the evidence ladder in [`methodology/evidence-levels.md`](methodology/evidence-levels.md).

## Evidence before attribution

Do not promote correlation into causation. In particular:

- AI-generated code is not proof that the AI caused a later incident.
- An artifact on disk is not proof that it executed.
- Execution is not proof that it caused the observed failure.
- Reproduction is stronger than anecdote, but environment and version boundaries still matter.
- A vendor closing an issue does not by itself prove or disprove the technical finding.

Corrections and counter-evidence are welcome. If a better root cause appears, update the case rather than defending an obsolete theory.

## Style

Keep the technical sections professional and source-backed. Dry humor is allowed; evidence claims are not punchlines.
