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
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, reproduced |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#88589](https://github.com/anthropics/claude-code/issues/88589) | \[Bug\] False positive cyber safeguard classification on authorized security audit skill | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:windows |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88605](https://github.com/anthropics/claude-code/issues/88605) | \[Bug\] Exit cleanup recursively deletes $HOME instead of session directory | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, data-loss, has repro, high-priority, platform:linux |
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, reproduced |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux |
| [#88589](https://github.com/anthropics/claude-code/issues/88589) | \[Bug\] False positive cyber safeguard classification on authorized security audit skill | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:windows |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88642](https://github.com/anthropics/claude-code/issues/88642) | \[Bug\]\[cyber\] False positive during Android widget UI modification and smali inspection (req\_011Ce26PGCu5HorbXineRam1) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88641](https://github.com/anthropics/claude-code/issues/88641) | \[Bug\]\[cyber\] ClAudit false-positive while: “check the test net logs. Its been up all day. done 4 fw upda…” (req\_011Ce26NXzdzGDX8DLU5NHiR) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88640](https://github.com/anthropics/claude-code/issues/88640) | \[BUG\] Cowork: Project memory reaches Local sessions but not Cloud sessions — silently, and the docs contradict each other | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, documentation, has repro |
| [#88639](https://github.com/anthropics/claude-code/issues/88639) | \[Bug\]\[cyber\] False positive while modifying Android widget UI assets and layout resources (req\_011Ce26MFhqDC8XWyN7Tx8nj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88638](https://github.com/anthropics/claude-code/issues/88638) | \[BUG\] Scheduled tasks evaluate their cron in the timezone they were armed in, while catch-up uses the current one | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:routines, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88637](https://github.com/anthropics/claude-code/issues/88637) | Bug: Claude for Chrome no completa la autorización (TypeError: Cannot convert a Symbol value to a string) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:chrome, area:cowork, bug, platform:windows |
| [#88636](https://github.com/anthropics/claude-code/issues/88636) | Desktop: archiving a session mid-turn kills its worker instantly with no confirmation — and leaves no interruption marker in the transcript | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, area:ui, enhancement, platform:macos |
| [#88635](https://github.com/anthropics/claude-code/issues/88635) | \[Bug\]\[cyber\] ClAudit false-positive while: “F••• YOU…” (req\_011Ce1L9qwesKZPazQax6CEo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:linux |
| [#88634](https://github.com/anthropics/claude-code/issues/88634) | CLAUDE.md "main session must not write code" rule is not enforced — no hook prevents direct Write/Edit of code files | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:hooks, enhancement, platform:windows |
| [#88633](https://github.com/anthropics/claude-code/issues/88633) | \[Bug\]\[cyber\] False positive while cloning repository for local source code audit (req\_011CdyFQ8AXBNXfaU9PLBoGQ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88632](https://github.com/anthropics/claude-code/issues/88632) | \[BUG\] Cowork Windows: Local environment cannot attach ANY Project — "Projects can't be included in sessions that run on this computer" (macOS unaffected, identical app version) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:cowork, bug, has repro, platform:windows |
| [#88631](https://github.com/anthropics/claude-code/issues/88631) | \[Bug\]\[cyber\] Android widget UI modification editing layout resources and smali bytecode (req\_011Ce26G7QczHGHBvXnVLqb9) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, duplicate, platform:linux |
| [#88629](https://github.com/anthropics/claude-code/issues/88629) | \[Bug\]\[cyber\] Editing decompiled Android widget layout resources to add media control button (req\_011Ce25wcEvvstAg81rKpEaL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#88628](https://github.com/anthropics/claude-code/issues/88628) | \[BUG\] Org repos not visible in Claude Code web/desktop repo picker despite valid gh token and SSO authorization | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, area:claude-code-web, duplicate |
| [#88626](https://github.com/anthropics/claude-code/issues/88626) | \[Bug\]\[cyber\] ClAudit false-positive while: “waht?…” (req\_011Ce25eJQuEeeQPJvWu7tJp) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:linux |
| [#88625](https://github.com/anthropics/claude-code/issues/88625) | Bootstrapping capabilities of Claude Code - can an agent modify its own toolchain? | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:tools, question |
| [#88624](https://github.com/anthropics/claude-code/issues/88624) | \[Bug\]\[cyber\] Decompiling local device UI package to customize media playback button (req\_011Ce255QPuQbJxu32SpuCXY) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:linux |
| [#88623](https://github.com/anthropics/claude-code/issues/88623) | \[Bug\]\[cyber\] Disassembling Android bytecode to inspect USB DAC mode configuration (req\_011Ce24Hkve8qyJvJqY9K1gJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:linux |
| [#88622](https://github.com/anthropics/claude-code/issues/88622) | \[FEATURE\] Claude Desktop: show sub-agent activity (tool calls, commands, results) in the task panel and session history | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:agents, area:desktop, area:ui, enhancement |
| [#88621](https://github.com/anthropics/claude-code/issues/88621) | \[BUG\] Claude Desktop: finished sub-agent tasks show "No output captured." although the transcript exists on disk | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agent-view, area:desktop, bug, has repro, platform:macos |
| [#88620](https://github.com/anthropics/claude-code/issues/88620) | \[Bug\]\[cyber\] ClAudit false-positive while: “Explore the Android app at /home/\[USER\]/Documents/GitHub/Alp…” (req\_011Ce212ZQq6GtYMZVt34ASD) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, duplicate, platform:linux |
| [#88619](https://github.com/anthropics/claude-code/issues/88619) | \[Bug\]\[cyber\] False positive during Android device pairing and audio DAC testing over ADB (req\_011Ce1xo8fCymVoVHLoXCmPz) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88618](https://github.com/anthropics/claude-code/issues/88618) | \[Bug\]\[cyber\] False positive configuring mobile app ADB connection to external hardware (req\_011Ce1xfC86WbCCcgM1BaZjz) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88617](https://github.com/anthropics/claude-code/issues/88617) | \[Bug\] Anthropic API Error: Repeated API errors preventing command execution | OPEN | observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:tui, bug, platform:windows |
| [#88616](https://github.com/anthropics/claude-code/issues/88616) | \[Bug\]\[cyber\] ClAudit false-positive while: “WHAT THE FUCLK!…” (req\_011Ce1nfb54WajbdYEaRdF9R) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, duplicate, platform:linux |

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
