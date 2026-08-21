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
| [#88655](https://github.com/anthropics/claude-code/issues/88655) | \[Bug\]\[cyber\] Mobile app location permission and playback logging implementation (req\_011Ce4yAiLMkyBBnw2B21Mev) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, duplicate, platform:linux |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, reproduced |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88655](https://github.com/anthropics/claude-code/issues/88655) | \[Bug\]\[cyber\] Mobile app location permission and playback logging implementation (req\_011Ce4yAiLMkyBBnw2B21Mev) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, duplicate, platform:linux |
| [#88648](https://github.com/anthropics/claude-code/issues/88648) | Opus 4.8 (1M context) fabricated an entire user turn during an unattended scheduled run, acted on it autonomously, then insisted the fabricated text was the user's own words | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, reproduced |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88678](https://github.com/anthropics/claude-code/issues/88678) | \[FEATURE\] Remotely initiate and control NEW Claude Code sessions on REGISTERED DEVICES | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | enhancement |
| [#88676](https://github.com/anthropics/claude-code/issues/88676) | \[Bug\]\[cyber\] Browser-based WebUSB firmware installer and device flashing tool (req\_011CeDvnkehEQBAGFfoAbBXD) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88675](https://github.com/anthropics/claude-code/issues/88675) | \[Bug\]\[cyber\] False positive during mobile OS lockscreen and user profile UI development (req\_011CeDur165RTpPmYPetfoZm) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88674](https://github.com/anthropics/claude-code/issues/88674) | \[Bug\]\[cyber\] False positive on customizing open-source mobile OS lockscreen and user profiles (req\_011CeDuoVH8v6CTRQcMGURey) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88673](https://github.com/anthropics/claude-code/issues/88673) | \[BUG\] Desktop app corrupted after silent "stealth update" — recurring "app is corrupt, needs repair" errors | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88672](https://github.com/anthropics/claude-code/issues/88672) | \[Bug\]\[cyber\] False positive analyzing Android boot animation media and system properties (req\_011CeDm22HEzxGmA3EJKg1KL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88671](https://github.com/anthropics/claude-code/issues/88671) | Sessions cannot introspect themselves: no way to read the current session's id, title, branch, or linked PR | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:core, enhancement, platform:macos |
| [#88670](https://github.com/anthropics/claude-code/issues/88670) | MCP UI widgets remount on session re-entry, stealing scroll/focus — and the only opt-out is losing the connector's tools | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, area:ui, bug, platform:macos |
| [#88669](https://github.com/anthropics/claude-code/issues/88669) | \[Bug\]\[cyber\] False positive while building custom OS images and configuring verified boot (req\_011CeDcJRtx64QziTUqB67DE) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88668](https://github.com/anthropics/claude-code/issues/88668) | \[Bug\]\[cyber\] False positive during OS signing key audit and test certificate hardening (req\_011CeDa5r5QL2AWzDbVGC99S) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88667](https://github.com/anthropics/claude-code/issues/88667) | \[Desktop/Windows\] Built-in Browser pane loading a Cloudflare challenge page crashes the GPU process and hangs the whole app; reinstall wipes claude-code-sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, duplicate, platform:windows |
| [#88666](https://github.com/anthropics/claude-code/issues/88666) | \[Bug\]\[cyber\] Block on asking to review and harden a build signing chain (req\_011CeDZtfVred9GScVBeGUu6) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88665](https://github.com/anthropics/claude-code/issues/88665) | \[Bug\]\[cyber\] Blocked while troubleshooting device sleep mode and media playback failure (req\_011Ce6xtHZeWiU1TZkNX4aZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#88664](https://github.com/anthropics/claude-code/issues/88664) | A marketplace catalog refresh disables an installed plugin when the catalog's newer version adds a dependency | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:plugins, bug, has repro, platform:macos |
| [#88663](https://github.com/anthropics/claude-code/issues/88663) | claude plugin update does not resolve newly-declared plugin dependencies (install does) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:plugins, bug, has repro, platform:macos |
| [#88661](https://github.com/anthropics/claude-code/issues/88661) | \[Bug\]\[cyber\] Firmware bytecode analysis and device lock debugging blocked on user exclamation (req\_011Ce5YL6TxvgJnuhsSoGfZN) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:linux |
| [#88660](https://github.com/anthropics/claude-code/issues/88660) | Background-job sessions lack macOS Keychain/Security.framework access | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agent-view, area:auth, bug, duplicate, platform:macos |
| [#88659](https://github.com/anthropics/claude-code/issues/88659) | Gateway model discovery pricing is ignored by /usage | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:api, area:cost, enhancement, platform:macos |
| [#88658](https://github.com/anthropics/claude-code/issues/88658) | \[Bug\]\[cyber\] False positive during Android firmware analysis for hardware switch handling (req\_011Ce5SMouAq7oggPYJS9eTa) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:linux |
| [#88656](https://github.com/anthropics/claude-code/issues/88656) | \[Bug\]\[cyber\] Android framework bytecode disassembly for hardware key lock debugging (req\_011Ce5SL4TidBKpqKQ1iCwWi) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88655](https://github.com/anthropics/claude-code/issues/88655) | \[Bug\]\[cyber\] Mobile app location permission and playback logging implementation (req\_011Ce4yAiLMkyBBnw2B21Mev) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, duplicate, platform:linux |
| [#88654](https://github.com/anthropics/claude-code/issues/88654) | \[Bug\]\[cyber\] Android package rebuild troubleshooting and Bluetooth remote input development (req\_011Ce3qvuFj6YSoAhGf2nCAU) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:linux |
| [#88653](https://github.com/anthropics/claude-code/issues/88653) | \[Bug\]\[cyber\] False positive on mapping browsing architecture in decompiled application (req\_011Ce3n2iFdrKH43D3H6G7ar) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88652](https://github.com/anthropics/claude-code/issues/88652) | \[Bug\]\[cyber\] False positive on uploading image assets for a website review update (req\_011Ce3gPv4vpPbGxrsYUVLYP) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:linux |
| [#88651](https://github.com/anthropics/claude-code/issues/88651) | \[Bug\]\[cyber\] Safeguard triggered when uploading image assets for a website review update (req\_011Ce3gFATMjdda5SpCR8DUx) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |

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
