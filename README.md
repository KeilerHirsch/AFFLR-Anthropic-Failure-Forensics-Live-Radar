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
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#87825](https://github.com/anthropics/claude-code/issues/87825) | Persistent memory rules are decorative — Claude ignores them before destructive actions, repeatedly, across sessions | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, memory, platform:macos |
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87838](https://github.com/anthropics/claude-code/issues/87838) | claude mcp get/list print configured MCP secrets (headers, env vars) in cleartext with no masking | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:mcp, area:security, enhancement |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |
| [#87805](https://github.com/anthropics/claude-code/issues/87805) | Jammed background tasks + Remote Control reconnect loops silently consume Max usage window after forced token rotation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, area:auth, area:cost, bug, platform:macos |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87857](https://github.com/anthropics/claude-code/issues/87857) | Thai text (and other space-less scripts) misaligns/right-shifts on line wrap, especially when the terminal is resized | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:a11y, area:tui, bug, platform:windows |
| [#87856](https://github.com/anthropics/claude-code/issues/87856) | \[BUG\] Thai output loses characters in the pty bytes themselves — TUI frame composition counts combining marks as one column (v2.1.235, Windows) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87855](https://github.com/anthropics/claude-code/issues/87855) | \[BUG\] claude-sonnet-5 cost inflated exactly 1.5x on first-party API — pricing table uses $3/$15 instead of the (now permanent) $2/$10 rates | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87854](https://github.com/anthropics/claude-code/issues/87854) | \[BUG\] Desktop app browser does not retain sessions despite session persistence set to shared | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, bug, platform:macos |
| [#87853](https://github.com/anthropics/claude-code/issues/87853) | Desktop app browser has no system password manager integration (Apple Passwords autofill unavailable on macOS) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87852](https://github.com/anthropics/claude-code/issues/87852) | Desktop app browser cannot complete passkey / WebAuthn sign-in (no platform authenticator, no Bluetooth hybrid transport) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:desktop, enhancement, platform:macos |
| [#87851](https://github.com/anthropics/claude-code/issues/87851) | Subagent view header shows the main session's model, not the subagent's | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:agent-view, area:ui, bug, platform:linux |
| [#87850](https://github.com/anthropics/claude-code/issues/87850) | \[Bug\] Auto-mode permission classifier denies allowed operations silently with incorrect remediation guidance | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:permissions, bug, has repro, platform:linux |
| [#87849](https://github.com/anthropics/claude-code/issues/87849) | \[Bug\] Claude Code hangs on startup after update in RustRover IDE | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:ide, bug, platform:intellij, platform:macos |
| [#87848](https://github.com/anthropics/claude-code/issues/87848) | Bundled search helper allocates without bound on a BRE pattern with a literal \| and -o (v2.1.233) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, bug, has repro, perf:memory, platform:linux |
| [#87847](https://github.com/anthropics/claude-code/issues/87847) | /code-review ultra fails server-side and consumes free-review quota with zero output | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:skills, bug |
| [#87846](https://github.com/anthropics/claude-code/issues/87846) | \[Feature Request\] Add legitimate coding pattern recognition to reduce false positive security flags | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87845](https://github.com/anthropics/claude-code/issues/87845) | \[Bug\] Model reasoning degradation affecting agent and workflow generation quality | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#87844](https://github.com/anthropics/claude-code/issues/87844) | \[desktop\] "Show background tasks" missing from Dispatch kebab menu until app relaunch (macOS) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:ui, bug, platform:macos |
| [#87843](https://github.com/anthropics/claude-code/issues/87843) | \[BUG\]Scheduled task stalls indefinitely on Write permission prompt despite matching allow rule (settings.json correct) | CLOSED / COMPLETED | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:skills, bug, platform:macos |
| [#87842](https://github.com/anthropics/claude-code/issues/87842) | \[Bug\] API Error: Non-streaming request receives event-stream response (HTTP 200) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:api, area:networking, bug, platform:macos |
| [#87840](https://github.com/anthropics/claude-code/issues/87840) | \[BUG\] manual sorting in sidebar session groups no longer works | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:ui, bug, platform:windows, regression |
| [#87839](https://github.com/anthropics/claude-code/issues/87839) | Session management: no way to browse/delete old sessions by content, only by opaque UUID filename | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, enhancement |
| [#87838](https://github.com/anthropics/claude-code/issues/87838) | claude mcp get/list print configured MCP secrets (headers, env vars) in cleartext with no masking | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:mcp, area:security, enhancement |
| [#87836](https://github.com/anthropics/claude-code/issues/87836) | Headless -p session exits when a turn ends while a background task is the only pending wake signal | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:cli, area:core, bug, platform:linux |
| [#87835](https://github.com/anthropics/claude-code/issues/87835) | Non-fork subagents receive auto-memory (MEMORY.md) in full, contradicting docs; no per-agent way to trim CLAUDE.md inheritance | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, area:cost, bug, has repro, platform:macos |
| [#87834](https://github.com/anthropics/claude-code/issues/87834) | \[FEATURE\] Shared memory / persistent identity across Claude sessions | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | enhancement |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#87832](https://github.com/anthropics/claude-code/issues/87832) | \[BUG\] Fable→Opus model\_consent\_fallback auto-cancels without displaying the prompt (186 events, 0 shown) — still occurring on 2.1.233 after #79337 closed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:model, duplicate, platform:macos |
| [#87831](https://github.com/anthropics/claude-code/issues/87831) | Auto-mode classifier "blocked" error doesn't reliably indicate whether the action executed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |

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
