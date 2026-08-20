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
| [#88280](https://github.com/anthropics/claude-code/issues/88280) | I don't have access to the trace IDs you've provided. To generate an appropriate GitHub issue title, I need you to share:  1. The actual error message or log output 2. What command/action triggers the issue 3. Any relevant context about when it started occ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:windows |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88280](https://github.com/anthropics/claude-code/issues/88280) | I don't have access to the trace IDs you've provided. To generate an appropriate GitHub issue title, I need you to share:  1. The actual error message or log output 2. What command/action triggers the issue 3. Any relevant context about when it started occ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:windows |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78860](https://github.com/anthropics/claude-code/issues/78860) | Background Bash tasks are internally stopped during Remote Control bridge re-registration under intermittent createCodeSession 401s (v2.1.212, Linux) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:networking, area:tools, bug, has repro, platform:linux, stale |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77882](https://github.com/anthropics/claude-code/issues/77882) | Opus 4.8 fabricates user turns/approval mid-message; subagents return confident zero-tool-call hallucinated reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:agents, area:model, area:security, bug, has repro, platform:macos, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78663](https://github.com/anthropics/claude-code/issues/78663) | \[Bug\] Cyber safeguard pipeline fails end-to-end in one day: 5 FP refusals on own-code defensive review, the appeal draft itself flagged, CVP denial-by-template, and 5 auto-replies (0 humans) at usersafety@ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | api:anthropic, area:model, area:security, bug, platform:macos, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |
| [#88216](https://github.com/anthropics/claude-code/issues/88216) | Desktop: Confirm before a denied permission prompt aborts an entire multi-agent workflow | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, area:permissions, enhancement, platform:windows |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88283](https://github.com/anthropics/claude-code/issues/88283) | \[BUG\] | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | bug |
| [#88281](https://github.com/anthropics/claude-code/issues/88281) | Fenced code blocks render with no visual container and lose their list indent | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |
| [#88280](https://github.com/anthropics/claude-code/issues/88280) | I don't have access to the trace IDs you've provided. To generate an appropriate GitHub issue title, I need you to share:  1. The actual error message or log output 2. What command/action triggers the issue 3. Any relevant context about when it started occ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:windows |
| [#88279](https://github.com/anthropics/claude-code/issues/88279) | Bash tool's injected \`grep\` shadow silently drops .gitignore'd files (--ignore-files), making absence unprovable | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:bash, bug, has repro, platform:macos |
| [#88277](https://github.com/anthropics/claude-code/issues/88277) | First-class session relocation and deletion (move/delete a transcript + its sidecar state) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:cli, area:core, enhancement |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88275](https://github.com/anthropics/claude-code/issues/88275) | \[BUG\] Claude Tag: !help, !routines, !restart silently ignored — commands fall through to the session as ordinary prompts | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:integrations, bug |
| [#88274](https://github.com/anthropics/claude-code/issues/88274) | Assistant text block dropped (UI + transcript) when followed by an interleaved thinking block before a tool call | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:ide, data-loss, duplicate, has repro, platform:windows |
| [#88273](https://github.com/anthropics/claude-code/issues/88273) | \[BUG\] Claude Code desktop causes kernel panic via memory exhaustion (WindowServer watchdog timeout) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, perf:memory, platform:macos |
| [#88271](https://github.com/anthropics/claude-code/issues/88271) | False completion: agent reported repair task fully resolved while the defect was still live (8,726 records missed) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:linux |
| [#88270](https://github.com/anthropics/claude-code/issues/88270) | \[FEATURE\]  Pause-and-steer for extended thinking — and formalizing delegation as steerable reasoning | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:tui, enhancement |
| [#88269](https://github.com/anthropics/claude-code/issues/88269) | \[Bug\] SafeGuard incorrectly triggered on benign content | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:vscode, platform:windows |
| [#88268](https://github.com/anthropics/claude-code/issues/88268) | \[BUG\] /design-sync card scaffold invents viewport and rewrites labels | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:skills, bug |
| [#88267](https://github.com/anthropics/claude-code/issues/88267) | \[Bug\] Claude unable to process cybersecurity assessment data and findings consolidation | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:macos |
| [#88264](https://github.com/anthropics/claude-code/issues/88264) | \[Bug\] Anthropic API Error: Reasoning Extraction Safety Filter Triggered on Legitimate Code | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:linux |
| [#88263](https://github.com/anthropics/claude-code/issues/88263) | \[Bug\] False Positive Detection in Code Analysis | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, needs-info, platform:linux |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |
| [#88260](https://github.com/anthropics/claude-code/issues/88260) | \[Bug\] \`ScheduleWakeup\` tool called outside \`/loop\` with missing required \`prompt\` field | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, area:skills, bug, duplicate |
| [#88259](https://github.com/anthropics/claude-code/issues/88259) | \[FEATURE\] Unscoped Read of an over-cap file: return stats + outline instead of a billed first-page slice (the pre-flight half of 2.1.145's PARTIAL view) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tools, enhancement |
| [#88256](https://github.com/anthropics/claude-code/issues/88256) | statusLine command fails silently on Windows when path contains spaces (no Git Bash, quotes stripped by \`powershell -Command\`) | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-20 | 2026-08-20 | area:statusline, bug, platform:windows |
| [#88255](https://github.com/anthropics/claude-code/issues/88255) | Automatic worktree cleanup deletes directories actively in use by running sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, bug, data-loss, has repro, platform:macos |
| [#88253](https://github.com/anthropics/claude-code/issues/88253) | Desktop app: git EPERM ('Unable to read current working directory') in session worktrees since ~Aug 10 — kills menu git status/history; FDA does not fix | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, area:sandbox, bug, has repro, platform:macos |
| [#88250](https://github.com/anthropics/claude-code/issues/88250) | \[BUG\] Linux sandbox stuck on "Workspace still starting" forever on Windows 11 (Cowork/Code) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:cowork, area:sandbox, bug, external, platform:windows |
| [#88249](https://github.com/anthropics/claude-code/issues/88249) | TUI does not restore raw mode after SIGCONT — input silently dead after SIGSTOP/fg, while the TUI keeps drawing | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:linux |
| [#88247](https://github.com/anthropics/claude-code/issues/88247) | Unexpected fable safeguard activation | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:macos |
| [#88246](https://github.com/anthropics/claude-code/issues/88246) | Fable5's safety classifier abused. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:macos |

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
