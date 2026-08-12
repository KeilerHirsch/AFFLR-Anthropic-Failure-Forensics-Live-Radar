# AFF-004 — Model pinning / resolution overrides

## Summary

Claude Code was reported to ignore or override an explicit `settings.json` model pin through multiple local and server-side resolution paths. The upstream report separates four measured bypass/override vectors from a documented automatic model-fallback path.

## Impact

Model selection affects behavior, cost, reproducibility, auditability, and the stability of agentic workflows. A configuration that looks authoritative but is not authoritative can create silent operational drift.

## Evidence level

**L4 — multiple paths measured / reproduced.**

The upstream issue records configuration state, timestamps, model-menu observations, cache state, and repeated startup behavior.

## What is proven

- Public upstream issue `anthropics/claude-code#83795` was filed by `KeilerHirsch`.
- The report documents a case where `settings.json` contained a Gen-4 model pin while Claude Code loaded a Gen-5 model.
- The report records a model value in `~/.claude.json` `clientDataCacheSlots` that differed from the explicit `settings.json` value.
- The report documents that model changes and resolution paths are not generally visible to the normal tool-hook surface.
- The issue separates a documented automatic fallback mechanism from the independently measured local/configuration observations.

## What is not proven

- The case does not claim a demonstrated end-to-end prompt-injection exploit that changes models autonomously.
- It does not claim every model-resolution path has the same trigger or persistence behavior.
- Server-side behavior can change without a local client update; reproduction is date/version sensitive.
- Architectural risk is not the same thing as a demonstrated exploit.

## References

- Upstream: https://github.com/anthropics/claude-code/issues/83795
- Related measured quality case: https://github.com/anthropics/claude-code/issues/83510
- Related hook case: https://github.com/anthropics/claude-code/issues/80697
