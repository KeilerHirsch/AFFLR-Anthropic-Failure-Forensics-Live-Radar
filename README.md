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
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#87825](https://github.com/anthropics/claude-code/issues/87825) | Persistent memory rules are decorative — Claude ignores them before destructive actions, repeatedly, across sessions | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, memory, platform:macos |
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#87838](https://github.com/anthropics/claude-code/issues/87838) | claude mcp get/list print configured MCP secrets (headers, env vars) in cleartext with no masking | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:mcp, area:security, enhancement |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |
| [#87805](https://github.com/anthropics/claude-code/issues/87805) | Jammed background tasks + Remote Control reconnect loops silently consume Max usage window after forced token rotation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, area:auth, area:cost, bug, platform:macos |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |
| [#87805](https://github.com/anthropics/claude-code/issues/87805) | Jammed background tasks + Remote Control reconnect loops silently consume Max usage window after forced token rotation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, area:auth, area:cost, bug, platform:macos |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |
| [#76144](https://github.com/anthropics/claude-code/issues/76144) | \[BUG\] Worktree pool writes .git/worktrees/&lt;name&gt;/gitdir as literal ".git", flagging healthy worktrees "prunable"; dormant ones then get reclaimed/deleted | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:desktop, bug, data-loss, has repro, platform:macos, stale |
| [#76127](https://github.com/anthropics/claude-code/issues/76127) | \[Bug\] Model ignores user directives when conflicting with default behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87900](https://github.com/anthropics/claude-code/issues/87900) | VS Code extension: startup indexing rewrites session mtimes, scrambling history sort order | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:ide, bug, has repro, platform:vscode, platform:windows |
| [#87897](https://github.com/anthropics/claude-code/issues/87897) | \[MODEL\] Forked subagents (subagent\_type: fork) sometimes report status: completed after doing no work, with a result message unrelated to the assigned task | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, bug, platform:macos |
| [#87896](https://github.com/anthropics/claude-code/issues/87896) | \[Bug\] Session limit triggered by unexpected agent behavior outside user instructions | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, area:model, bug, platform:linux |
| [#87893](https://github.com/anthropics/claude-code/issues/87893) | \[Bug\] Session state inconsistency after /rewind and /resume with file state mismatch | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87892](https://github.com/anthropics/claude-code/issues/87892) | Possibilita di colorare i gruppi nella sidebar delle sessioni | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87891](https://github.com/anthropics/claude-code/issues/87891) | \[BUG\] Background daemon never reaps stale workers or unclaimed spares — they are re-adopted on every restart (64 leaked processes / ~7.1 GB after six weeks) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, bug, has repro, platform:macos |
| [#87890](https://github.com/anthropics/claude-code/issues/87890) | EnterWorktree does not propagate to PreToolUse hook subprocesses — hooks keep resolving against the original repo directory, not the worktree | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:hooks, bug, has repro, platform:windows |
| [#87889](https://github.com/anthropics/claude-code/issues/87889) | \[BUG\] No audit trail for retention cleanup — deleted sessions leave no log, making the loss unverifiable after the fact | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | bug |
| [#87886](https://github.com/anthropics/claude-code/issues/87886) | \[Feature Request\] Add option to configure security checks behavior in Claude Code CLI | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87885](https://github.com/anthropics/claude-code/issues/87885) | \[BUG\] Directory-selection widget disappears when \`projects/&lt;slug&gt;/memory\` is an NTFS junction (Windows desktop) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | bug |
| [#87884](https://github.com/anthropics/claude-code/issues/87884) | Auto-compact should continue the same session instead of starting a new one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87883](https://github.com/anthropics/claude-code/issues/87883) | claude agents --json reports state: stopped, but the state set is undocumented and has no terminal flag | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87882](https://github.com/anthropics/claude-code/issues/87882) | Background session state.json: detail echoes the brief, state reads blocked when idle, and session writes are reverted | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent-view, bug, platform:linux |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87879](https://github.com/anthropics/claude-code/issues/87879) | \[BUG\] MSIX in-place update leaks a container silo, making Claude Desktop unlaunchable until reboot (0x80070020) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87878](https://github.com/anthropics/claude-code/issues/87878) | \[FEATURE\] Restore Session from inside Claude Desktop | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, enhancement |
| [#87877](https://github.com/anthropics/claude-code/issues/87877) | Remote Control: no way to archive/clean up disconnected sessions on claude.ai | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87876](https://github.com/anthropics/claude-code/issues/87876) | \[BUG\] Subscription features are withdrawn when \`ANTHROPIC\_BASE\_URL\` isn't the official string, even when the proxy terminates at Anthropic | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:networking, area:statusline, bug, has repro, platform:linux |
| [#87875](https://github.com/anthropics/claude-code/issues/87875) | Add the Browser pane's annotate (pencil) tool to the iOS Simulator panel | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:ui, enhancement, platform:ios |
| [#87874](https://github.com/anthropics/claude-code/issues/87874) | Subagent orchestration has no concurrency model: no join, no cancellation semantics, no quiescent stop, no signal ordering — and the semantics change silently between releases | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87872](https://github.com/anthropics/claude-code/issues/87872) | \[Bug\] Context limit error when sesssion context space available | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87871](https://github.com/anthropics/claude-code/issues/87871) | Model emitted a standalone assistant turn impersonating a user instruction (asked to bypass review and push to prod) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro, platform:macos |
| [#87870](https://github.com/anthropics/claude-code/issues/87870) | Cross-session messaging (agents\_cross\_session\_inbox) is enabled on Linux but not Windows for the same account | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, duplicate, platform:windows |
| [#87869](https://github.com/anthropics/claude-code/issues/87869) | \[macOS\] Korean (Hangul) IME composition is a daily usability blocker for CLI real-time typing — consolidating related reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:macos |
| [#87868](https://github.com/anthropics/claude-code/issues/87868) | \[Bug\] Bun runtime segmentation fault during long-running interactive session with multiple subagents | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |

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
