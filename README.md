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
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75322](https://github.com/anthropics/claude-code/issues/75322) | \[BUG\] awsCredentialRefresh ListInferenceProfiles failed: JSON Parse error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | api:bedrock, area:auth, bug, platform:macos, stale |
| [#75300](https://github.com/anthropics/claude-code/issues/75300) | \[Bug\]\[cyber\] False-positive block during routine sysadmin triage: process/event log checks and per-user mail-f (req\_011CcnvGWRHZqMtLSkb3HLxy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87661](https://github.com/anthropics/claude-code/issues/87661) | sdk-cli mode: Streamable HTTP MCP GET-stream aborts ~200-500ms after connect, tools vanish before first call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#87644](https://github.com/anthropics/claude-code/issues/87644) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, duplicate, has repro, platform:macos, regression |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-06 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |
| [#76236](https://github.com/anthropics/claude-code/issues/76236) | \[BUG\] \`CLAUDE\_CODE\_SUBPROCESS\_ENV\_SCRUB=1\` leaves an empty \`~/.bash\_profile\` behind, silently breaking login-shell PATH | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-07-10 | area:sandbox, bug, has repro, platform:linux, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75322](https://github.com/anthropics/claude-code/issues/75322) | \[BUG\] awsCredentialRefresh ListInferenceProfiles failed: JSON Parse error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | api:bedrock, area:auth, bug, platform:macos, stale |
| [#75300](https://github.com/anthropics/claude-code/issues/75300) | \[Bug\]\[cyber\] False-positive block during routine sysadmin triage: process/event log checks and per-user mail-f (req\_011CcnvGWRHZqMtLSkb3HLxy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87661](https://github.com/anthropics/claude-code/issues/87661) | sdk-cli mode: Streamable HTTP MCP GET-stream aborts ~200-500ms after connect, tools vanish before first call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#87644](https://github.com/anthropics/claude-code/issues/87644) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, duplicate, has repro, platform:macos, regression |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-06 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |
| [#76144](https://github.com/anthropics/claude-code/issues/76144) | \[BUG\] Worktree pool writes .git/worktrees/&lt;name&gt;/gitdir as literal ".git", flagging healthy worktrees "prunable"; dormant ones then get reclaimed/deleted | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:desktop, bug, data-loss, has repro, platform:macos, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87791](https://github.com/anthropics/claude-code/issues/87791) | \[BUG\] MCP server reports \`hasTools: true\` on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |
| [#87789](https://github.com/anthropics/claude-code/issues/87789) | \[FEATURE\] Per-model effort levels: allow \`effortLevel\` to accept a model-keyed map | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:core, area:model, duplicate |
| [#87788](https://github.com/anthropics/claude-code/issues/87788) | \[BUG\] Capability-string effort fall back sends \`high\` instead of the highest supported level at or below | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | api:bedrock, area:model, bug, has repro, platform:macos |
| [#87787](https://github.com/anthropics/claude-code/issues/87787) | \[BUG\] Cloud routine (CCR) stuck at "Claude Code process started" — never executes | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:routines, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87786](https://github.com/anthropics/claude-code/issues/87786) | /mcp reconnect &lt;server&gt; fails with CLI-only "terminal is still starting up" error in VS Code extension | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:mcp, duplicate, platform:macos, platform:vscode |
| [#87785](https://github.com/anthropics/claude-code/issues/87785) | \[BUG\] Opening suno.com in the preview browser crashes Claude Desktop and it won't launch again until reinstalled | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | invalid |
| [#87783](https://github.com/anthropics/claude-code/issues/87783) | Auto memory persists claims but not observations: no record of which sources a note was read from, so drifted and never-bound notes are indistinguishable | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | enhancement, memory |
| [#87782](https://github.com/anthropics/claude-code/issues/87782) | \[FEATURE\] Let a folder on a WSL path open as a Local (Windows) session | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:desktop, enhancement, platform:wsl |
| [#87779](https://github.com/anthropics/claude-code/issues/87779) | Agent View: add a way to add a new project folder without relaunching Claude Code | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:agent-view, enhancement |
| [#87774](https://github.com/anthropics/claude-code/issues/87774) | \[Claude in Chrome / macOS\] Service worker restarts drop session→tab-group mapping every few minutes; timed-out tool calls actually executed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:chrome, bug, has repro, platform:macos |
| [#87772](https://github.com/anthropics/claude-code/issues/87772) | \[BUG\] Days permanently disappear from the desktop usage heatmap because only the CLI writes the stats cache | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:desktop, bug, data-loss, has repro, platform:macos |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#87769](https://github.com/anthropics/claude-code/issues/87769) | \[FEATURE\] Mouse support in the terminal UI — click-to-navigate and cursor interaction | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:tui, enhancement |
| [#87767](https://github.com/anthropics/claude-code/issues/87767) | Claude in Chrome: native host broadcasts every tool response to all connected MCP clients — concurrent sessions silently receive each other's results | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:chrome, area:mcp, bug, has repro, platform:windows |
| [#87761](https://github.com/anthropics/claude-code/issues/87761) | Opus orchestrator contaminates "independent" subagent consults: injects its own candidate answers, relabels an unverified subagent claim as VERIFIED, and transmits a rejected design's frame while warning against it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:agents, area:model, bug, platform:linux |
| [#87759](https://github.com/anthropics/claude-code/issues/87759) | \[BUG\] Cowork VM fails to boot on Intel Mac after update to 1.32352.1 — guest kernel halts at ~1.7 s, host hangs at usernet: calling AcceptBess (works on 1.25927.0) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, has repro, platform:macos, regression |
| [#87758](https://github.com/anthropics/claude-code/issues/87758) | \[Bug\] Anthropic API Error: Overly restrictive content filtering for legitimate game development queries | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, needs-repro, platform:linux |
| [#87754](https://github.com/anthropics/claude-code/issues/87754) | \[Bug\] Safeguard triggered during app test execution | OPEN | observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, needs-info, platform:macos |
| [#87753](https://github.com/anthropics/claude-code/issues/87753) | \[BUG\] Editing an SSH connection's port doesn't propagate to existing sessions using it | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:desktop, bug, has repro, platform:macos |
| [#87750](https://github.com/anthropics/claude-code/issues/87750) | \[BUG\] Cowork browser fallback crashes app, leaves it unable to launch ("This app can't open") — recurs even after reinstall | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, platform:windows |
| [#87749](https://github.com/anthropics/claude-code/issues/87749) | \[BUG\] Cowork VM: guest kernel boots but init hangs at 1.5s — "Direct-boot artifacts not present" false negative forces broken EFI/GRUB fallback (v1.32352.1, macOS 26.5.2 Intel) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, duplicate, platform:macos, regression |
| [#87748](https://github.com/anthropics/claude-code/issues/87748) | \[BUG\] Default cleanupPeriodDays:30 silently deletes local transcripts, leaving unopenable sessions in the Desktop sidebar | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:core, area:desktop, bug, data-loss, duplicate, platform:windows |
| [#87745](https://github.com/anthropics/claude-code/issues/87745) | Moving a session to an existing project name ungroups all sessions | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:ui, bug, has repro, platform:windows |
| [#87743](https://github.com/anthropics/claude-code/issues/87743) | Claude Desktop: no session-scoped model override, and floor-reset notifications are noisy/token-costly | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | invalid |

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
