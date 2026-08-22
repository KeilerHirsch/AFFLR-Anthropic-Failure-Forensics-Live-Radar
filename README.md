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
| [#88730](https://github.com/anthropics/claude-code/issues/88730) | \[Bug\]\[cyber\] Mobile OS partition building and bootloader flashing blocked mid-session (req\_011CeGvzkFj7mBffNufL9Mzk) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88729](https://github.com/anthropics/claude-code/issues/88729) | \[Bug\]\[cyber\] False positive while building custom OS images and flashing test devices (req\_011CeGvtV13DGrztLkbumLeG) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, area:security, bug, duplicate, platform:linux |
| [#88728](https://github.com/anthropics/claude-code/issues/88728) | \[Bug\]\[cyber\] OS partition image compilation and fastboot flashing verification blocked (req\_011CeGvkgAHFMmdyUX2RJeTc) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88727](https://github.com/anthropics/claude-code/issues/88727) | \[Bug\] MSIX installation failed with error code 0x80073CF6 on Windows 11 | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, area:installation, bug, platform:windows |
| [#88726](https://github.com/anthropics/claude-code/issues/88726) | Generated Chrome native-host wrapper pins a version path that the next update deletes | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:chrome, bug, has repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88725](https://github.com/anthropics/claude-code/issues/88725) | remoteControlAtStartup not applied to sessions restored after Desktop app restart | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, bug, duplicate |
| [#88724](https://github.com/anthropics/claude-code/issues/88724) | \[Bug\]\[cyber\] Session blocked during crypto security audit documentation cleanup (req\_011CeGudDMfUNwhKvQMMwzu6) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, duplicate, platform:linux |
| [#88723](https://github.com/anthropics/claude-code/issues/88723) | \[Bug\]\[cyber\] Blocked while copy-editing a forensic audit report on a vendor connector (req\_011CeGtzKfeKWGwHKcntC3JU) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#88722](https://github.com/anthropics/claude-code/issues/88722) | Model pathologized an autistic user's verification requests as "paranoia" and "obsessive" | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug |
| [#88721](https://github.com/anthropics/claude-code/issues/88721) | \[FEATURE\] Add a setting to hide the "Jump to bottom" scroll hint | OPEN | observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:tui, enhancement |
| [#88720](https://github.com/anthropics/claude-code/issues/88720) | \[Bug\]\[cyber\] ClAudit false-positive while: “In the repo /home/\[USER\]/Documents/GitHub/m500, the Miku Mus…” (req\_011CeGsbEsA4Jer6uPwwW9At) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88719](https://github.com/anthropics/claude-code/issues/88719) | \[BUG\] Claude Desktop 1.34493.1.0 (Windows 11, MSIX) — silent crashes, minidumps written but zero log output | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | invalid |
| [#88718](https://github.com/anthropics/claude-code/issues/88718) | \[Bug\]\[cyber\] False positive while inspecting framework audio routing and DAC playback logic (req\_011CeGsarrqNcHos6vSt46hk) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88717](https://github.com/anthropics/claude-code/issues/88717) | \[BUG\] Voice hold mode: resuming push-to-talk submits the partial prompt — key auto-repeat satisfies the 300 ms submit double-tap | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tui, bug, has repro, platform:macos |
| [#88716](https://github.com/anthropics/claude-code/issues/88716) | Workflow approval handler rejects scripts by total size, independent of line length ("hidden control characters" false positive) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:tools, bug, has repro, platform:windows |
| [#88714](https://github.com/anthropics/claude-code/issues/88714) | \[Bug\] Content Router Incorrectly Flags Application Process Isolation as Cybersecurity | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:linux |
| [#88713](https://github.com/anthropics/claude-code/issues/88713) | \[BUG\] GitHub connector authorized but write operations fail with "403 Resource not accessible by integration | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:claude-code-web, area:integrations, area:mcp, bug, platform:windows |
| [#88712](https://github.com/anthropics/claude-code/issues/88712) | \[Bug\] Mobile push notifications not delivered despite successful server confirmation | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | bug, platform:windows |
| [#88710](https://github.com/anthropics/claude-code/issues/88710) | Claude Design preview: artifact comments can't anchor to design elements — anchors collapse to editor-chrome selectors | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:skills, bug, platform:macos, platform:vscode |
| [#88708](https://github.com/anthropics/claude-code/issues/88708) | Docs: sandbox settings reload live mid-session but are omitted from "When edits take effect" | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:sandbox, documentation, enhancement |
| [#88707](https://github.com/anthropics/claude-code/issues/88707) | Recall-driven confidence led to an unverified package recommendation | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:macos |
| [#88705](https://github.com/anthropics/claude-code/issues/88705) | Sidebar session list repeatedly goes empty despite session data being intact | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:macos |
| [#88704](https://github.com/anthropics/claude-code/issues/88704) | \[FEATURE\] Custom connectors: support static request headers (e.g. \`Authorization: Bearer …\`) — currently OAuth-only, forcing \`mcp-remote\` stdio shims | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, enhancement |
| [#88703](https://github.com/anthropics/claude-code/issues/88703) | \[Bug\]\[cyber\] False positive during Android firmware audio HAL analysis and UI debugging (req\_011CeGhmNpWS5qRYGP6J2tfu) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88702](https://github.com/anthropics/claude-code/issues/88702) | Bash run\_in\_background ignores \`timeout\` and a never-exiting background task produces no notification | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, area:tools, bug, has repro, platform:macos |

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
