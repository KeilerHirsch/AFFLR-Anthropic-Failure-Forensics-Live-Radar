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
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79883](https://github.com/anthropics/claude-code/issues/79883) | Memory feature's own directory (~/.claude/projects/&lt;id&gt;/memory/) is blocked by the .claude sensitive-file guardrail — no way to pre-authorize | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80170](https://github.com/anthropics/claude-code/issues/80170) | \[Bug\] Permission classifier blocks safe command phrasings during production incidents, ignoring settings.json allowlists | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:permissions |
| [#80045](https://github.com/anthropics/claude-code/issues/80045) | Security: MCP server \`env\` secrets exposed in plaintext via \`--mcp-config\` argv (visible in \`ps\`/\`/proc\`/EDR logs) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:ide |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#79750](https://github.com/anthropics/claude-code/issues/79750) | \[Bug\] Auto-mode classifier inherits \[1m\] suffix, causing repeated permission check failures and session lockout | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80552](https://github.com/anthropics/claude-code/issues/80552) | Auto-mode classifier denies a destructive MCP tool call after it already succeeded (mismatched tool\_use\_id) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:permissions |
| [#81090](https://github.com/anthropics/claude-code/issues/81090) | Custom HTTP MCP server: OAuth authorization does not persist across launches, and server visibility is inconsistent across surfaces | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:mcp |
| [#81100](https://github.com/anthropics/claude-code/issues/81100) | \[BUG\] Desktop app: 30-day retention sweep deletes the only copy of Desktop transcripts, leaving unopenable ghost entries in the session list | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:desktop |
| [#81142](https://github.com/anthropics/claude-code/issues/81142) | Auto mode classifier sends \[1m\]-suffixed model without the 1M beta header; HTTP 400 is reported as "temporarily unavailable" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81378](https://github.com/anthropics/claude-code/issues/81378) | PowerShell command blocked citing a path unrelated to the command; here-string text content is scanned as code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-26 | area:permissions |
| [#80426](https://github.com/anthropics/claude-code/issues/80426) | Desktop app (Windows/MSIX) intermittently fails to start after self-inflicted race condition on native-host install; recovery wipes local session index | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:desktop |
| [#80999](https://github.com/anthropics/claude-code/issues/80999) | Windows: hidden Browser-pane preview kills the app via Code Integrity block on packaged vk\_swiftshader.dll, then "Repair" dialog | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:desktop |
| [#81041](https://github.com/anthropics/claude-code/issues/81041) | permissions.ask rules are loaded and displayed in /permissions but never enforced (2.1.219, macOS) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81526](https://github.com/anthropics/claude-code/issues/81526) | \[BUG\] Sandbox silently deletes project-root \`refs/\`, \`objects/\`, \`HEAD\` created mid-session — recursive, no prompt (macOS, 2.1.220) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:core |
| [#82167](https://github.com/anthropics/claude-code/issues/82167) | \[Bug\] Settings file corrupted to \`{}\` by stale in-memory config persisting over concurrent writes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-29 | area:core |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81745](https://github.com/anthropics/claude-code/issues/81745) | \[BUG\] Windows MSIX: Code Integrity blocks vk\_swiftshader.dll in the GPU process on first in-app Browser use, package flagged NeedsRemediation, app self-terminates (root cause for #49676) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:desktop |
| [#82748](https://github.com/anthropics/claude-code/issues/82748) | \[Bug\] \`claude-opus-5\` absent from client model table on 2.1.212 — /context uses a 200K denominator while auto-compact and the API both use 1M | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-30 | area:core |
| [#83058](https://github.com/anthropics/claude-code/issues/83058) | \[BUG\] Recursive rm deleted ~200 GB of home directory — no approval prompt for a delete outside the project cwd | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | area:permissions |
| [#74913](https://github.com/anthropics/claude-code/issues/74913) | \[BUG\] Claude Desktop (macOS): chat MCP tool calls time out with zero network activity when a system PAC is configured; configured MCP server stays connected and never receives tools/call | OPEN / REOPENED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-06 | area:desktop, area:mcp, invalid, stale |
| [#79804](https://github.com/anthropics/claude-code/issues/79804) | New chat sessions without an explicitly selected project can default the working directory to the entire user home folder (unscoped, expensive tool reads) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:desktop |
| [#79759](https://github.com/anthropics/claude-code/issues/79759) | \[BUG\] Permission model: let a specific allow override a broad deny (specificity-aware precedence) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80809](https://github.com/anthropics/claude-code/issues/80809) | Subagent fabricated an urgent 'user message' inside its own end\_turn output; orchestrator on automated wake initially believed it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:agents |
| [#81083](https://github.com/anthropics/claude-code/issues/81083) | \[BUG\] claude.ai connectors not registered at session start in task-chip-spawned sessions; appear only mid-session as UUID servers, while plugin:productivity:\* keeps claiming they need auth | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:mcp |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79883](https://github.com/anthropics/claude-code/issues/79883) | Memory feature's own directory (~/.claude/projects/&lt;id&gt;/memory/) is blocked by the .claude sensitive-file guardrail — no way to pre-authorize | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80170](https://github.com/anthropics/claude-code/issues/80170) | \[Bug\] Permission classifier blocks safe command phrasings during production incidents, ignoring settings.json allowlists | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:permissions |
| [#80045](https://github.com/anthropics/claude-code/issues/80045) | Security: MCP server \`env\` secrets exposed in plaintext via \`--mcp-config\` argv (visible in \`ps\`/\`/proc\`/EDR logs) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:ide |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#79750](https://github.com/anthropics/claude-code/issues/79750) | \[Bug\] Auto-mode classifier inherits \[1m\] suffix, causing repeated permission check failures and session lockout | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80552](https://github.com/anthropics/claude-code/issues/80552) | Auto-mode classifier denies a destructive MCP tool call after it already succeeded (mismatched tool\_use\_id) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:permissions |
| [#81090](https://github.com/anthropics/claude-code/issues/81090) | Custom HTTP MCP server: OAuth authorization does not persist across launches, and server visibility is inconsistent across surfaces | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:mcp |
| [#81100](https://github.com/anthropics/claude-code/issues/81100) | \[BUG\] Desktop app: 30-day retention sweep deletes the only copy of Desktop transcripts, leaving unopenable ghost entries in the session list | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:desktop |
| [#81142](https://github.com/anthropics/claude-code/issues/81142) | Auto mode classifier sends \[1m\]-suffixed model without the 1M beta header; HTTP 400 is reported as "temporarily unavailable" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81378](https://github.com/anthropics/claude-code/issues/81378) | PowerShell command blocked citing a path unrelated to the command; here-string text content is scanned as code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-26 | area:permissions |
| [#80426](https://github.com/anthropics/claude-code/issues/80426) | Desktop app (Windows/MSIX) intermittently fails to start after self-inflicted race condition on native-host install; recovery wipes local session index | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:desktop |
| [#80999](https://github.com/anthropics/claude-code/issues/80999) | Windows: hidden Browser-pane preview kills the app via Code Integrity block on packaged vk\_swiftshader.dll, then "Repair" dialog | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:desktop |
| [#81041](https://github.com/anthropics/claude-code/issues/81041) | permissions.ask rules are loaded and displayed in /permissions but never enforced (2.1.219, macOS) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81526](https://github.com/anthropics/claude-code/issues/81526) | \[BUG\] Sandbox silently deletes project-root \`refs/\`, \`objects/\`, \`HEAD\` created mid-session — recursive, no prompt (macOS, 2.1.220) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:core |
| [#82167](https://github.com/anthropics/claude-code/issues/82167) | \[Bug\] Settings file corrupted to \`{}\` by stale in-memory config persisting over concurrent writes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-29 | area:core |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81745](https://github.com/anthropics/claude-code/issues/81745) | \[BUG\] Windows MSIX: Code Integrity blocks vk\_swiftshader.dll in the GPU process on first in-app Browser use, package flagged NeedsRemediation, app self-terminates (root cause for #49676) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:desktop |
| [#82748](https://github.com/anthropics/claude-code/issues/82748) | \[Bug\] \`claude-opus-5\` absent from client model table on 2.1.212 — /context uses a 200K denominator while auto-compact and the API both use 1M | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-30 | area:core |
| [#83058](https://github.com/anthropics/claude-code/issues/83058) | \[BUG\] Recursive rm deleted ~200 GB of home directory — no approval prompt for a delete outside the project cwd | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | area:permissions |
| [#74913](https://github.com/anthropics/claude-code/issues/74913) | \[BUG\] Claude Desktop (macOS): chat MCP tool calls time out with zero network activity when a system PAC is configured; configured MCP server stays connected and never receives tools/call | OPEN / REOPENED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-06 | area:desktop, area:mcp, invalid, stale |
| [#79804](https://github.com/anthropics/claude-code/issues/79804) | New chat sessions without an explicitly selected project can default the working directory to the entire user home folder (unscoped, expensive tool reads) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:desktop |
| [#79759](https://github.com/anthropics/claude-code/issues/79759) | \[BUG\] Permission model: let a specific allow override a broad deny (specificity-aware precedence) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80809](https://github.com/anthropics/claude-code/issues/80809) | Subagent fabricated an urgent 'user message' inside its own end\_turn output; orchestrator on automated wake initially believed it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:agents |
| [#81083](https://github.com/anthropics/claude-code/issues/81083) | \[BUG\] claude.ai connectors not registered at session start in task-chip-spawned sessions; appear only mid-session as UUID servers, while plugin:productivity:\* keeps claiming they need auth | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:mcp |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88129](https://github.com/anthropics/claude-code/issues/88129) | Feature request: external/programmatic writes to the session task list (~/.claude/tasks) — or a disk re-read contract for the task panel | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tools, area:tui, enhancement |
| [#88128](https://github.com/anthropics/claude-code/issues/88128) | \[BUG\] MCP tools/list and resources/list rejected as invalid when optional ttlMs/cacheScope cache hints are omitted (protocol 2026-07-28) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#88127](https://github.com/anthropics/claude-code/issues/88127) | VS Code extension: allow opening existing conversations in the native panel regardless of their working directory | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:ide, enhancement, platform:vscode |
| [#88126](https://github.com/anthropics/claude-code/issues/88126) | Sessions silently deleted without user action | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | bug, data-loss, platform:macos |
| [#88125](https://github.com/anthropics/claude-code/issues/88125) | send\_message (ccd\_session\_mgmt) silently stops delivering and wedges the recipient session — regression since CLI 2.1.227 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:desktop, bug, has repro, platform:macos, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88124](https://github.com/anthropics/claude-code/issues/88124) | Auto-update at boot invalidates session, forces relogin | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:auth, area:packaging, bug, platform:windows |
| [#88122](https://github.com/anthropics/claude-code/issues/88122) | Model fabricated a user message and executed it: unrequested git commit, push, and issue edit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:model, area:security, bug, platform:macos |
| [#88121](https://github.com/anthropics/claude-code/issues/88121) | CoworkVMService restarts silently kill running scheduled-task sessions mid-turn — no recovery actions configured | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:cowork, bug, has repro, perf:memory, platform:windows |
| [#88120](https://github.com/anthropics/claude-code/issues/88120) | \[Bug\] claude-api skill context usage balloons to hundreds of thousands of tokens on basic queries | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:skills, bug, duplicate, platform:macos |
| [#88115](https://github.com/anthropics/claude-code/issues/88115) | \[Security\] Assistant-generated text injected into USER message turn after advisor tool call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:security, area:tools, bug, platform:macos |
| [#87086](https://github.com/anthropics/claude-code/issues/87086) | \[EVAL/TRANSPARENCY\] Anthropic's regulation case rests on internal evals — apply the #86979 provenance standard to Glasswing and 'When AI Builds Itself' | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-16 | invalid |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86174](https://github.com/anthropics/claude-code/issues/86174) | \[BUG\] ListAgents/list-agents returns empty while team is alive — leadSessionId not re-bound after session resume/clear | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-12 | area:agents, bug, has repro, platform:linux, reproduced |
| [#85199](https://github.com/anthropics/claude-code/issues/85199) | \[BUG\]Claude Desktop repeatedly crashes and requires “Advanced Options → Repair” on Windows | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-09 | bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83705](https://github.com/anthropics/claude-code/issues/83705) | \[BUG\] Entering a background agent thread hangs when the session is parked in AskUserQuestion (attach guard checks only \`state\`, ignores \`tempo\`/\`block\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-04 | area:agents |
| [#83704](https://github.com/anthropics/claude-code/issues/83704) | \[BUG\] Desktop plugin stores desync: sessions load stale account-registry copies that shadow current CLI installs; settings Update checks the wrong store and Uninstall deletes from both | OPEN | security / trust boundary | 2026-08-20 | 2026-08-04 | area:desktop, area:plugins |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#83379](https://github.com/anthropics/claude-code/issues/83379) | Windows desktop app: message input becomes unfocusable mid-conversation; force-quit and hard reboot do not clear it (logout/login reported as fix) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-02 | area:desktop |
| [#83362](https://github.com/anthropics/claude-code/issues/83362) | ask permission rules are silently ignored in interactive sessions while deny rules from the same file are enforced | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-02 | area:permissions |
| [#83342](https://github.com/anthropics/claude-code/issues/83342) | Bundled ugrep balloons to 9–14 GB RSS compiling a bounded-interval BRE (plain grep is transparently routed to it) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-02 | area:tools |
| [#83332](https://github.com/anthropics/claude-code/issues/83332) | \[BUG\] Plan mode: second plan in the same session is not displayed — UI keeps showing the first plan (Claude Desktop) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-02 | area:desktop |
| [#83321](https://github.com/anthropics/claude-code/issues/83321) | Claude Desktop (Windows) recurring AppHang (Event ID 1002 MoAppHang) during background subagent dispatch — 7+ occurrences, no crash dump captured despite LocalDumps configured | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-02 | area:desktop |
| [#83318](https://github.com/anthropics/claude-code/issues/83318) | \[Windows\] GPU-process crash in Cowork preview bricks MSIX install (NeedsRemediation loop) → forced reinstall wipes local sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-02 | area:desktop |
| [#83225](https://github.com/anthropics/claude-code/issues/83225) | \[BUG/FEATURE\] Partial compaction ('Summarize up to here') is unusable from the desktop app: no UI for it, CLI-created summaries are ignored by the app, and the app's Rewind dialog is restore-only | OPEN | security / trust boundary | 2026-08-20 | 2026-08-02 | area:desktop |

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
