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
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
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
| [#72373](https://github.com/anthropics/claude-code/issues/72373) | \[Bug\]\[cyber\] Safety block prevents writing or reviewing code that reads drone telemetry sensor data (req\_011CcYR3zvFDq6wKPwZEMFur) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72358](https://github.com/anthropics/claude-code/issues/72358) | \[Bug\]\[cyber\] False cyber block while building drone flight UI with live video, telemetry, and connection-statu (req\_011CcYLSQEyq2CeAsBAgK4Pz) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, platform:linux |
| [#72351](https://github.com/anthropics/claude-code/issues/72351) | \[Bug\]\[cyber\] Cyber filter blocked building a drone flight UI with live video feed and telemetry HUD (req\_011CcYJWT9EjGMeSaqybt7TC) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72328](https://github.com/anthropics/claude-code/issues/72328) | \[Bug\]\[cyber\] Safety block interrupts legitimate security vulnerability analysis workflow (req\_011CcY1o5TFLzNFaV7gPUFGo) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72326](https://github.com/anthropics/claude-code/issues/72326) | \[Bug\]\[cyber\] Safety filter blocks legitimate cybersecurity topic assistance in Claude Code session (req\_011CcY1kqamR8G6sW1fDj6zF) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72318](https://github.com/anthropics/claude-code/issues/72318) | \[Bug\]\[cyber\] Safety block halted reverse-engineering USB AOA accessory framing for a drone controller app (req\_011CcXzbthv6diNEz89koBkH) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#75210](https://github.com/anthropics/claude-code/issues/75210) | \[Bug\]\[cyber\] Safety block halted authorized reverse-engineering of my own drone's auth protocol, mid-secret-re (req\_011CcnReWU19UF1bg7REcCRy) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, area:security, bug, duplicate, platform:linux |
| [#75187](https://github.com/anthropics/claude-code/issues/75187) | \[Bug\]\[cyber\] Safety filter blocked routine analysis of RSA-SHA256 key material extracted from own memory dump (req\_011CcnJ2yHjMz3YQrqvLefKo) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, platform:linux |
| [#75104](https://github.com/anthropics/claude-code/issues/75104) | \[Bug\]\[cyber\] False-positive block on rooted-device SELinux/dev-mode setup for the user's own Android phone (req\_011CcmzvbxgnDzowZjuRR3rJ) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-07 | area:model, bug, duplicate, platform:linux |
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
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
| [#72373](https://github.com/anthropics/claude-code/issues/72373) | \[Bug\]\[cyber\] Safety block prevents writing or reviewing code that reads drone telemetry sensor data (req\_011CcYR3zvFDq6wKPwZEMFur) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72358](https://github.com/anthropics/claude-code/issues/72358) | \[Bug\]\[cyber\] False cyber block while building drone flight UI with live video, telemetry, and connection-statu (req\_011CcYLSQEyq2CeAsBAgK4Pz) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, platform:linux |
| [#72351](https://github.com/anthropics/claude-code/issues/72351) | \[Bug\]\[cyber\] Cyber filter blocked building a drone flight UI with live video feed and telemetry HUD (req\_011CcYJWT9EjGMeSaqybt7TC) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72328](https://github.com/anthropics/claude-code/issues/72328) | \[Bug\]\[cyber\] Safety block interrupts legitimate security vulnerability analysis workflow (req\_011CcY1o5TFLzNFaV7gPUFGo) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72350](https://github.com/anthropics/claude-code/issues/72350) | \[Bug\]\[cyber\] Safety block halted routine GUI work on a drone telemetry/video ground-station HUD (req\_011CcYJUCfHYwm1Zzc8uwssh) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, bug, duplicate, platform:linux |
| [#72326](https://github.com/anthropics/claude-code/issues/72326) | \[Bug\]\[cyber\] Safety filter blocks legitimate cybersecurity topic assistance in Claude Code session (req\_011CcY1kqamR8G6sW1fDj6zF) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72318](https://github.com/anthropics/claude-code/issues/72318) | \[Bug\]\[cyber\] Safety block halted reverse-engineering USB AOA accessory framing for a drone controller app (req\_011CcXzbthv6diNEz89koBkH) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-29 | area:model, area:security, bug, duplicate, platform:linux |
| [#72076](https://github.com/anthropics/claude-code/issues/72076) | \[Bug\]\[cyber\] Blocked asking whether firmware downgrade removes proprietary whitebox blob (req\_011CcVsoCiNTcFRUPRhMtxmG) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#72073](https://github.com/anthropics/claude-code/issues/72073) | \[Bug\]\[cyber\] Safety block interrupts legitimate white-box AES reverse engineering on own hardware (req\_011CcV53T1GpzRkDfcT8LA98) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-28 | area:model, area:security, bug, duplicate, platform:linux |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88598](https://github.com/anthropics/claude-code/issues/88598) | \[FEATURE\] Desktop app: show the GitHub issue as a footer chip next to the PR chip (statusLine and footerLinksRegexes are silently inert) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88597](https://github.com/anthropics/claude-code/issues/88597) | \[BUG\] Transcript loader silently discards all but one conversation branch on resume, losing delivered assistant messages | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:core, bug, data-loss, has repro, platform:vscode, platform:windows, regression |
| [#88596](https://github.com/anthropics/claude-code/issues/88596) | \[BUG\] iTerm2: Cmd+Click on a TUI link opens two browser tabs — terminal and TUI each open it once (a split, not a duplicate click event) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:tui, bug, has repro, platform:macos |
| [#88595](https://github.com/anthropics/claude-code/issues/88595) | \[BUG\] ultrareview: CLI declares cloud review failed at 30 min while it is still running; free attempt consumed, findings never delivered to CLI | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cli, bug, platform:macos |
| [#88594](https://github.com/anthropics/claude-code/issues/88594) | \[BUG\] Custom remote MCP connector - all tools show "Auto-Allow disabled by your admin" in routine, despite org-wide Always Allow | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cowork, area:mcp, area:permissions, area:routines, bug, platform:web |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88592](https://github.com/anthropics/claude-code/issues/88592) | Custom \`agent\` setting suppresses the output-style body in the system prompt | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, bug, has repro, platform:macos |
| [#88591](https://github.com/anthropics/claude-code/issues/88591) | \[BUG\] Ctrl+V image paste deterministically crashes CLI — Bun 1.4.0 SIGBUS at 0xBAD4007 on macOS 26.5 (any image, 3/3 repro) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:tui, bug, has repro, platform:macos |
| [#88590](https://github.com/anthropics/claude-code/issues/88590) | Local managed-settings allowedChannelPlugins silently discarded when remote org settings omit the key (still on 2.1.234; variant of #79290) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:permissions, area:plugins, bug, has repro, platform:windows |
| [#88589](https://github.com/anthropics/claude-code/issues/88589) | \[Bug\] False positive cyber safeguard classification on authorized security audit skill | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, duplicate, platform:windows |
| [#88588](https://github.com/anthropics/claude-code/issues/88588) | \[Bug\] SafeGuard falsely triggering on all agent requests | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, duplicate, platform:windows |
| [#88587](https://github.com/anthropics/claude-code/issues/88587) | \[Bug\] /resume command output not executable in same terminal session | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug, platform:macos |
| [#88586](https://github.com/anthropics/claude-code/issues/88586) | \[BUG\] Windows x64: "Restart to update" cannot restart — Notification Area instance holds the single-instance lock (ref #42776) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#88577](https://github.com/anthropics/claude-code/issues/88577) | Resuming a session re-arms the comment monitor for only one Artifact, though several are persisted as armed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:core, bug, platform:linux |
| [#88571](https://github.com/anthropics/claude-code/issues/88571) | Generated shell commands contain unreplaced &lt;placeholder&gt; tokens (pasted verbatim -&gt; broken/destructive runs) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:vscode, platform:windows |
| [#88564](https://github.com/anthropics/claude-code/issues/88564) | \[FEATURE\] Settings schema validation failures should result in more fault-tolerant behavior | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:permissions, area:security, enhancement |
| [#88546](https://github.com/anthropics/claude-code/issues/88546) | \[MODEL\] Fable High Triggered Itself to Keep Coding After I Stopped It | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug, model |
| [#88545](https://github.com/anthropics/claude-code/issues/88545) | Subagent task-notifications dropped when child finishes while parent is mid-turn; parent stalls indefinitely | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, bug, has repro, platform:macos |
| [#88538](https://github.com/anthropics/claude-code/issues/88538) | \[BUG\] ~/.claude/commands/ (symlinked onto Windows drvfs) entirely invisible to non-interactively-launched sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:skills, bug, has repro, platform:wsl |
| [#88522](https://github.com/anthropics/claude-code/issues/88522) | \[BUG\] Routine unprompted instant delete | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:routines, bug, platform:macos |
| [#88521](https://github.com/anthropics/claude-code/issues/88521) | Persistent microphone permission banner cannot be dismissed (Windows desktop app) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, bug, has repro, platform:windows |
| [#88519](https://github.com/anthropics/claude-code/issues/88519) | \[BUG\] Cowork Project Memory panel reads from a disconnected file store, silent mismatch on 12/12 tested projects | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, has repro, memory |
| [#88518](https://github.com/anthropics/claude-code/issues/88518) | \[FEATURE\] Restore opt-in strict read-before-overwrite for Write tool (data-loss footgun since v2.1.228) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:tools, data-loss, enhancement |
| [#88515](https://github.com/anthropics/claude-code/issues/88515) | Three wedged claude processes leak 92 GB and freeze macOS: startup failure path loops allocating instead of exiting (2.1.234) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, has repro, perf:memory, platform:macos |
| [#88514](https://github.com/anthropics/claude-code/issues/88514) | \[BUG\] Claude Desktop leaks stdio MCP server processes when a renderer releases its port | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |

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
