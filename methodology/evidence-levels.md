# Evidence Levels

This project uses a small evidence ladder to keep **observation**, **provenance**, **execution**, **reproduction**, and **causality** separate.

| Level | Meaning | Typical evidence |
|---|---|---|
| **L0 — Hypothesis** | A plausible explanation exists, but no supporting artifact or reproducible observation has been established. | working theory, anomaly, temporal correlation |
| **L1 — Artifact observed** | A relevant artifact or behavior has been directly observed. | file, registry value, log entry, transcript, system state |
| **L2 — Provenance established** | The relevant artifact or behavior is tied to the claimed AI/vendor/product context. | generated-file provenance, session record, upstream product trace |
| **L3 — Execution established** | The relevant action actually occurred in the affected environment. | shell history, event log, process trace, timestamped mutation |
| **L4 — Failure reproduced or measured** | The failure can be reproduced under controlled conditions or quantified with a repeatable method. | minimal reproduction, benchmark, regression test, repeated measurements |
| **L5 — Causal chain established** | The observed failure is linked to the claimed cause with competing explanations materially excluded. | controlled before/after, mechanism-level reproduction, rollback/reapply proof |

## Rules

- Evidence levels are **not severity levels**.
- A case may contain sub-findings at different levels; the displayed case level should reflect the strongest claim the case actually makes.
- Closing, labeling, or triaging an upstream issue does not automatically change the evidence level.
- Vendor acknowledgment is useful evidence, but reproducibility and mechanism matter more than authority.
- If new evidence weakens a claim, reduce the level. The ladder is descriptive, not aspirational.

## Preferred claim language

Use language that matches the level:

- L0: "hypothesis", "possible", "not established"
- L1-L2: "observed", "artifact present", "provenance confirmed"
- L3: "execution confirmed"
- L4: "reproduced", "measured"
- L5: "causal chain established"

Avoid "root cause" unless the evidence supports L5 or the phrase is clearly attributed to an external source.
