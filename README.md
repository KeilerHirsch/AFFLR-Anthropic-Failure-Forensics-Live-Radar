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
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#78364](https://github.com/anthropics/claude-code/issues/78364) | Remote Control silently self-disables after 3 transient failures and never recovers (per-session init latch + persisted OAuth dead-token backoff) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:networking, bug, has repro, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |
| [#75859](https://github.com/anthropics/claude-code/issues/75859) | Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-08 | area:bash, area:sandbox, bug, data-loss, high-priority, platform:linux, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88267](https://github.com/anthropics/claude-code/issues/88267) | \[Bug\] Claude unable to process cybersecurity assessment data and findings consolidation | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:macos |
| [#88264](https://github.com/anthropics/claude-code/issues/88264) | \[Bug\] Anthropic API Error: Reasoning Extraction Safety Filter Triggered on Legitimate Code | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:linux |
| [#88263](https://github.com/anthropics/claude-code/issues/88263) | \[Bug\] False Positive Detection in Code Analysis | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, needs-info, platform:linux |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |
| [#88260](https://github.com/anthropics/claude-code/issues/88260) | \[Bug\] \`ScheduleWakeup\` tool called outside \`/loop\` with missing required \`prompt\` field | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, area:skills, bug, duplicate |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88259](https://github.com/anthropics/claude-code/issues/88259) | \[FEATURE\] Unscoped Read of an over-cap file: return stats + outline instead of a billed first-page slice (the pre-flight half of 2.1.145's PARTIAL view) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tools, enhancement |
| [#88258](https://github.com/anthropics/claude-code/issues/88258) | /mo\[Bug\] Consecutive API failures with Claude Opus and Claude 3.5 Sonnet models | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:api, area:model, bug, needs-repro, platform:windows |
| [#88255](https://github.com/anthropics/claude-code/issues/88255) | Automatic worktree cleanup deletes directories actively in use by running sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, bug, data-loss, has repro, platform:macos |
| [#88253](https://github.com/anthropics/claude-code/issues/88253) | Desktop app: git EPERM ('Unable to read current working directory') in session worktrees since ~Aug 10 — kills menu git status/history; FDA does not fix | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, area:sandbox, bug, has repro, platform:macos |
| [#88252](https://github.com/anthropics/claude-code/issues/88252) | Desktop app (CCD): inter-session messages delivered but never processed — wake deferred ~8h, dies offline, never retried | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos |
| [#88250](https://github.com/anthropics/claude-code/issues/88250) | \[BUG\] Linux sandbox stuck on "Workspace still starting" forever on Windows 11 (Cowork/Code) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:cowork, area:sandbox, bug, external, platform:windows |
| [#88249](https://github.com/anthropics/claude-code/issues/88249) | TUI does not restore raw mode after SIGCONT — input silently dead after SIGSTOP/fg, while the TUI keeps drawing | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:linux |
| [#88247](https://github.com/anthropics/claude-code/issues/88247) | Unexpected fable safeguard activation | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:macos |
| [#88246](https://github.com/anthropics/claude-code/issues/88246) | Fable5's safety classifier abused. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:macos |
| [#88245](https://github.com/anthropics/claude-code/issues/88245) | \[BUG\] Routines (CCR) の定期実行がセッション初期化直後で毎回停止する | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:routines, bug, platform:web |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#88242](https://github.com/anthropics/claude-code/issues/88242) | \[Bug\] Claude Code misclassifies legitimate API health check scripts as credential abuse | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:windows |
| [#88241](https://github.com/anthropics/claude-code/issues/88241) | \[Bug\] False positive security detection for API health check scripts with rate limit monitoring | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, platform:windows |
| [#88239](https://github.com/anthropics/claude-code/issues/88239) | Background session cannot be deleted after a squash merge: "worktree is not clean" on a clean worktree | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:agent-view, duplicate, platform:wsl |
| [#88238](https://github.com/anthropics/claude-code/issues/88238) | \[FEATURE\] subagentStatusLine: separate agent name from launch provenance in the tasks\[\] payload | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:statusline, enhancement |
| [#88234](https://github.com/anthropics/claude-code/issues/88234) | Claude Desktop local agent silently downloads an 8.5 GB iOS Simulator runtime and leaves system-wide devices and caches without storage confirmation | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:permissions, area:tools, bug, has repro, platform:macos |
| [#88233](https://github.com/anthropics/claude-code/issues/88233) | Remote Control denial after \`--resume\` silently disables cross-machine discovery and messaging | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:cli, bug, has repro, platform:macos |
| [#88231](https://github.com/anthropics/claude-code/issues/88231) | Cross-session send\_message: delivered:true returned for cold targets, then the message is silently dropped (regression, CLI 2.1.222 → 2.1.227/2.1.229) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, bug, has repro, platform:macos, regression |
| [#88230](https://github.com/anthropics/claude-code/issues/88230) | /code-review (high) stalls before final report on Fable model — waits forever for its last review angle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:model, area:skills, bug, platform:macos |
| [#88226](https://github.com/anthropics/claude-code/issues/88226) | \[Feature Request\] Add security research exemption or override for safety blocks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, enhancement, platform:linux |

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
