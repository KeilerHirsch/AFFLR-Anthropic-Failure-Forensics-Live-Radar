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
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#78457](https://github.com/anthropics/claude-code/issues/78457) | Fable 5 dual-use safeguard routes legitimate defensive security work off the model (false positive) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#78022](https://github.com/anthropics/claude-code/issues/78022) | \[Bug\] Anthropic API Safety Filter: Unauthorized Model Substitution Without User Consent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, duplicate, platform:linux, stale |
| [#77745](https://github.com/anthropics/claude-code/issues/77745) | Agent asserted unverified causal explanations as fact and wrote them into permanent project records (5+ times in one session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, model, platform:windows, stale |
| [#77699](https://github.com/anthropics/claude-code/issues/77699) | False-positive safeguard flag interrupted legitimate work; /feedback unavailable in Cursor harness | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, area:security, duplicate, stale |
| [#77218](https://github.com/anthropics/claude-code/issues/77218) | \[MODEL\] False-positive "cyber" refusals on routine container/Kubernetes templating work (9-refusal cluster, claude-fable-5) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | api:anthropic, area:model, bug, model, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#77707](https://github.com/anthropics/claude-code/issues/77707) | Third-party plugin (Codex Companion) silently made unauthorized Anthropic API calls using inherited ANTHROPIC\_API\_KEY | OPEN | security / trust boundary | 2026-08-20 | 2026-07-15 | area:hooks, area:plugins, area:security, bug, platform:macos, stale |
| [#78372](https://github.com/anthropics/claude-code/issues/78372) | Auto-mode safety classifier routes through ANTHROPIC\_BASE\_URL (undocumented) — gateway users' classifier is served by their gateway | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, area:security, bug, stale |
| [#78344](https://github.com/anthropics/claude-code/issues/78344) | Auto-mode permission classifier blocks every path to handle a user-provided token — 5 denials, one task, zero safety gained | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, bug, stale |
| [#75859](https://github.com/anthropics/claude-code/issues/75859) | Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-08 | area:bash, area:sandbox, bug, data-loss, high-priority, platform:linux, stale |
| [#77996](https://github.com/anthropics/claude-code/issues/77996) | \[FEATURE\] Hook event for permission-prompt outcomes (and document PermissionRequest/Notification input schemas) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-16 | area:hooks, area:permissions, duplicate, enhancement, stale |
| [#77463](https://github.com/anthropics/claude-code/issues/77463) | Session instances are invisible to the user — the "kids in a trenchcoat" problem (fork/resume divergence across a fleet of surfaces, conflicting stale writes, premium-rate token burn, no instance identity anywhere) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-14 | area:core, bug, stale |
| [#77254](https://github.com/anthropics/claude-code/issues/77254) | \[BUG\] Auto-mode classifier: false positive on an org-distributed skill's sanctioned command, with no org-level channel to vouch for it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-13 | area:permissions, area:skills, bug, platform:macos, stale |
| [#76908](https://github.com/anthropics/claude-code/issues/76908) | \[MODEL\] Fable5 - Silent downgrade to Opus | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:agents, bug, model, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#78457](https://github.com/anthropics/claude-code/issues/78457) | Fable 5 dual-use safeguard routes legitimate defensive security work off the model (false positive) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#78022](https://github.com/anthropics/claude-code/issues/78022) | \[Bug\] Anthropic API Safety Filter: Unauthorized Model Substitution Without User Consent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, duplicate, platform:linux, stale |
| [#77745](https://github.com/anthropics/claude-code/issues/77745) | Agent asserted unverified causal explanations as fact and wrote them into permanent project records (5+ times in one session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, model, platform:windows, stale |
| [#77699](https://github.com/anthropics/claude-code/issues/77699) | False-positive safeguard flag interrupted legitimate work; /feedback unavailable in Cursor harness | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, area:security, duplicate, stale |
| [#77218](https://github.com/anthropics/claude-code/issues/77218) | \[MODEL\] False-positive "cyber" refusals on routine container/Kubernetes templating work (9-refusal cluster, claude-fable-5) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | api:anthropic, area:model, bug, model, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#78372](https://github.com/anthropics/claude-code/issues/78372) | Auto-mode safety classifier routes through ANTHROPIC\_BASE\_URL (undocumented) — gateway users' classifier is served by their gateway | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, area:security, bug, stale |
| [#78344](https://github.com/anthropics/claude-code/issues/78344) | Auto-mode permission classifier blocks every path to handle a user-provided token — 5 denials, one task, zero safety gained | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-17 | area:permissions, bug, stale |
| [#75859](https://github.com/anthropics/claude-code/issues/75859) | Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-08 | area:bash, area:sandbox, bug, data-loss, high-priority, platform:linux, stale |
| [#77996](https://github.com/anthropics/claude-code/issues/77996) | \[FEATURE\] Hook event for permission-prompt outcomes (and document PermissionRequest/Notification input schemas) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-16 | area:hooks, area:permissions, duplicate, enhancement, stale |
| [#77463](https://github.com/anthropics/claude-code/issues/77463) | Session instances are invisible to the user — the "kids in a trenchcoat" problem (fork/resume divergence across a fleet of surfaces, conflicting stale writes, premium-rate token burn, no instance identity anywhere) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-14 | area:core, bug, stale |
| [#77254](https://github.com/anthropics/claude-code/issues/77254) | \[BUG\] Auto-mode classifier: false positive on an org-distributed skill's sanctioned command, with no org-level channel to vouch for it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-13 | area:permissions, area:skills, bug, platform:macos, stale |
| [#76908](https://github.com/anthropics/claude-code/issues/76908) | \[MODEL\] Fable5 - Silent downgrade to Opus | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:agents, bug, model, stale |
| [#76823](https://github.com/anthropics/claude-code/issues/76823) | Tool-result stream injection: fabricated git output attempted to induce destructive git reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-12 | area:bash, area:security, bug, platform:windows, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88206](https://github.com/anthropics/claude-code/issues/88206) | \[Bug\] AskUserQuestion picker with previews unresponsive to keyboard input in auto mode | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |
| [#88205](https://github.com/anthropics/claude-code/issues/88205) | ScheduleWakeup rejects noop:true calls made outside /loop with "prompt is required when stop is not true" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, area:skills, bug |
| [#88203](https://github.com/anthropics/claude-code/issues/88203) | PreToolUse hook + background subagent: tools in the notification-woken turn are cancelled as "user doesn't want to take this action" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-sdk, area:agents, area:core, area:hooks, bug, has repro, platform:macos |
| [#88202](https://github.com/anthropics/claude-code/issues/88202) | \[Bug\] False Positive Detection Issue | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, needs-info, platform:macos |
| [#88201](https://github.com/anthropics/claude-code/issues/88201) | \[Bug\] Anthropic API Error: Fable 5 safeguards falsely flagging safe messages | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, duplicate, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88200](https://github.com/anthropics/claude-code/issues/88200) | \[Bug\] Ultrareview free quota consumed on failed run without refund | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:cost, area:skills, bug, platform:linux |
| [#88185](https://github.com/anthropics/claude-code/issues/88185) | Claude Desktop: unexpected re-authentication when switching between Chat and Code tabs | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:auth, area:desktop, bug, platform:linux |
| [#88172](https://github.com/anthropics/claude-code/issues/88172) | MCP connector serves a stale tools/list after a server adds tools — only an app relaunch refreshes it (a new conversation and re-issued server/discover do not) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:mcp, bug, platform:macos |
| [#88170](https://github.com/anthropics/claude-code/issues/88170) | \[BUG\] Marketplace-entry dependencies: version constraints silently ignored, prune deletes live dependencies | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:plugins, bug, has repro, platform:macos |
| [#88168](https://github.com/anthropics/claude-code/issues/88168) | Desktop app: chat scrollback permanently truncated at a fixed mid-conversation point after app restart (session JSONL intact) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos |
| [#88158](https://github.com/anthropics/claude-code/issues/88158) | \[Bug\] MCP update\_document patch mode silently drops content after checkbox lists | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, data-loss, has repro, platform:windows |
| [#88138](https://github.com/anthropics/claude-code/issues/88138) | \[BUG\] Claude Desktop (Windows MSIX) transitions from Ok to Modified, NeedsRemediation on first launch, with no deployment event in any Windows log | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:cowork, area:desktop, bug, platform:windows |
| [#88122](https://github.com/anthropics/claude-code/issues/88122) | Model fabricated a user message and executed it: unrequested git commit, push, and issue edit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:model, area:security, bug, platform:macos |
| [#87991](https://github.com/anthropics/claude-code/issues/87991) | OTEL\_RESOURCE\_ATTRIBUTES set via settings.json env or OS-level env var never applied to Claude Code's own OTLP export | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:core, bug, has repro, platform:windows |
| [#87796](https://github.com/anthropics/claude-code/issues/87796) | Published artifacts deleted server-side without user action on a personal account (no delete UI exists; links were already shared) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-19 | area:claude-code-web, bug, data-loss |
| [#87710](https://github.com/anthropics/claude-code/issues/87710) | Fresh install: desktop app sidebar shows no session history despite intact ~/.claude/projects data | OPEN | security / trust boundary | 2026-08-20 | 2026-08-18 | area:desktop, bug, platform:windows |
| [#87684](https://github.com/anthropics/claude-code/issues/87684) | Desktop app: clipboard-change warning toast has no off switch — constant false positives with dictation apps (Wispr Flow) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-18 | area:desktop, enhancement, platform:macos |
| [#87294](https://github.com/anthropics/claude-code/issues/87294) | \[FEATURE\] On-demand screen sharing in voice mode on iOS | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-20 | 2026-08-17 | invalid |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#87086](https://github.com/anthropics/claude-code/issues/87086) | \[EVAL/TRANSPARENCY\] Anthropic's regulation case rests on internal evals — apply the #86979 provenance standard to Glasswing and 'When AI Builds Itself' | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-16 | invalid |
| [#87055](https://github.com/anthropics/claude-code/issues/87055) | \[BUG\] Background Bash task's process group is SIGKILLed mid-run when the command spawns a daemonizing CLI (cursor-agent) — and reported as completed (exit code 0) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:bash, bug, has repro, platform:macos |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86604](https://github.com/anthropics/claude-code/issues/86604) | PR-activity webhook events render as if the user sent them, and non-actionable bot comment-edits are relayed with full raw payloads | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:claude-code-web, area:ui, bug, platform:web |
| [#86498](https://github.com/anthropics/claude-code/issues/86498) | MCP-originated cross-session sends (\`ccd\_session\_mgmt send\_message\`) never deliver — payload lost in app layer; receiving session UI hangs on "phantom" turn | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-13 | area:desktop, area:mcp, bug, duplicate, has repro, platform:windows, regression |
| [#86311](https://github.com/anthropics/claude-code/issues/86311) | \[Bug\] Subagent experiencing high error rate - communication betweet session | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-20 | 2026-08-13 | area:agents, bug, needs-info, needs-repro, platform:macos |

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
