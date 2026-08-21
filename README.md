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
| [#88686](https://github.com/anthropics/claude-code/issues/88686) | \[Bug\]\[cyber\] False positive during inspection and theming of decoded Android keyboard package (req\_011CeE1nY9Cj8mFPXwharjsj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#74250](https://github.com/anthropics/claude-code/issues/74250) | MCP OAuth: parallel sessions sharing the credential store break refresh-token rotation (family revoked, all sessions forced to interactive re-auth) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-04 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#77402](https://github.com/anthropics/claude-code/issues/77402) | \[MODEL\] Opus 4.8 systemic failure in Claude Code — sustained hallucination spiral, context dropping, tool output loss | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-14 | area:model, area:tools, bug, model, platform:windows, stale |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88685](https://github.com/anthropics/claude-code/issues/88685) | \[Bug\]\[cyber\] Inspecting decompiled Android keyboard APK resource XMLs and theme structure (req\_011CeE1kUrDAu69sb76YcsHV) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#81296](https://github.com/anthropics/claude-code/issues/81296) | Agent maintained ToS-violating automation for weeks, worsened the resulting bot-block, then misreported it as a login failure | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-26 | stale |
| [#81186](https://github.com/anthropics/claude-code/issues/81186) | \[BUG\] Native binary segfaults within ~2 seconds while nProtect GameGuard (Helldivers 2) is running — GameGuard module confirmed in crash stack | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#79849](https://github.com/anthropics/claude-code/issues/79849) | Remote MCP servers declaring completions/logging capabilities fail to connect despite valid initialize handshake | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-21 | stale |
| [#81172](https://github.com/anthropics/claude-code/issues/81172) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |
| [#80878](https://github.com/anthropics/claude-code/issues/80878) | Agent scaled an unverified destructive fix to ~98% of a user's data, causing a Plex library collapse (classifier friction also noted) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80793](https://github.com/anthropics/claude-code/issues/80793) | \[BUG\] Opus 4.8 thinking-only end\_turn followed by fabricated tool and background-agent results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80340](https://github.com/anthropics/claude-code/issues/80340) | plugin install fails for git-subdir sources pinned to a commit SHA ("fatal: Remote branch &lt;sha&gt; not found in upstream origin") | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88686](https://github.com/anthropics/claude-code/issues/88686) | \[Bug\]\[cyber\] False positive during inspection and theming of decoded Android keyboard package (req\_011CeE1nY9Cj8mFPXwharjsj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#74250](https://github.com/anthropics/claude-code/issues/74250) | MCP OAuth: parallel sessions sharing the credential store break refresh-token rotation (family revoked, all sessions forced to interactive re-auth) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-04 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#77402](https://github.com/anthropics/claude-code/issues/77402) | \[MODEL\] Opus 4.8 systemic failure in Claude Code — sustained hallucination spiral, context dropping, tool output loss | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-14 | area:model, area:tools, bug, model, platform:windows, stale |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88685](https://github.com/anthropics/claude-code/issues/88685) | \[Bug\]\[cyber\] Inspecting decompiled Android keyboard APK resource XMLs and theme structure (req\_011CeE1kUrDAu69sb76YcsHV) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#81296](https://github.com/anthropics/claude-code/issues/81296) | Agent maintained ToS-violating automation for weeks, worsened the resulting bot-block, then misreported it as a login failure | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-26 | stale |
| [#81186](https://github.com/anthropics/claude-code/issues/81186) | \[BUG\] Native binary segfaults within ~2 seconds while nProtect GameGuard (Helldivers 2) is running — GameGuard module confirmed in crash stack | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#79849](https://github.com/anthropics/claude-code/issues/79849) | Remote MCP servers declaring completions/logging capabilities fail to connect despite valid initialize handshake | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-21 | stale |
| [#81172](https://github.com/anthropics/claude-code/issues/81172) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-25 | bug, stale |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |
| [#80878](https://github.com/anthropics/claude-code/issues/80878) | Agent scaled an unverified destructive fix to ~98% of a user's data, causing a Plex library collapse (classifier friction also noted) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80793](https://github.com/anthropics/claude-code/issues/80793) | \[BUG\] Opus 4.8 thinking-only end\_turn followed by fabricated tool and background-agent results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |
| [#80340](https://github.com/anthropics/claude-code/issues/80340) | plugin install fails for git-subdir sources pinned to a commit SHA ("fatal: Remote branch &lt;sha&gt; not found in upstream origin") | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | stale |
| [#80026](https://github.com/anthropics/claude-code/issues/80026) | \[BUG\] Chat mode: MCP tools/call never sent to server (tools/list works), Cowork and Code MCP unaffected | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-22 | bug, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88694](https://github.com/anthropics/claude-code/issues/88694) | \[Bug\]\[cyber\] Android fastboot recovery and Boot Control Block wipe troubleshooting (req\_011CeEzfZaDTAu5YVWEye1C6) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88693](https://github.com/anthropics/claude-code/issues/88693) | \[Bug\]\[cyber\] Custom Android OS configuration and device debugging blocked (req\_011CeEf87YDsrpbYCySt8G5M) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88692](https://github.com/anthropics/claude-code/issues/88692) | \[BUG\] Windows: reinstall regenerates the \`ant-did\` device identity but preserves \`remoteToolsDeviceName\`, permanently orphaning existing Claude Code sessions ("Can't reach your computer") | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, bug, has repro, platform:windows |
| [#88691](https://github.com/anthropics/claude-code/issues/88691) | \[BUG\] \[Cowork\] "Record a skill": trajectory built and consumed by renderer, but the task session receives no demonstration — no proposal generated, capture never persisted to disk | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, area:skills, bug, data-loss, platform:macos |
| [#88690](https://github.com/anthropics/claude-code/issues/88690) | \[Bug\]\[cyber\] False positive during vendor access revocation and DNS record updates (req\_011CeEe1vKFi4iTAMBWLp4D7) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88689](https://github.com/anthropics/claude-code/issues/88689) | \[BUG\] Windows MSIX: Repair and Reset can never succeed — the installer registers the package from \`%TEMP%\\Claude-\*.msix\`, which is later deleted (0x80073CF0 / 0x80070002) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, duplicate, platform:windows |
| [#88688](https://github.com/anthropics/claude-code/issues/88688) | \[Bug\]\[cyber\] Block triggered during routine access control revocation and domain redirection (req\_011CeEdFgKQoGKAK5CRmFVAq) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88687](https://github.com/anthropics/claude-code/issues/88687) | \[Bug\]\[cyber\] False positive on local documentation review during user frustration (req\_011CeEZCtrAsxnDCz2TFG7Pg) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#88686](https://github.com/anthropics/claude-code/issues/88686) | \[Bug\]\[cyber\] False positive during inspection and theming of decoded Android keyboard package (req\_011CeE1nY9Cj8mFPXwharjsj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88685](https://github.com/anthropics/claude-code/issues/88685) | \[Bug\]\[cyber\] Inspecting decompiled Android keyboard APK resource XMLs and theme structure (req\_011CeE1kUrDAu69sb76YcsHV) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88684](https://github.com/anthropics/claude-code/issues/88684) | \[Bug\]\[cyber\] ClAudit false-positive while: “our repo will need PII stripped and replaced with setup and …” (req\_011CeDy1bGyuqeLe8z3M4RmC) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88683](https://github.com/anthropics/claude-code/issues/88683) | \[Bug\]\[cyber\] Android firmware image rebuild and device rooting for boot audio debugging (req\_011CeGcW64SuZGmcT9xgJSXp) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88682](https://github.com/anthropics/claude-code/issues/88682) | \[Bug\]\[cyber\] False positive during application binary build and staging deployment (req\_011CeGPdaQwyBwTQQ5sWBBVQ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88681](https://github.com/anthropics/claude-code/issues/88681) | \[Bug\]\[cyber\] False positive during Android partition recovery and bootloop troubleshooting (req\_011CeEzgRFBvbqHEqsy2xaCM) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88671](https://github.com/anthropics/claude-code/issues/88671) | Sessions cannot introspect themselves: no way to read the current session's id, title, branch, or linked PR | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:core, enhancement, platform:macos |
| [#88664](https://github.com/anthropics/claude-code/issues/88664) | A marketplace catalog refresh disables an installed plugin when the catalog's newer version adds a dependency | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:plugins, bug, has repro, platform:macos |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88646](https://github.com/anthropics/claude-code/issues/88646) | MessageDisplay: two non-overlapping hooks sometimes both render, sometimes only one does, and no race/order model found so far explains it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:hooks, bug, has repro, platform:macos |
| [#88636](https://github.com/anthropics/claude-code/issues/88636) | Desktop: archiving a session mid-turn kills its worker instantly with no confirmation — and leaves no interruption marker in the transcript | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, area:ui, enhancement, platform:macos |
| [#88621](https://github.com/anthropics/claude-code/issues/88621) | \[BUG\] Claude Desktop: finished sub-agent tasks show "No output captured." although the transcript exists on disk | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agent-view, area:desktop, bug, has repro, platform:macos |
| [#88611](https://github.com/anthropics/claude-code/issues/88611) | \[Bug\]\[cyber\] False positive while analyzing local packet captures during device firmware update (req\_011Ce1J4t6WgbqX3FKCWz9Ta) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#88607](https://github.com/anthropics/claude-code/issues/88607) | \[BUG\] Interrupted sign-in with a different email orphans the desktop app's entire Code session store; sessions appear permanently deleted while transcripts remain intact on disk | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, area:desktop, bug, platform:macos |
| [#88606](https://github.com/anthropics/claude-code/issues/88606) | \`/ultrareview\` results become permanently unrecoverable once the task ID expires | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:cost, area:skills, bug, has repro |
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#88602](https://github.com/anthropics/claude-code/issues/88602) | Completed background/remote-agent task output can't be re-fetched once the task ID expires | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:agent, bug |

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
