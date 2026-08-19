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
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#72862](https://github.com/anthropics/claude-code/issues/72862) | \[BUG\] macOS: Desktop app spawns headless sessions that mint new hashed keychain items, causing endless "security wants to access Claude Code-credentials" prompts | CLOSED / NOT\_PLANNED | security / trust boundary · high-signal label | 2026-08-19 | 2026-07-01 | area:auth, area:desktop, bug, has repro, platform:macos, stale |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#67258](https://github.com/anthropics/claude-code/issues/67258) | MCP OAuth with pre-configured oauth.clientId still attempts DCR: 'Incompatible auth server: does not support dynamic client registration' (v2.1.172, Box remote MCP) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-06-10 | area:auth, area:mcp, bug, has repro, platform:macos, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#74016](https://github.com/anthropics/claude-code/issues/74016) | Background daemon posts spurious "needs re-authentication" notification when a proactive OAuth refresh fails during macOS sleep/PowerNap dark-wake (transient, self-heals, auth never actually invalid) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-03 | area:auth, bug, has repro, platform:macos, stale |
| [#75676](https://github.com/anthropics/claude-code/issues/75676) | \[Bug\] Anthropic API Error: False positive cybersecurity content flag on legitimate local development diagnostics | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, bug, platform:macos, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87825](https://github.com/anthropics/claude-code/issues/87825) | Persistent memory rules are decorative — Claude ignores them before destructive actions, repeatedly, across sessions | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, memory, platform:macos |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#72808](https://github.com/anthropics/claude-code/issues/72808) | \[BUG\] headersHelper never executed for HTTP managedMcpServers (Claude Desktop, macOS) — static headers work, helper script silently ignored | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-19 | 2026-07-01 | api:bedrock, area:desktop, area:mcp, bug, platform:macos, stale |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#76293](https://github.com/anthropics/claude-code/issues/76293) | \[BUG\] Interactive CLI silently exits after successful Bash tool result; session resumes normally | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-10 | area:core, area:tui, bug, platform:macos, stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#74016](https://github.com/anthropics/claude-code/issues/74016) | Background daemon posts spurious "needs re-authentication" notification when a proactive OAuth refresh fails during macOS sleep/PowerNap dark-wake (transient, self-heals, auth never actually invalid) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-03 | area:auth, bug, has repro, platform:macos, stale |
| [#75676](https://github.com/anthropics/claude-code/issues/75676) | \[Bug\] Anthropic API Error: False positive cybersecurity content flag on legitimate local development diagnostics | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, bug, platform:macos, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#76293](https://github.com/anthropics/claude-code/issues/76293) | \[BUG\] Interactive CLI silently exits after successful Bash tool result; session resumes normally | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-10 | area:core, area:tui, bug, platform:macos, stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87926](https://github.com/anthropics/claude-code/issues/87926) | fullscreen: "1 new message" banner stays after scrolling back to the bottom | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:macos |
| [#87924](https://github.com/anthropics/claude-code/issues/87924) | \[Bug\] Anthropic API Error: Content Flagged by Safety Filters for Legitimate Use Case | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:vscode, platform:windows |
| [#87923](https://github.com/anthropics/claude-code/issues/87923) | \[Bug\] RCE safeguard triggered during CTF testing | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:security, bug, needs-repro, platform:macos |
| [#87922](https://github.com/anthropics/claude-code/issues/87922) | \[FEATURE\] \`claude auth login --email\` should force the OAuth account chooser (prompt=select\_account) instead of reusing the browser's claude.ai session | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cli, enhancement |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87919](https://github.com/anthropics/claude-code/issues/87919) | \[FEATURE\] Add a dedicated theme token for spinner tip text, separate from \`subtle\` | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:tui, area:ui, enhancement |
| [#87918](https://github.com/anthropics/claude-code/issues/87918) | \[BUG\] Markdown file links resolve against launch directory, not the session's worktree, after EnterWorktree | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, area:desktop, bug, platform:windows |
| [#87917](https://github.com/anthropics/claude-code/issues/87917) | \[FEATURE\] Add "Mark" action to text selection menu for highlighting reading position | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | invalid |
| [#87915](https://github.com/anthropics/claude-code/issues/87915) | skill-creator: run\_eval.py writes skills to .claude/commands/, so description optimization always measures recall=0% | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:plugins, area:skills, duplicate, platform:macos |
| [#87913](https://github.com/anthropics/claude-code/issues/87913) | ralph-loop: two copies of setup-ralph-loop.sh at v1.0.0; the unpatched one silently creates unstoppable loops | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:plugins, bug, has repro, platform:windows |
| [#87912](https://github.com/anthropics/claude-code/issues/87912) | \[BUG\] 2.1.234/2.1.235: interactive sessions in fullscreen TUI write no transcript JSONL at all (headless -p and non-fullscreen pty still do) — 2.1.233 fine | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, data-loss, has repro, platform:linux, regression |
| [#87911](https://github.com/anthropics/claude-code/issues/87911) | \[Bug\] Duplicate issue creation without prior verification against existing issues and design documentation | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:tui, bug, platform:windows |
| [#87910](https://github.com/anthropics/claude-code/issues/87910) | \[BUG\] Pycharm keeps freezing when using Claude on the terminal of the IDE | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:tui, bug, platform:intellij, platform:windows |
| [#87909](https://github.com/anthropics/claude-code/issues/87909) | \[BUG\] Session not visible in session list; no diagnostics for very large transcripts (165MB+) and bulk-touched mtimes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:core, bug, platform:macos |
| [#87908](https://github.com/anthropics/claude-code/issues/87908) | \[Feature Request\] Add CTF/security testing mode for controlled vulnerability exploitation | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, enhancement |
| [#87907](https://github.com/anthropics/claude-code/issues/87907) | \[Bug\] Anthropic API Error: Opus 5 Safeguards Flagged Legitimate Request | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:vscode, platform:windows |
| [#87906](https://github.com/anthropics/claude-code/issues/87906) | /insights Languages chart: no Swift/Objective-C in extension map; .h misattributed to C on iOS codebases | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:cli, bug, has repro, platform:macos, reproduced |
| [#87905](https://github.com/anthropics/claude-code/issues/87905) | \[BUG\] Claude in Chrome side panel dictation always "Microphone access is blocked" — claude.ai iframe missing \`microphone\` in allow attribute (v1.0.85) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:browser-extension, area:chrome, bug, has repro, platform:macos |
| [#87904](https://github.com/anthropics/claude-code/issues/87904) | \[BUG\] RemoteTrigger routine stalls silently after "Claude Code process started" — no tool calls, session stuck active/idle (same symptom as closed #54260) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:routines, bug, has repro |
| [#87903](https://github.com/anthropics/claude-code/issues/87903) | \[Bug\] Anthropic API Error: Cyber Safeguards Blocking Legitimate Requests | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:anthropic, area:model, bug, platform:linux |
| [#87902](https://github.com/anthropics/claude-code/issues/87902) | --continue can silently resume another live session's conversation when the working directory is shared | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:core, bug |
| [#87901](https://github.com/anthropics/claude-code/issues/87901) | Bundled ugrep runs away (4.7GB, 4h) on bounded-repeat pattern over long lines; complexity guard does not fire | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:tools, bug |
| [#87897](https://github.com/anthropics/claude-code/issues/87897) | \[MODEL\] Forked subagents (subagent\_type: fork) sometimes report status: completed after doing no work, with a result message unrelated to the assigned task | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, bug, platform:macos |
| [#87893](https://github.com/anthropics/claude-code/issues/87893) | \[Bug\] Session state inconsistency after /rewind and /resume with file state mismatch | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87890](https://github.com/anthropics/claude-code/issues/87890) | EnterWorktree does not propagate to PreToolUse hook subprocesses — hooks keep resolving against the original repo directory, not the worktree | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:hooks, bug, has repro, platform:windows |

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
