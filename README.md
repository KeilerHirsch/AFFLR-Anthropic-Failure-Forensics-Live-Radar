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
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
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
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
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

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87886](https://github.com/anthropics/claude-code/issues/87886) | \[Feature Request\] Add option to configure security checks behavior in Claude Code CLI | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87885](https://github.com/anthropics/claude-code/issues/87885) | \[BUG\] Directory-selection widget disappears when \`projects/&lt;slug&gt;/memory\` is an NTFS junction (Windows desktop) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | bug |
| [#87884](https://github.com/anthropics/claude-code/issues/87884) | Auto-compact should continue the same session instead of starting a new one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87883](https://github.com/anthropics/claude-code/issues/87883) | claude agents --json reports state: stopped, but the state set is undocumented and has no terminal flag | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87882](https://github.com/anthropics/claude-code/issues/87882) | Background session state.json: detail echoes the brief, state reads blocked when idle, and session writes are reverted | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent-view, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
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
| [#87867](https://github.com/anthropics/claude-code/issues/87867) | \[FEATURE\]  allow connecting to LiteLLM (third-party proxy) directly from the /login flow in the TUI | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | enhancement |
| [#87866](https://github.com/anthropics/claude-code/issues/87866) | \[Bug\] Claude.ai connectors unavailable in background/detached Claude Code sessions | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87864](https://github.com/anthropics/claude-code/issues/87864) | \[Bug\] Prompt Injection: User utterances can trigger unintended code execution | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87863](https://github.com/anthropics/claude-code/issues/87863) | Remote control: dead environment (404) shows misleading "Sign in again to verify your device" modal instead of environment-gone state | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:ui, bug, has repro, platform:macos |
| [#87862](https://github.com/anthropics/claude-code/issues/87862) | \[BUG\] Bun 1.4.0 segfault at address 0x10 on main thread (JSC JSStringJoiner/JSArray::fastToString frames) after 21.8 h session with 8 live subagents — CLI 2.1.235, Windows 11 26200 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:core, area:packaging, bug, platform:windows |
| [#87861](https://github.com/anthropics/claude-code/issues/87861) | Having issue to connect | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:browser-extension, duplicate |
| [#87860](https://github.com/anthropics/claude-code/issues/87860) | @-mention file completion spawns unbounded ripgrep processes (605 procs in ~2 min, 204 zombies, extension host crash) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87859](https://github.com/anthropics/claude-code/issues/87859) | OTel: git\_commit\_id is never emitted for commits created by cherry-pick / rebase / merge / revert | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, has repro |

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
