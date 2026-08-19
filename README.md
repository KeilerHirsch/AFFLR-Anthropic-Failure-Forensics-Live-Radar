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
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#72862](https://github.com/anthropics/claude-code/issues/72862) | \[BUG\] macOS: Desktop app spawns headless sessions that mint new hashed keychain items, causing endless "security wants to access Claude Code-credentials" prompts | CLOSED / NOT\_PLANNED | security / trust boundary · high-signal label | 2026-08-19 | 2026-07-01 | area:auth, area:desktop, bug, has repro, platform:macos, stale |
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
| [#87838](https://github.com/anthropics/claude-code/issues/87838) | claude mcp get/list print configured MCP secrets (headers, env vars) in cleartext with no masking | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:mcp, area:security, enhancement |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#72808](https://github.com/anthropics/claude-code/issues/72808) | \[BUG\] headersHelper never executed for HTTP managedMcpServers (Claude Desktop, macOS) — static headers work, helper script silently ignored | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-19 | 2026-07-01 | api:bedrock, area:desktop, area:mcp, bug, platform:macos, stale |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
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
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#74734](https://github.com/anthropics/claude-code/issues/74734) | Fable 5 session repeatedly auto-downgraded to Opus 4.8 (suspected safety-classifier false positive on normal deploy work) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-06 | area:model, bug, model, platform:vscode, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87967](https://github.com/anthropics/claude-code/issues/87967) | Worktree isolation: session guidance suggests the ! prefix as a workaround, but ! runs in the same session and hits the identical block | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:bash, area:sandbox, bug |
| [#87966](https://github.com/anthropics/claude-code/issues/87966) | \[BUG\] Prompt cache lookup fails intermittently mid-session — cache\_read pinned to the stable-prefix boundary, 89 full-context rewrites across 9 days (~59M excess cache\_creation tokens) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:core, area:cost, area:mcp, bug, has repro, platform:windows |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#87964](https://github.com/anthropics/claude-code/issues/87964) | \[Bug\] Unexpected model switch to opus-4-1 during file read operations | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:windows |
| [#87963](https://github.com/anthropics/claude-code/issues/87963) | \[BUG\] Remote Control: ending a session from the app exits the child 1, so the bridge reports a crash and permanently leaks the worktree | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:self-hosted-environments, bug, has repro, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87962](https://github.com/anthropics/claude-code/issues/87962) | Artifact live-update monitor (monitor\_ws) persists indefinitely in scheduled-task sessions, blocking app restart — no way to disable auto-arm or auto-exit the session | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:routines, bug, platform:windows |
| [#87961](https://github.com/anthropics/claude-code/issues/87961) | Feature request: import/create comment threads on Artifacts (round-trip serialization) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, enhancement |
| [#87959](https://github.com/anthropics/claude-code/issues/87959) | Worktree-isolation Bash guard refuses every compound command, even with no git usage at all | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:bash, area:sandbox, enhancement, platform:macos |
| [#87958](https://github.com/anthropics/claude-code/issues/87958) | /cd changes the working directory but does not relocate the session to the new project storage | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:linux |
| [#87957](https://github.com/anthropics/claude-code/issues/87957) | Claude in Chrome extension not connecting — tabs\_context\_mcp reports "not connected" despite correct install, sign-in, and restart | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:chrome, area:cowork, duplicate |
| [#87956](https://github.com/anthropics/claude-code/issues/87956) | \[BUG\] "Set up auto mode for your environment?" dialog is uncompletable: Enter toggles the checkbox instead of submitting and arrow keys never reach Continue | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, area:ui, bug, has repro, platform:macos |
| [#87955](https://github.com/anthropics/claude-code/issues/87955) | \[FEATURE\] A structured channel for users to submit ideas, with opt-in transcript sharing and reciprocity | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:cli, enhancement |
| [#87954](https://github.com/anthropics/claude-code/issues/87954) | \[FEATURE\] Cross-session conversation channel: let two users' Claude Code sessions talk to each other | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:agents, enhancement |
| [#87953](https://github.com/anthropics/claude-code/issues/87953) | Subagent Bash cwd resets to another subagent's worktree, with no cwd param to pin it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:bash, bug, platform:windows |
| [#87952](https://github.com/anthropics/claude-code/issues/87952) | Remote Control mobile/desktop view: show currently running subagents (live agent roster) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent-view, area:ui, enhancement |
| [#87951](https://github.com/anthropics/claude-code/issues/87951) | Remote Control view renders the injected cross-session security preamble verbatim on every teammate message — terminal view collapses it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent-view, area:ui, bug, platform:ios, platform:web |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87949](https://github.com/anthropics/claude-code/issues/87949) | \[Bug\] Anthropic API Error: Overly Aggressive Content Filtering on Legitimate Cybersecurity Development Work | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, duplicate, external, platform:macos |
| [#87948](https://github.com/anthropics/claude-code/issues/87948) | \[BUG\] run\_in\_background tasks intermittently killed ~17-20s after start, seconds after the arming turn ends (terminal CLI, Linux — not idle-timeout timing) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:core, bug, has repro, platform:linux |
| [#87947](https://github.com/anthropics/claude-code/issues/87947) | Print/SDK mode persists empty thinking blocks in session transcript (signature only) — interactive mode persists full text | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:windows |
| [#87946](https://github.com/anthropics/claude-code/issues/87946) | \[BUG\] thinking summary language | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:api, area:model, bug |
| [#87945](https://github.com/anthropics/claude-code/issues/87945) | Browser tool navigate consistently fails with "denied or failed" for previously-working sites | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:mcp, bug, platform:windows |
| [#87943](https://github.com/anthropics/claude-code/issues/87943) | \[BUG\] VS Code panel: sequential edits to one file diff each proposal against a stale snapshot (diff-editor tab only) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:vscode, bug, has repro, platform:linux, platform:vscode |
| [#87942](https://github.com/anthropics/claude-code/issues/87942) | Personal Pro subscription blocked in Claude Code — "organization has disabled subscription access" (auto-generated personal org) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, duplicate, platform:windows |
| [#87941](https://github.com/anthropics/claude-code/issues/87941) | \[Bug\] Anthropic API Error: Sonnet 5 Safeguards Flagging Verified Cyber Users | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:windows |

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
