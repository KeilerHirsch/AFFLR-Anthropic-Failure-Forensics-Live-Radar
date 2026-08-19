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
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#72862](https://github.com/anthropics/claude-code/issues/72862) | \[BUG\] macOS: Desktop app spawns headless sessions that mint new hashed keychain items, causing endless "security wants to access Claude Code-credentials" prompts | CLOSED / NOT\_PLANNED | security / trust boundary · high-signal label | 2026-08-19 | 2026-07-01 | area:auth, area:desktop, bug, has repro, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#74016](https://github.com/anthropics/claude-code/issues/74016) | Background daemon posts spurious "needs re-authentication" notification when a proactive OAuth refresh fails during macOS sleep/PowerNap dark-wake (transient, self-heals, auth never actually invalid) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-03 | area:auth, bug, has repro, platform:macos, stale |
| [#75676](https://github.com/anthropics/claude-code/issues/75676) | \[Bug\] Anthropic API Error: False positive cybersecurity content flag on legitimate local development diagnostics | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, bug, platform:macos, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#87825](https://github.com/anthropics/claude-code/issues/87825) | Persistent memory rules are decorative — Claude ignores them before destructive actions, repeatedly, across sessions | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, memory, platform:macos |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87838](https://github.com/anthropics/claude-code/issues/87838) | claude mcp get/list print configured MCP secrets (headers, env vars) in cleartext with no masking | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:mcp, area:security, enhancement |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#72808](https://github.com/anthropics/claude-code/issues/72808) | \[BUG\] headersHelper never executed for HTTP managedMcpServers (Claude Desktop, macOS) — static headers work, helper script silently ignored | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-19 | 2026-07-01 | api:bedrock, area:desktop, area:mcp, bug, platform:macos, stale |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#76293](https://github.com/anthropics/claude-code/issues/76293) | \[BUG\] Interactive CLI silently exits after successful Bash tool result; session resumes normally | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-10 | area:core, area:tui, bug, platform:macos, stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#74016](https://github.com/anthropics/claude-code/issues/74016) | Background daemon posts spurious "needs re-authentication" notification when a proactive OAuth refresh fails during macOS sleep/PowerNap dark-wake (transient, self-heals, auth never actually invalid) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-03 | area:auth, bug, has repro, platform:macos, stale |
| [#75676](https://github.com/anthropics/claude-code/issues/75676) | \[Bug\] Anthropic API Error: False positive cybersecurity content flag on legitimate local development diagnostics | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, bug, platform:macos, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#76293](https://github.com/anthropics/claude-code/issues/76293) | \[BUG\] Interactive CLI silently exits after successful Bash tool result; session resumes normally | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-10 | area:core, area:tui, bug, platform:macos, stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87949](https://github.com/anthropics/claude-code/issues/87949) | \[Bug\] Anthropic API Error: Overly Aggressive Content Filtering on Legitimate Cybersecurity Development Work | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, duplicate, external, platform:macos |
| [#87948](https://github.com/anthropics/claude-code/issues/87948) | \[BUG\] run\_in\_background tasks intermittently killed ~17-20s after start, seconds after the arming turn ends (terminal CLI, Linux — not idle-timeout timing) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:core, bug, has repro, platform:linux |
| [#87947](https://github.com/anthropics/claude-code/issues/87947) | Print/SDK mode persists empty thinking blocks in session transcript (signature only) — interactive mode persists full text | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:windows |
| [#87946](https://github.com/anthropics/claude-code/issues/87946) | \[BUG\] thinking summary language | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:api, area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87945](https://github.com/anthropics/claude-code/issues/87945) | Browser tool navigate consistently fails with "denied or failed" for previously-working sites | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:mcp, bug, platform:windows |
| [#87943](https://github.com/anthropics/claude-code/issues/87943) | \[BUG\] VS Code panel: sequential edits to one file diff each proposal against a stale snapshot (diff-editor tab only) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:vscode, bug, has repro, platform:linux, platform:vscode |
| [#87942](https://github.com/anthropics/claude-code/issues/87942) | Personal Pro subscription blocked in Claude Code — "organization has disabled subscription access" (auto-generated personal org) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, duplicate, platform:windows |
| [#87941](https://github.com/anthropics/claude-code/issues/87941) | \[Bug\] Anthropic API Error: Sonnet 5 Safeguards Flagging Verified Cyber Users | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:windows |
| [#87940](https://github.com/anthropics/claude-code/issues/87940) | Scheduled/desktop tasks stop firing once a manual session is active | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:routines, bug, platform:windows |
| [#87939](https://github.com/anthropics/claude-code/issues/87939) | Browser-pane dev-server launcher fails with EPERM (uv\_cwd) -- sandboxed subprocess can't load an ad-hoc-signed native binary (Vite 8/Rolldown) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, bug, has repro, platform:macos |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87937](https://github.com/anthropics/claude-code/issues/87937) | Auto-compact summarization prompt leaks into the compacted history as a fabricated "text-only, no tools" user override | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-sdk, area:core, bug, has repro, platform:macos |
| [#87936](https://github.com/anthropics/claude-code/issues/87936) | \[FEATURE\] Should look for git.path in Vscode user settings | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:ide, enhancement, platform:vscode |
| [#87935](https://github.com/anthropics/claude-code/issues/87935) | Sandboxed Bash wedges permanently when the working directory is on a read-only filesystem (no cwd recovery) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:sandbox, bug, has repro, platform:linux, reproduced |
| [#87934](https://github.com/anthropics/claude-code/issues/87934) | Cloud/remote session token usage not included in "Total tokens" stat on the Overview dashboard | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:claude-code-web, bug |
| [#87933](https://github.com/anthropics/claude-code/issues/87933) | \[Feature Request\] Mid-turn user message delivery with interrupt capability | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:tui, enhancement, platform:linux |
| [#87932](https://github.com/anthropics/claude-code/issues/87932) | Gate keybinding contexts on vim mode (NORMAL/INSERT) so scroll and line-editing keys can share a keystroke | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:tui, enhancement, keybindings, platform:macos |
| [#87931](https://github.com/anthropics/claude-code/issues/87931) | \[Feature Request\] Add "Ask about it" option to permission prompts for clarification without rejection | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:tui, enhancement, platform:linux |
| [#87930](https://github.com/anthropics/claude-code/issues/87930) | \[BUG\]  Regression in 2.1.228: streaming to a Bedrock gateway returns zero events, client silently falls back to non-streaming, throughput halves | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:api, bug, has repro, platform:windows, regression |
| [#87929](https://github.com/anthropics/claude-code/issues/87929) | \[BUG\] Claude in Chrome: tab viewport silently collapses to 280x15 and never recovers; screenshot/left\_click/resize\_window all keep reporting success | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:chrome, area:cowork, area:mcp, area:tools, bug, platform:macos |
| [#87926](https://github.com/anthropics/claude-code/issues/87926) | fullscreen: "1 new message" banner stays after scrolling back to the bottom | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:macos |
| [#87924](https://github.com/anthropics/claude-code/issues/87924) | \[Bug\] Anthropic API Error: Content Flagged by Safety Filters for Legitimate Use Case | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:vscode, platform:windows |
| [#87923](https://github.com/anthropics/claude-code/issues/87923) | \[Bug\] RCE safeguard triggered during CTF testing | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:security, bug, needs-repro, platform:macos |
| [#87922](https://github.com/anthropics/claude-code/issues/87922) | \[FEATURE\] \`claude auth login --email\` should force the OAuth account chooser (prompt=select\_account) instead of reusing the browser's claude.ai session | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cli, enhancement |

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
