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
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#88686](https://github.com/anthropics/claude-code/issues/88686) | \[Bug\]\[cyber\] False positive during inspection and theming of decoded Android keyboard package (req\_011CeE1nY9Cj8mFPXwharjsj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#74250](https://github.com/anthropics/claude-code/issues/74250) | MCP OAuth: parallel sessions sharing the credential store break refresh-token rotation (family revoked, all sessions forced to interactive re-auth) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-04 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#77402](https://github.com/anthropics/claude-code/issues/77402) | \[MODEL\] Opus 4.8 systemic failure in Claude Code — sustained hallucination spiral, context dropping, tool output loss | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-14 | area:model, area:tools, bug, model, platform:windows, stale |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#88685](https://github.com/anthropics/claude-code/issues/88685) | \[Bug\]\[cyber\] Inspecting decompiled Android keyboard APK resource XMLs and theme structure (req\_011CeE1kUrDAu69sb76YcsHV) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#81296](https://github.com/anthropics/claude-code/issues/81296) | Agent maintained ToS-violating automation for weeks, worsened the resulting bot-block, then misreported it as a login failure | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-26 | stale |
| [#81186](https://github.com/anthropics/claude-code/issues/81186) | \[BUG\] Native binary segfaults within ~2 seconds while nProtect GameGuard (Helldivers 2) is running — GameGuard module confirmed in crash stack | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#79849](https://github.com/anthropics/claude-code/issues/79849) | Remote MCP servers declaring completions/logging capabilities fail to connect despite valid initialize handshake | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-21 | stale |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |
| [#80878](https://github.com/anthropics/claude-code/issues/80878) | Agent scaled an unverified destructive fix to ~98% of a user's data, causing a Plex library collapse (classifier friction also noted) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80793](https://github.com/anthropics/claude-code/issues/80793) | \[BUG\] Opus 4.8 thinking-only end\_turn followed by fabricated tool and background-agent results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80340](https://github.com/anthropics/claude-code/issues/80340) | plugin install fails for git-subdir sources pinned to a commit SHA ("fatal: Remote branch &lt;sha&gt; not found in upstream origin") | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |
| [#80026](https://github.com/anthropics/claude-code/issues/80026) | \[BUG\] Chat mode: MCP tools/call never sent to server (tools/list works), Cowork and Code MCP unaffected | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | bug, stale |
| [#80292](https://github.com/anthropics/claude-code/issues/80292) | Multi-device Max subscription: refresh token invalidated hours after another device logs in (cross-device logout ping-pong, 2.1.217) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |
| [#80224](https://github.com/anthropics/claude-code/issues/80224) | \[BUG\] Claude Code: chain of avoidable errors — unverified links, unauthorized file changes, destructive sed, excessive token waste | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | bug, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#88686](https://github.com/anthropics/claude-code/issues/88686) | \[Bug\]\[cyber\] False positive during inspection and theming of decoded Android keyboard package (req\_011CeE1nY9Cj8mFPXwharjsj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#74250](https://github.com/anthropics/claude-code/issues/74250) | MCP OAuth: parallel sessions sharing the credential store break refresh-token rotation (family revoked, all sessions forced to interactive re-auth) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-04 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#77402](https://github.com/anthropics/claude-code/issues/77402) | \[MODEL\] Opus 4.8 systemic failure in Claude Code — sustained hallucination spiral, context dropping, tool output loss | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-14 | area:model, area:tools, bug, model, platform:windows, stale |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#88685](https://github.com/anthropics/claude-code/issues/88685) | \[Bug\]\[cyber\] Inspecting decompiled Android keyboard APK resource XMLs and theme structure (req\_011CeE1kUrDAu69sb76YcsHV) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#81296](https://github.com/anthropics/claude-code/issues/81296) | Agent maintained ToS-violating automation for weeks, worsened the resulting bot-block, then misreported it as a login failure | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-26 | stale |
| [#81186](https://github.com/anthropics/claude-code/issues/81186) | \[BUG\] Native binary segfaults within ~2 seconds while nProtect GameGuard (Helldivers 2) is running — GameGuard module confirmed in crash stack | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#79849](https://github.com/anthropics/claude-code/issues/79849) | Remote MCP servers declaring completions/logging capabilities fail to connect despite valid initialize handshake | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-21 | stale |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |
| [#80878](https://github.com/anthropics/claude-code/issues/80878) | Agent scaled an unverified destructive fix to ~98% of a user's data, causing a Plex library collapse (classifier friction also noted) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80793](https://github.com/anthropics/claude-code/issues/80793) | \[BUG\] Opus 4.8 thinking-only end\_turn followed by fabricated tool and background-agent results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80340](https://github.com/anthropics/claude-code/issues/80340) | plugin install fails for git-subdir sources pinned to a commit SHA ("fatal: Remote branch &lt;sha&gt; not found in upstream origin") | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |
| [#80026](https://github.com/anthropics/claude-code/issues/80026) | \[BUG\] Chat mode: MCP tools/call never sent to server (tools/list works), Cowork and Code MCP unaffected | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | bug, stale |
| [#80292](https://github.com/anthropics/claude-code/issues/80292) | Multi-device Max subscription: refresh token invalidated hours after another device logs in (cross-device logout ping-pong, 2.1.217) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |
| [#80224](https://github.com/anthropics/claude-code/issues/80224) | \[BUG\] Claude Code: chain of avoidable errors — unverified links, unauthorized file changes, destructive sed, excessive token waste | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | bug, stale |
| [#58952](https://github.com/anthropics/claude-code/issues/58952) | \[Tahoe 26.x\] terminal process tree EPERM in ~/Documents — root cause analysis &amp; data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-05-14 | area:sandbox, bug, platform:macos |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88750](https://github.com/anthropics/claude-code/issues/88750) | \[BUG\] Setting Model to claude-opus-4-8\[1m\] in VS Code Plugin Doesn't Save to Settings | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:ide, bug, platform:vscode, platform:windows |
| [#88749](https://github.com/anthropics/claude-code/issues/88749) | \[BUG\] Windows: GPU process crashes (exitCode 101457950) and app will not relaunch until Windows "Repair" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:desktop, bug, platform:windows |
| [#88748](https://github.com/anthropics/claude-code/issues/88748) | \[Bug\] Unrelated safeguarding triggers in non-technical document context | OPEN | observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:linux |
| [#88747](https://github.com/anthropics/claude-code/issues/88747) | Worktree creation writes an ABSOLUTE core.hooksPath into config.worktree, so worktrees run the MAIN checkout's hooks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tools, bug, has repro, platform:macos |
| [#88746](https://github.com/anthropics/claude-code/issues/88746) | \[Bug\] Agent repeatedly ignores corrections and produces mismatched outputs across conversation turns | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, area:tui, bug, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88745](https://github.com/anthropics/claude-code/issues/88745) | Remote Control: stuck 'Thinking…' indicator with no active tool calls | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:ui, bug |
| [#88744](https://github.com/anthropics/claude-code/issues/88744) | \[BUG\] Desktop Code tab: pane-header drag target for rearranging panes is ~1px tall, making custom layouts effectively unachievable (NOT the app window drag region) | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:desktop, area:ui, bug, has repro, platform:macos |
| [#88742](https://github.com/anthropics/claude-code/issues/88742) | A missed task-notification wake stalls an interactive session indefinitely | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:core, bug, has repro, platform:linux |
| [#88741](https://github.com/anthropics/claude-code/issues/88741) | SendMessage racing an agent's task stop strands the reply with no notification | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:agents, bug, has repro, platform:linux |
| [#88740](https://github.com/anthropics/claude-code/issues/88740) | Silent main-loop model fallback (Fable 5 → Opus 4.8): no notification, static identity line misleads the model, /model does not stick | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:macos |
| [#88739](https://github.com/anthropics/claude-code/issues/88739) | \[BUG\] SessionStart hook fires for sessions that never materialize (no transcript file is ever created) - side effects get attributed to a real, named session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:hooks, duplicate, has repro, platform:macos, platform:windows |
| [#88738](https://github.com/anthropics/claude-code/issues/88738) | PreToolUse hook silently stops firing mid-session and never recovers; concurrent session unaffected | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:hooks, bug, platform:vscode, platform:windows |
| [#88737](https://github.com/anthropics/claude-code/issues/88737) | \[Bug\] Excessive token consumption in iterative debugging loops | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:cost, area:model, bug, needs-repro, platform:macos |
| [#88736](https://github.com/anthropics/claude-code/issues/88736) | \[BUG\] Weekly usage bar exhausted in August with 30–45% LOWER token consumption than June (Max 20x) | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:cost, bug, platform:macos |
| [#88735](https://github.com/anthropics/claude-code/issues/88735) | Custom subagent registry silently caps at 3 (not documented), drops alphabetically-last entries with no load-time error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:agents, bug, platform:windows |
| [#88734](https://github.com/anthropics/claude-code/issues/88734) | \[BUG\] Persistent Monitor can survive as an orphan (parent dead, child running): the harness stops receiving its events while every liveness check still reports healthy | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, platform:windows |
| [#88733](https://github.com/anthropics/claude-code/issues/88733) | Google Drive MCP: read\_file\_content returns only the head post of each comment thread, not replies | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:mcp, enhancement |
| [#88732](https://github.com/anthropics/claude-code/issues/88732) | \[BUG\] /clear silently terminates persistent Monitor background tasks - the session loses its only wake mechanism and is never told | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tools, area:tui, bug, platform:windows |
| [#88731](https://github.com/anthropics/claude-code/issues/88731) | \[BUG\] Artifact tool absent in sessions spawned by \`claude remote-control\` (server mode); \`claude --remote-control\` works on the same machine and account | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:agent-sdk, area:tools, bug, platform:macos |
| [#88730](https://github.com/anthropics/claude-code/issues/88730) | \[Bug\]\[cyber\] Mobile OS partition building and bootloader flashing blocked mid-session (req\_011CeGvzkFj7mBffNufL9Mzk) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88729](https://github.com/anthropics/claude-code/issues/88729) | \[Bug\]\[cyber\] False positive while building custom OS images and flashing test devices (req\_011CeGvtV13DGrztLkbumLeG) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, area:security, bug, duplicate, platform:linux |
| [#88728](https://github.com/anthropics/claude-code/issues/88728) | \[Bug\]\[cyber\] OS partition image compilation and fastboot flashing verification blocked (req\_011CeGvkgAHFMmdyUX2RJeTc) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88727](https://github.com/anthropics/claude-code/issues/88727) | \[Bug\] MSIX installation failed with error code 0x80073CF6 on Windows 11 | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, area:installation, bug, platform:windows |
| [#88726](https://github.com/anthropics/claude-code/issues/88726) | Generated Chrome native-host wrapper pins a version path that the next update deletes | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:chrome, bug, has repro, platform:windows |
| [#88725](https://github.com/anthropics/claude-code/issues/88725) | remoteControlAtStartup not applied to sessions restored after Desktop app restart | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, bug, duplicate |

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
