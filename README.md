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
| [#88795](https://github.com/anthropics/claude-code/issues/88795) | Read tool ignores permissions.deny Read(/Users/\*\*) rules in managed-settings.json and user settings.json | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:permissions, area:security, bug, has repro, platform:macos |
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#77993](https://github.com/anthropics/claude-code/issues/77993) | \[FEATURE\] Make the billing identity (account/org) visible and attribute all limit messages to it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-16 | area:auth, enhancement, platform:macos, stale |
| [#77247](https://github.com/anthropics/claude-code/issues/77247) | \[BUG\] 3P LLM gateway: natively-1M models (Sonnet 5) are budgeted at 200K because the embedded/standalone CLI never resolves provider "gateway" — verified root cause + working env workaround | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-13 | area:core, area:desktop, area:providers, bug, has repro, platform:macos, stale |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#73273](https://github.com/anthropics/claude-code/issues/73273) | Remote/cloud sandbox: GitHub credential-injection proxy returns 502, blocking all git/GitHub access | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-02 | area:agents, area:networking, area:sandbox, bug, stale |
| [#81923](https://github.com/anthropics/claude-code/issues/81923) | HTTP MCP OAuth reconnect fails with "MCP endpoint not found at &lt;origin&gt;" right after successful token exchange | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81545](https://github.com/anthropics/claude-code/issues/81545) | Non-interactive login: a supported way to obtain the authorization URL programmatically | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81876](https://github.com/anthropics/claude-code/issues/81876) | \[Bug\] Cyber safeguards falsely blocking subagents on defensive security work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81830](https://github.com/anthropics/claude-code/issues/81830) | \[BUG\] Cowork/Code fail with 403 "Invalid authorization" for 10+ days — Chat works fine | OPEN | security / trust boundary | 2026-08-22 | 2026-07-28 | bug, stale |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81661](https://github.com/anthropics/claude-code/issues/81661) | MCP OAuth: unhandled TypeError "Cannot read properties of undefined (reading 'map')" when a DCR response omits grant\_types/response\_types | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81583](https://github.com/anthropics/claude-code/issues/81583) | \[Bug\] Fable 5 Safeguards Block Legitimate Workspace Admin Operations on Tool Results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81574](https://github.com/anthropics/claude-code/issues/81574) | \[BUG\] Windows: recurring forced logouts since ~Jul 22 — .credentials.json overwritten with test-fixture content ("fixture-claude-secret-value-x") | OPEN | security / trust boundary | 2026-08-22 | 2026-07-27 | stale |
| [#81571](https://github.com/anthropics/claude-code/issues/81571) | \[BUG\] Telegram channel plugin: starting a second session kills the running poller, leaving the channel permanently dead | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |
| [#81552](https://github.com/anthropics/claude-code/issues/81552) | \[Bug\] Anthropic API Error: False positive cyber policy block on defensive security audit tooling | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81521](https://github.com/anthropics/claude-code/issues/81521) | \[BUG\] Event loop busy-waits ~30s at ~1.3 cores when the embedded resolver has no usable nameservers (EPOLLERR on UDP sockets never serviced); interactive startup then hard-fails with misleading ETIMEOUT — amplifies #78529 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |
| [#79948](https://github.com/anthropics/claude-code/issues/79948) | I double-dog-dare you: build the project-management layer Claude Code is missing — because I am tired of doing it for you, and I am WORN | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-21 | stale |
| [#80358](https://github.com/anthropics/claude-code/issues/80358) | \[FEATURE\] Tool manifest — a third tool-loading mode between preload and on-demand | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-22 | enhancement, stale |
| [#88790](https://github.com/anthropics/claude-code/issues/88790) | \[FEATURE\] AskUserQuestion tool result cannot be distinguished from a genuine human response | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:agents, area:permissions, area:security, enhancement |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#77993](https://github.com/anthropics/claude-code/issues/77993) | \[FEATURE\] Make the billing identity (account/org) visible and attribute all limit messages to it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-16 | area:auth, enhancement, platform:macos, stale |
| [#77247](https://github.com/anthropics/claude-code/issues/77247) | \[BUG\] 3P LLM gateway: natively-1M models (Sonnet 5) are budgeted at 200K because the embedded/standalone CLI never resolves provider "gateway" — verified root cause + working env workaround | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-13 | area:core, area:desktop, area:providers, bug, has repro, platform:macos, stale |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#73273](https://github.com/anthropics/claude-code/issues/73273) | Remote/cloud sandbox: GitHub credential-injection proxy returns 502, blocking all git/GitHub access | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-02 | area:agents, area:networking, area:sandbox, bug, stale |
| [#81923](https://github.com/anthropics/claude-code/issues/81923) | HTTP MCP OAuth reconnect fails with "MCP endpoint not found at &lt;origin&gt;" right after successful token exchange | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81545](https://github.com/anthropics/claude-code/issues/81545) | Non-interactive login: a supported way to obtain the authorization URL programmatically | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81876](https://github.com/anthropics/claude-code/issues/81876) | \[Bug\] Cyber safeguards falsely blocking subagents on defensive security work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81661](https://github.com/anthropics/claude-code/issues/81661) | MCP OAuth: unhandled TypeError "Cannot read properties of undefined (reading 'map')" when a DCR response omits grant\_types/response\_types | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81583](https://github.com/anthropics/claude-code/issues/81583) | \[Bug\] Fable 5 Safeguards Block Legitimate Workspace Admin Operations on Tool Results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81571](https://github.com/anthropics/claude-code/issues/81571) | \[BUG\] Telegram channel plugin: starting a second session kills the running poller, leaving the channel permanently dead | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |
| [#81552](https://github.com/anthropics/claude-code/issues/81552) | \[Bug\] Anthropic API Error: False positive cyber policy block on defensive security audit tooling | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81521](https://github.com/anthropics/claude-code/issues/81521) | \[BUG\] Event loop busy-waits ~30s at ~1.3 cores when the embedded resolver has no usable nameservers (EPOLLERR on UDP sockets never serviced); interactive startup then hard-fails with misleading ETIMEOUT — amplifies #78529 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |
| [#79948](https://github.com/anthropics/claude-code/issues/79948) | I double-dog-dare you: build the project-management layer Claude Code is missing — because I am tired of doing it for you, and I am WORN | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-21 | stale |
| [#80358](https://github.com/anthropics/claude-code/issues/80358) | \[FEATURE\] Tool manifest — a third tool-loading mode between preload and on-demand | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-22 | enhancement, stale |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#81296](https://github.com/anthropics/claude-code/issues/81296) | Agent maintained ToS-violating automation for weeks, worsened the resulting bot-block, then misreported it as a login failure | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-26 | stale |
| [#81186](https://github.com/anthropics/claude-code/issues/81186) | \[BUG\] Native binary segfaults within ~2 seconds while nProtect GameGuard (Helldivers 2) is running — GameGuard module confirmed in crash stack | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88797](https://github.com/anthropics/claude-code/issues/88797) | \[Feature Request\] Add allowlist for approved security research use cases with Claude Opus models | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, enhancement, platform:macos |
| [#88796](https://github.com/anthropics/claude-code/issues/88796) | \[BUG\] Artifact mit artifact-Capability zeigt dauerhaft "Nur Lesezugriff" für den Eigentümer – Schreibvorgänge werden nicht gespeichert | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:claude-code-web, bug, platform:windows |
| [#88795](https://github.com/anthropics/claude-code/issues/88795) | Read tool ignores permissions.deny Read(/Users/\*\*) rules in managed-settings.json and user settings.json | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:permissions, area:security, bug, has repro, platform:macos |
| [#88790](https://github.com/anthropics/claude-code/issues/88790) | \[FEATURE\] AskUserQuestion tool result cannot be distinguished from a genuine human response | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:agents, area:permissions, area:security, enhancement |
| [#88786](https://github.com/anthropics/claude-code/issues/88786) | \[BUG\]   Remote Control: replies never arrive live (stuck loading), only appear after manual page reload | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:desktop, bug, has repro, platform:windows, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88785](https://github.com/anthropics/claude-code/issues/88785) | \[BUG\] node.exe consumes 45 GB, exhausts commit limit and hard-locks Windows 11 (Event ID 2004 + Kernel-Power 41) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:core, bug, has repro, perf:memory, platform:windows |
| [#88777](https://github.com/anthropics/claude-code/issues/88777) | Cross-session SendMessage reports success for messages never delivered (incl. nonexistent session names) and silently truncates at ~4.7KB | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:agents, bug, has repro, platform:windows |
| [#88773](https://github.com/anthropics/claude-code/issues/88773) | \[BUG\] Session scratchpad silently wiped by macOS reboot and recreated empty on resume — agent gets no notification | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:core, bug, has repro, platform:macos |
| [#88760](https://github.com/anthropics/claude-code/issues/88760) | \[BUG\] Claude Desktop Crash, Forced Reinstall, Which Mangled Sessions | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | invalid |
| [#88754](https://github.com/anthropics/claude-code/issues/88754) | Bash run\_in\_background tasks killed at turn boundary on MSYS2 MINGW64, and reported status does not match the process | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:bash, bug, has repro, platform:windows |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |
| [#88747](https://github.com/anthropics/claude-code/issues/88747) | Worktree creation writes an ABSOLUTE core.hooksPath into config.worktree, so worktrees run the MAIN checkout's hooks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tools, bug, has repro, platform:macos |
| [#88745](https://github.com/anthropics/claude-code/issues/88745) | Remote Control: stuck 'Thinking…' indicator with no active tool calls | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:ui, bug |
| [#88742](https://github.com/anthropics/claude-code/issues/88742) | A missed task-notification wake stalls an interactive session indefinitely | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:core, bug, has repro, platform:linux |
| [#88741](https://github.com/anthropics/claude-code/issues/88741) | SendMessage racing an agent's task stop strands the reply with no notification | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:agents, bug, has repro, platform:linux |
| [#88740](https://github.com/anthropics/claude-code/issues/88740) | Silent main-loop model fallback (Fable 5 → Opus 4.8): no notification, static identity line misleads the model, /model does not stick | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:macos |
| [#88739](https://github.com/anthropics/claude-code/issues/88739) | \[BUG\] SessionStart hook fires for sessions that never materialize (no transcript file is ever created) - side effects get attributed to a real, named session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:hooks, duplicate, has repro, platform:macos, platform:windows |
| [#88738](https://github.com/anthropics/claude-code/issues/88738) | PreToolUse hook silently stops firing mid-session and never recovers; concurrent session unaffected | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:hooks, bug, platform:vscode, platform:windows |
| [#88734](https://github.com/anthropics/claude-code/issues/88734) | \[BUG\] Persistent Monitor can survive as an orphan (parent dead, child running): the harness stops receiving its events while every liveness check still reports healthy | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, platform:windows |
| [#88732](https://github.com/anthropics/claude-code/issues/88732) | \[BUG\] /clear silently terminates persistent Monitor background tasks - the session loses its only wake mechanism and is never told | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tools, area:tui, bug, platform:windows |
| [#88712](https://github.com/anthropics/claude-code/issues/88712) | \[Bug\] Mobile push notifications not delivered despite successful server confirmation | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | bug, platform:windows |
| [#88705](https://github.com/anthropics/claude-code/issues/88705) | Sidebar session list repeatedly goes empty despite session data being intact | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:macos |
| [#88702](https://github.com/anthropics/claude-code/issues/88702) | Bash run\_in\_background ignores \`timeout\` and a never-exiting background task produces no notification | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, area:tools, bug, has repro, platform:macos |
| [#88691](https://github.com/anthropics/claude-code/issues/88691) | \[BUG\] \[Cowork\] "Record a skill": trajectory built and consumed by renderer, but the task session receives no demonstration — no proposal generated, capture never persisted to disk | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, area:skills, bug, data-loss, platform:macos |
| [#88689](https://github.com/anthropics/claude-code/issues/88689) | \[BUG\] Windows MSIX: Repair and Reset can never succeed — the installer registers the package from \`%TEMP%\\Claude-\*.msix\`, which is later deleted (0x80073CF0 / 0x80070002) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, duplicate, platform:windows |

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
