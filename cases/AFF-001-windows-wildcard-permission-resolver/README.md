# AFF-001 — Windows wildcard / permission resolver failure

## Summary

A Windows drive-letter change was reported to break command-specific wildcard permission matching in Claude Code, causing permission accumulation in `settings.local.json` and out-of-workspace `.claude/` directory creation. The public report includes reproduction steps and preserved forensic artifacts.

A related private disclosure was filed as **HackerOne #3609218**. This case records that identifier only; it does not republish private HackerOne contents.

## Impact

Permission-state growth, unexpected filesystem writes, broken workspace assumptions, and a costly recovery/debugging cycle on Windows.

## Evidence level

**L4 — failure reproduced / measured.**

The public upstream issue contains a reproduction path and concrete artifact measurements. This case does not independently elevate every security interpretation in the original report to L5 causality.

## What is proven

- Public upstream issue `anthropics/claude-code#34866` was filed by `KeilerHirsch` on 2026-03-16.
- The issue documents a Windows drive-letter-change reproduction scenario.
- The report records `settings.local.json` growth from roughly 1.1 KB to substantially larger corrupted states, including a 25.2 KB preserved artifact.
- The report records unexpected `.claude/` material outside the intended workspace and states that five corrupted configuration files were preserved.
- Anthropic's tracker labeled the report `bug`, `has repro`, `platform:windows`, `area:security`, and `area:permissions` before it was later closed `not_planned`.
- Historical private-disclosure tracking references HackerOne report `#3609218`.

## What is not proven

- This case does not claim that every out-of-workspace write mechanism described in the original issue is independently re-demonstrated here.
- Tracker closure does not establish that the technical behavior was fixed, invalid, or harmless.
- Private HackerOne contents are not public evidence in this repository.
- Broader claims about sandbox architecture should be evaluated against the exact Claude Code version and current implementation.

## References

- Upstream: https://github.com/anthropics/claude-code/issues/34866
- Historical disclosure reference: HackerOne `#3609218` (private disclosure metadata only)
- Related upstream references are preserved in the original issue body.
