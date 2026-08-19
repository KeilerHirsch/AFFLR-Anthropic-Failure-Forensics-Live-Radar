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
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75322](https://github.com/anthropics/claude-code/issues/75322) | \[BUG\] awsCredentialRefresh ListInferenceProfiles failed: JSON Parse error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | api:bedrock, area:auth, bug, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75300](https://github.com/anthropics/claude-code/issues/75300) | \[Bug\]\[cyber\] False-positive block during routine sysadmin triage: process/event log checks and per-user mail-f (req\_011CcnvGWRHZqMtLSkb3HLxy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87661](https://github.com/anthropics/claude-code/issues/87661) | sdk-cli mode: Streamable HTTP MCP GET-stream aborts ~200-500ms after connect, tools vanish before first call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-06 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#76262](https://github.com/anthropics/claude-code/issues/76262) | Path-scoped --allowedTools 'Write(dir/\*\*)' denies the first out-of-scope write but a retried out-of-scope write in the same session is not re-checked and succeeds (headless -p) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:permissions, area:security, bug, has repro, platform:windows, stale |
| [#76243](https://github.com/anthropics/claude-code/issues/76243) | \[Bug\] Claude Code ignores stop instructions and continues tool execution after explicit rejection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:model, area:tools, bug, stale |
| [#76128](https://github.com/anthropics/claude-code/issues/76128) | \[Bug\] Config Files (claude.md, skills) Don't Override Default Behavior | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-09 | area:model, bug, platform:macos, stale |
| [#75322](https://github.com/anthropics/claude-code/issues/75322) | \[BUG\] awsCredentialRefresh ListInferenceProfiles failed: JSON Parse error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | api:bedrock, area:auth, bug, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75300](https://github.com/anthropics/claude-code/issues/75300) | \[Bug\]\[cyber\] False-positive block during routine sysadmin triage: process/event log checks and per-user mail-f (req\_011CcnvGWRHZqMtLSkb3HLxy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#75292](https://github.com/anthropics/claude-code/issues/75292) | claude-fable-5 fabricated a fake user turn inside its own output, containing self-addressed dangerous instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:model, area:security, bug, has repro, platform:macos, stale |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#40175](https://github.com/anthropics/claude-code/issues/40175) | \[BUG\] Cowork: Global instructions silently revert to older version after saving | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-28 | area:cowork, bug, has repro, platform:macos, platform:windows |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#87661](https://github.com/anthropics/claude-code/issues/87661) | sdk-cli mode: Streamable HTTP MCP GET-stream aborts ~200-500ms after connect, tools vanish before first call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87670](https://github.com/anthropics/claude-code/issues/87670) | Model fabricated a fake \`user\` turn and \`system\` block mid-response, then denied authorship; also refused an explicitly authorized deployment and the bug report about it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, platform:vscode, platform:windows |
| [#39027](https://github.com/anthropics/claude-code/issues/39027) | Background task notifications trigger autonomous API calls — model responds as if it were the user | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-03-25 | area:agents, area:core, area:permissions, bug, has repro, high-priority, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#87713](https://github.com/anthropics/claude-code/issues/87713) | \[BUG\] Desktop 1.32352.x: first-time OAuth MCP connect never opens the browser — version-negotiation probe wraps a client-side auth error, which is then misclassified as transport | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-06 | — |
| [#75325](https://github.com/anthropics/claude-code/issues/75325) | \[Bug\] Auto-mode classifier re-blocks the same verified-safe deterministic action every run, and treats a good-faith rewording of the prompt as evidence of evasion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-07 | area:agents, area:permissions, area:security, bug, platform:macos, stale |
| [#87770](https://github.com/anthropics/claude-code/issues/87770) | Claude in Chrome extension always binds to Desktop's native-messaging host, never the CLI's, even with Desktop fully quit | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:browser-extension, area:chrome, bug, duplicate, platform:macos |
| [#67873](https://github.com/anthropics/claude-code/issues/67873) | \[BUG\] \[Cowork\] Dispatch: per-tool MCP permission prompts in child task sessions are not forwarded to the mobile thread (regression) | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-06-12 | duplicate |
| [#53610](https://github.com/anthropics/claude-code/issues/53610) | \[Feature\] Multi-agent runtime needs mechanical enforcement: 9 gaps that defeat unattended overnight operation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-04-26 | area:agents, area:permissions, enhancement, platform:windows, stale |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87814](https://github.com/anthropics/claude-code/issues/87814) | Claude in Chrome extension fails to connect from Cowork desktop session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:chrome, area:cowork, area:mcp, bug |
| [#87813](https://github.com/anthropics/claude-code/issues/87813) | \[BUG\] Background processes not cleaned up on session exit, causing "file in use" errors on app update | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:bash, bug, platform:windows |
| [#87812](https://github.com/anthropics/claude-code/issues/87812) | \[Bug\] Daemon proactive refresh hangs ~9h on Windows, falls back to non-existent keychain | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:windows |
| [#87811](https://github.com/anthropics/claude-code/issues/87811) | \[BUG\] Cowork scheduled tasks never fire, even with app open and Cowork actively used (not just late — related to #36131) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cowork, area:routines, bug, platform:windows, regression |
| [#87810](https://github.com/anthropics/claude-code/issues/87810) | Feature: word-by-word gloss (interlinear translation) under English text, esp. thinking blocks | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:ui, enhancement |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87809](https://github.com/anthropics/claude-code/issues/87809) | \[BUG\] Permission classifier blocks the actions that would grant permission — no escape hatch in non-interactive sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:permissions, bug, platform:windows |
| [#87808](https://github.com/anthropics/claude-code/issues/87808) | \[BUG\] Gmail connector: all calls fail with "The caller does not have permission" despite valid OAuth grant | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | invalid |
| [#87807](https://github.com/anthropics/claude-code/issues/87807) | \[FEATURE\] Cowork: multi-choice question widget (AskUserQuestion) interrupts user before they finish reading the response | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cowork, area:ui, enhancement |
| [#87805](https://github.com/anthropics/claude-code/issues/87805) | Jammed background tasks + Remote Control reconnect loops silently consume Max usage window after forced token rotation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, area:auth, area:cost, bug, platform:macos |
| [#87804](https://github.com/anthropics/claude-code/issues/87804) | \[FEATURE\] Prompt-topic triggers for .claude/rules/ — \`paths:\` covers files, nothing covers subjects | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, enhancement |
| [#87803](https://github.com/anthropics/claude-code/issues/87803) | \[Bug\] Anthropic API Error: Account validation state mismatch for forensics access | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, platform:windows |
| [#87802](https://github.com/anthropics/claude-code/issues/87802) | \[Bug\] Dual-use safeguard false positives on legitimate defensive security review; mid-session auto-model-switch breaks continuity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, duplicate, platform:macos |
| [#87800](https://github.com/anthropics/claude-code/issues/87800) | Feature request: configurable safety-fallback target — Fable 5 should fall back to Opus 5, not Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, enhancement, platform:macos |
| [#87799](https://github.com/anthropics/claude-code/issues/87799) | \[BUG\] Claude Code hangs indefinitely in local console sessions on Windows — but works over SSH on the same machine | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:core, bug, platform:windows |
| [#87798](https://github.com/anthropics/claude-code/issues/87798) | \[Bug\] Misleading "cyber" flag name; functions as self-debugging tool, not cybersecurity feature | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-info, platform:macos |
| [#87797](https://github.com/anthropics/claude-code/issues/87797) | /design-sync: no way to declare a stylesheet 'stylesheet-only' — check\_design\_system scans the full styles.css closure for tokens | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:skills, enhancement |
| [#87796](https://github.com/anthropics/claude-code/issues/87796) | Published artifacts deleted server-side without user action on a personal account (no delete UI exists; links were already shared) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:claude-code-web, bug, data-loss |
| [#87795](https://github.com/anthropics/claude-code/issues/87795) | \[Bug\] Cloud routines fail silently when GitHub MCP removed but system prompt still requires it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:mcp, area:routines, bug, platform:macos |
| [#87794](https://github.com/anthropics/claude-code/issues/87794) | \[BUG\] Cowork VM fails to boot on Intel iMac — Claude Desktop burns 120% CPU nonstop | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:cowork, area:desktop, bug, platform:macos |
| [#87792](https://github.com/anthropics/claude-code/issues/87792) | Korean IME broken again after update to 2.1.235 (regression of #35307) | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, bug, has repro, platform:windows, regression |
| [#87791](https://github.com/anthropics/claude-code/issues/87791) | \[BUG\] MCP server reports \`hasTools: true\` on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-18 | area:mcp, bug, has repro, platform:linux |
| [#87790](https://github.com/anthropics/claude-code/issues/87790) | \[BUG\] Agent response Markdown rendering in TUI mutates meaning of content (renumbers ordered lists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tui, area:ui, bug, has repro, platform:linux |
| [#87789](https://github.com/anthropics/claude-code/issues/87789) | \[FEATURE\] Per-model effort levels: allow \`effortLevel\` to accept a model-keyed map | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:core, area:model, duplicate |
| [#87788](https://github.com/anthropics/claude-code/issues/87788) | \[BUG\] Capability-string effort fall back sends \`high\` instead of the highest supported level at or below | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | api:bedrock, area:model, bug, has repro, platform:macos |
| [#87787](https://github.com/anthropics/claude-code/issues/87787) | \[BUG\] Cloud routine (CCR) stuck at "Claude Code process started" — never executes | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:routines, bug, has repro |

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
