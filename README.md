# AFFLR — Anthropic Failure Forensics Live Radar

AFFLR watches the public [`anthropics/claude-code`](https://github.com/anthropics/claude-code/issues) issue space and prioritizes security/trust-boundary, evidence/provenance/integrity, and fresh critical signals for human review. Popularity and discussion remain secondary discovery metadata.

> **Automation for productive laziness.** The radar does the repetitive watching; humans still decide what the evidence means.

## 🛰️ Live radar status

**⏱ Next automatic trigger:** every hour at **`:17 UTC`**  
**🔁 Schedule:** hourly  
**▶️ Manual trigger:** available in [GitHub Actions](../../actions/workflows/afflr.yml)  
**📡 Full radar output:** [`watchlist/candidates.md`](watchlist/candidates.md)

The **Top 5** of each view are visible directly below. Positions 6–25 stay one click away in the expandable sections.

<!-- AFFLR-RADAR:START -->
> Automated discovery metadata from public `anthropics/claude-code` issues. Primary ranking is **discovery-only** — not an AFF evidence level, vulnerability rating, or causal attribution.

The live README prioritizes security/trust-boundary and provenance/integrity signals from both recent activity and targeted search pools. Popularity views remain in [`watchlist/candidates.md`](watchlist/candidates.md) as secondary discovery metadata.

### 🛡️ Security & trust-boundary signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#78457](https://github.com/anthropics/claude-code/issues/78457) | Fable 5 dual-use safeguard routes legitimate defensive security work off the model (false positive) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#78022](https://github.com/anthropics/claude-code/issues/78022) | \[Bug\] Anthropic API Safety Filter: Unauthorized Model Substitution Without User Consent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, duplicate, platform:linux, stale |
| [#77745](https://github.com/anthropics/claude-code/issues/77745) | Agent asserted unverified causal explanations as fact and wrote them into permanent project records (5+ times in one session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |
| [#77707](https://github.com/anthropics/claude-code/issues/77707) | Third-party plugin (Codex Companion) silently made unauthorized Anthropic API calls using inherited ANTHROPIC\_API\_KEY | OPEN | security / trust boundary | 2026-08-20 | 2026-07-15 | area:hooks, area:plugins, area:security, bug, platform:macos, stale |
| [#78372](https://github.com/anthropics/claude-code/issues/78372) | Auto-mode safety classifier routes through ANTHROPIC\_BASE\_URL (undocumented) — gateway users' classifier is served by their gateway | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, area:security, bug, stale |
| [#78344](https://github.com/anthropics/claude-code/issues/78344) | Auto-mode permission classifier blocks every path to handle a user-provided token — 5 denials, one task, zero safety gained | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, bug, stale |
| [#75859](https://github.com/anthropics/claude-code/issues/75859) | Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-08 | area:bash, area:sandbox, bug, data-loss, high-priority, platform:linux, stale |
| [#77996](https://github.com/anthropics/claude-code/issues/77996) | \[FEATURE\] Hook event for permission-prompt outcomes (and document PermissionRequest/Notification input schemas) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-16 | area:hooks, area:permissions, duplicate, enhancement, stale |
| [#77463](https://github.com/anthropics/claude-code/issues/77463) | Session instances are invisible to the user — the "kids in a trenchcoat" problem (fork/resume divergence across a fleet of surfaces, conflicting stale writes, premium-rate token burn, no instance identity anywhere) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-14 | area:core, bug, stale |
| [#76908](https://github.com/anthropics/claude-code/issues/76908) | \[MODEL\] Fable5 - Silent downgrade to Opus | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:agents, bug, model, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#78457](https://github.com/anthropics/claude-code/issues/78457) | Fable 5 dual-use safeguard routes legitimate defensive security work off the model (false positive) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#78022](https://github.com/anthropics/claude-code/issues/78022) | \[Bug\] Anthropic API Safety Filter: Unauthorized Model Substitution Without User Consent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, duplicate, platform:linux, stale |
| [#77745](https://github.com/anthropics/claude-code/issues/77745) | Agent asserted unverified causal explanations as fact and wrote them into permanent project records (5+ times in one session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |
| [#78372](https://github.com/anthropics/claude-code/issues/78372) | Auto-mode safety classifier routes through ANTHROPIC\_BASE\_URL (undocumented) — gateway users' classifier is served by their gateway | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, area:security, bug, stale |
| [#78344](https://github.com/anthropics/claude-code/issues/78344) | Auto-mode permission classifier blocks every path to handle a user-provided token — 5 denials, one task, zero safety gained | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, bug, stale |
| [#75859](https://github.com/anthropics/claude-code/issues/75859) | Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-08 | area:bash, area:sandbox, bug, data-loss, high-priority, platform:linux, stale |
| [#77996](https://github.com/anthropics/claude-code/issues/77996) | \[FEATURE\] Hook event for permission-prompt outcomes (and document PermissionRequest/Notification input schemas) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-16 | area:hooks, area:permissions, duplicate, enhancement, stale |
| [#77463](https://github.com/anthropics/claude-code/issues/77463) | Session instances are invisible to the user — the "kids in a trenchcoat" problem (fork/resume divergence across a fleet of surfaces, conflicting stale writes, premium-rate token burn, no instance identity anywhere) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-14 | area:core, bug, stale |
| [#76908](https://github.com/anthropics/claude-code/issues/76908) | \[MODEL\] Fable5 - Silent downgrade to Opus | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:agents, bug, model, stale |
| [#76823](https://github.com/anthropics/claude-code/issues/76823) | Tool-result stream injection: fabricated git output attempted to induce destructive git reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:bash, area:security, bug, platform:windows, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88238](https://github.com/anthropics/claude-code/issues/88238) | \[FEATURE\] subagentStatusLine: separate agent name from launch provenance in the tasks\[\] payload | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:statusline, enhancement |
| [#88237](https://github.com/anthropics/claude-code/issues/88237) | Claude-in-Chrome extension not connecting from cloud/Cowork session despite extension active locally | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:chrome, area:cowork, bug |
| [#88236](https://github.com/anthropics/claude-code/issues/88236) | \[FEATURE\] Desktop app: persist the chosen transcript view (thinking) as the default for new sessions | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, enhancement, platform:linux |
| [#88235](https://github.com/anthropics/claude-code/issues/88235) | \[BUG\] Claude Desktop arm64 fails to launch on Snapdragon X2 Elite — GPU process crashes (exitCode 101457950) | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | invalid |
| [#88234](https://github.com/anthropics/claude-code/issues/88234) | Claude Desktop local agent silently downloads an 8.5 GB iOS Simulator runtime and leaves system-wide devices and caches without storage confirmation | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:permissions, area:tools, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88233](https://github.com/anthropics/claude-code/issues/88233) | Remote Control denial after \`--resume\` silently disables cross-machine discovery and messaging | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:cli, bug, has repro, platform:macos |
| [#88232](https://github.com/anthropics/claude-code/issues/88232) | Claude in Chrome extension fails to connect to Cowork session ("Browser extension is not connected") | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:browser-extension, area:cowork, duplicate, platform:windows |
| [#88231](https://github.com/anthropics/claude-code/issues/88231) | Cross-session send\_message: delivered:true returned for cold targets, then the message is silently dropped (regression, CLI 2.1.222 → 2.1.227/2.1.229) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, bug, has repro, platform:macos, regression |
| [#88230](https://github.com/anthropics/claude-code/issues/88230) | /code-review (high) stalls before final report on Fable model — waits forever for its last review angle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:model, area:skills, bug, platform:macos |
| [#88229](https://github.com/anthropics/claude-code/issues/88229) | \[BUG\] Claude Desktop (Windows): downloads fail silently for all extensions in Chromium's ALLOW\_ON\_USER\_GESTURE list (.py/.js/.rb/.sh/.ps1/.bat/.pyw) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | invalid |
| [#88227](https://github.com/anthropics/claude-code/issues/88227) | \[Bug\] Profile bio field incorrectly triggers safety filters | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:windows |
| [#88226](https://github.com/anthropics/claude-code/issues/88226) | \[Feature Request\] Add security research exemption or override for safety blocks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, enhancement, platform:linux |
| [#88224](https://github.com/anthropics/claude-code/issues/88224) | \[FEATURE\] Manually sort session list | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:ui, enhancement |
| [#88222](https://github.com/anthropics/claude-code/issues/88222) | Claude overuses the word "arm" | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug |
| [#88221](https://github.com/anthropics/claude-code/issues/88221) | CLAUDE\_AX\_SCREEN\_READER=1 set correctly but screen reader mode doesn't activate (v2.1.237) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:a11y, area:tui, bug, has repro, platform:linux |
| [#88220](https://github.com/anthropics/claude-code/issues/88220) | Session deleted and lost during interaction\[BUG\] | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, bug, needs-repro, platform:windows |
| [#88219](https://github.com/anthropics/claude-code/issues/88219) | \[Bug\] Anthropic API Error: Repeated failures during plan updates | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, duplicate, platform:linux |
| [#88218](https://github.com/anthropics/claude-code/issues/88218) | Session history split across two project-slug folders for the same cwd (ñ normalization / space+case handling) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:core, bug, has repro, platform:macos |
| [#88217](https://github.com/anthropics/claude-code/issues/88217) | iOS Simulator MCP/panel: attach reports a device it does not route actions to — taps land on the wrong simulator, and shut-down or deleted devices are reported as attached | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, area:mcp, bug, has repro, platform:macos |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |
| [#88215](https://github.com/anthropics/claude-code/issues/88215) | \[Bug\] Anthropic API Error: Reasoning Extraction False Positives in Extended Sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:windows |
| [#88214](https://github.com/anthropics/claude-code/issues/88214) | Cloud sessions never install plugins declared in .claude/settings.json, and /plugin is unavailable to fix it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:claude-code-web, area:plugins, bug, has repro, platform:web |
| [#88213](https://github.com/anthropics/claude-code/issues/88213) | \[BUG\] Persistent bottom-right notifications ("Update installed · Restart to update") replace the context meter instead of coexisting with it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:tui, area:ui, bug |
| [#88212](https://github.com/anthropics/claude-code/issues/88212) | \[Bug\] Anthropic API Error: Safeguard triggered on non-harmful content | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug |
| [#88211](https://github.com/anthropics/claude-code/issues/88211) | \[BUG\] Default totalTokensReminder (padded-countdown) shows a number unrelated to context usage — model told the user "plenty left" moments before dying at the 1M context limit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, bug, has repro |

</details>
<!-- AFFLR-RADAR:END -->

Open and closed issues are included. The radar records useful public metadata such as the issue link, author, state, reactions, comments, timestamps, and labels.

## How it works

```text
public Claude Code issues
        ↓
hourly scan
        ↓
objective GitHub metadata
        ↓
README + full watchlist refresh
        ↓
human evidence review
```

The radar is discovery infrastructure, not an automatic truth machine.

## What AFFLR does not do

- No AI-generated importance score.
- No automatic root-cause claims.
- No automatic forensic conclusions.
- No rewriting reviewed findings just because an issue is popular.

> **Evidence before attribution.**

## Support

If AFFLR saves you debugging time or helps you spot something worth investigating, you can support the forensic hamster maintenance here:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?style=flat&logo=kofi&logoColor=white)](https://ko-fi.com/keilerhirsch)

## License

MIT. See [`LICENSE`](LICENSE).
