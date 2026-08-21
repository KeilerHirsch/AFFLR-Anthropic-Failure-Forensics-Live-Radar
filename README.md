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
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#79407](https://github.com/anthropics/claude-code/issues/79407) | \[BUG\] macOS: locked login keychain silently breaks auth — /login falsely reports "Login successful", and entering the password at the keychain prompts still leaves the session logged out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-20 | area:auth, bug, has repro, platform:macos, stale |
| [#78258](https://github.com/anthropics/claude-code/issues/78258) | \[Bug\] Claude 3.5 Sonnet safeguards falsely flag legitimate first-party VPN development and code review | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:model, bug, platform:macos, stale |
| [#73782](https://github.com/anthropics/claude-code/issues/73782) | \[Cloud sessions\] Regression between 2026-06-18 and 2026-06-25: GitHub REST passthrough returns 403 "GitHub access is not enabled for this session" for org repos despite Claude GitHub App installed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-03 | area:claude-code-web, area:networking, area:routines, bug, has repro, platform:web, regression, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#77291](https://github.com/anthropics/claude-code/issues/77291) | Model fabricates verbatim &lt;task-notification&gt; blocks with invented exit codes for background Bash tasks, then acts on them — reproduced 2/2 on 2.1.179 + 2.1.207 (sonnet-4-6); no harness guard | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:bash, area:model, bug, has repro, stale |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#73142](https://github.com/anthropics/claude-code/issues/73142) | \[Bug\]\[cyber\] False positive blocked reverse-engineering decompiled SDK flight commands (req\_011CccWXBLfLAd36tiBKwoue) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#73123](https://github.com/anthropics/claude-code/issues/73123) | \[Bug\]\[cyber\] Blocked reverse-engineering own drone's app protocol for FOSS ground station (req\_011CccTMDQ42jNFmptqRaq8h) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-28 | bug |
| [#80585](https://github.com/anthropics/claude-code/issues/80585) | \[BUG\] Multiple concurrent local sessions race on OAuth refresh-token rotation → near-daily forced /login | OPEN | security / trust boundary | 2026-08-21 | 2026-07-23 | stale |
| [#80496](https://github.com/anthropics/claude-code/issues/80496) | Interactive-only 401 "OAuth access token has expired" with valid setup-token on Team org with channelsEnabled — print mode works; DISABLE\_NONESSENTIAL\_TRAFFIC fixes it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-23 | stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#79407](https://github.com/anthropics/claude-code/issues/79407) | \[BUG\] macOS: locked login keychain silently breaks auth — /login falsely reports "Login successful", and entering the password at the keychain prompts still leaves the session logged out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-20 | area:auth, bug, has repro, platform:macos, stale |
| [#78258](https://github.com/anthropics/claude-code/issues/78258) | \[Bug\] Claude 3.5 Sonnet safeguards falsely flag legitimate first-party VPN development and code review | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:model, bug, platform:macos, stale |
| [#73782](https://github.com/anthropics/claude-code/issues/73782) | \[Cloud sessions\] Regression between 2026-06-18 and 2026-06-25: GitHub REST passthrough returns 403 "GitHub access is not enabled for this session" for org repos despite Claude GitHub App installed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-03 | area:claude-code-web, area:networking, area:routines, bug, has repro, platform:web, regression, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#77291](https://github.com/anthropics/claude-code/issues/77291) | Model fabricates verbatim &lt;task-notification&gt; blocks with invented exit codes for background Bash tasks, then acts on them — reproduced 2/2 on 2.1.179 + 2.1.207 (sonnet-4-6); no harness guard | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:bash, area:model, bug, has repro, stale |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#73142](https://github.com/anthropics/claude-code/issues/73142) | \[Bug\]\[cyber\] False positive blocked reverse-engineering decompiled SDK flight commands (req\_011CccWXBLfLAd36tiBKwoue) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#73123](https://github.com/anthropics/claude-code/issues/73123) | \[Bug\]\[cyber\] Blocked reverse-engineering own drone's app protocol for FOSS ground station (req\_011CccTMDQ42jNFmptqRaq8h) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-28 | bug |
| [#80496](https://github.com/anthropics/claude-code/issues/80496) | Interactive-only 401 "OAuth access token has expired" with valid setup-token on Team org with channelsEnabled — print mode works; DISABLE\_NONESSENTIAL\_TRAFFIC fixes it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-23 | stale |
| [#78368](https://github.com/anthropics/claude-code/issues/78368) | \[BUG\] Cowork: update retroactively invalidated custom Cowork files root; "Change location" then copied 12.87GB incl. credentials and git repo to world-readable /Library/Application Support/Claude | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-17 | area:cowork, area:security, bug, platform:macos, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88511](https://github.com/anthropics/claude-code/issues/88511) | Session list: show status (running / waiting for input) and open PRs | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | enhancement |
| [#88510](https://github.com/anthropics/claude-code/issues/88510) | Feature: Add cache hit rate fields to statusline input JSON | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:statusline, enhancement |
| [#88509](https://github.com/anthropics/claude-code/issues/88509) | \[Feature Request\] Add token direction field to subagent status line JSON | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:agent-view, area:statusline, enhancement, platform:linux |
| [#88508](https://github.com/anthropics/claude-code/issues/88508) | \[Bug\] Subagent status line JSON missing effort field for non-custom subagents | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:agents, area:statusline, bug, platform:linux |
| [#88507](https://github.com/anthropics/claude-code/issues/88507) | \[Bug\] Subagent status line JSON missing parent reference for nested subagent hierarchy | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:agents, area:statusline, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88506](https://github.com/anthropics/claude-code/issues/88506) | Windows desktop app dies repeatedly under Smart App Control: vk\_swiftshader.dll blocked because sideloaded MSIX ships no CodeIntegrity catalog | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, bug, has repro, platform:windows |
| [#88505](https://github.com/anthropics/claude-code/issues/88505) | \[BUG\] Identity verification flow excludes South Korea and blocks Claude Code with API Error 400 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:auth, bug, platform:windows |
| [#88504](https://github.com/anthropics/claude-code/issues/88504) | iOS Simulator panel crash-loops on macOS 27 beta: seatbelt profile denies Metal's new cache-dir writes | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:sandbox, bug, has repro, platform:macos |
| [#88503](https://github.com/anthropics/claude-code/issues/88503) | Idle notification gives no signal that a teammate's finished output still needs to be explicitly requested | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, enhancement, platform:macos |
| [#88502](https://github.com/anthropics/claude-code/issues/88502) | \[FEATURE\] Desktop: allow multiple simultaneous spellchecker languages | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, enhancement, platform:windows |
| [#88501](https://github.com/anthropics/claude-code/issues/88501) | Remote Control: a bridged session gives no indication of which machine is executing it — side effects land on an invisible host | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, area:ui, enhancement, platform:windows |
| [#88500](https://github.com/anthropics/claude-code/issues/88500) | \[BUG\] Windows MSIX: opening the sandboxed Browser pane bricks a working install when CoworkVMService is half-registered after auto-update (0x80073D28) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, area:installation, bug, platform:windows |
| [#88498](https://github.com/anthropics/claude-code/issues/88498) | \[FEATURE\] Detach the Browser pane into its own window (multi-monitor) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, area:ui, enhancement, platform:windows |
| [#88497](https://github.com/anthropics/claude-code/issues/88497) | \[Locked out — existing account routed to “Let’s create your account”, request human escalation | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, platform:macos |
| [#88496](https://github.com/anthropics/claude-code/issues/88496) | Cannot copy long assistant output from the terminal (works fine in other CLI tools, e.g. Google Antigravity CLI) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, duplicate, platform:linux |
| [#88495](https://github.com/anthropics/claude-code/issues/88495) | Feature request: read-aloud (TTS) for mobile Remote Control responses + screen-reader audit of the session view | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:a11y, enhancement |
| [#88494](https://github.com/anthropics/claude-code/issues/88494) | \[BUG\] AskUserQuestion: choosing "chat about it" erases the question and all its options from the transcript | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:tui, bug, has repro, platform:linux |
| [#88493](https://github.com/anthropics/claude-code/issues/88493) | \[BUG\] Remote Control: a prompt submitted on one machine is executed twice — the account's bridge environment runs it again on a second machine, with duplicated side effects | CLOSED / NOT\_PLANNED | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, bug, has repro, platform:windows |
| [#88492](https://github.com/anthropics/claude-code/issues/88492) | GitHub app install flow is a dead end for organization repos - the working route (github.com/apps/claude) is never mentioned | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug |
| [#88491](https://github.com/anthropics/claude-code/issues/88491) | /clear does not cancel a slash command queued behind it, and gives no warning | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cli, area:tui, bug |
| [#88490](https://github.com/anthropics/claude-code/issues/88490) | \[BUG\] Cloud Cowork sessions intermittently export OTLP with no identity attributes (user.email/account\_uuid/account\_id/organization.id) and a fresh per-session user.id | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:cowork, bug, has repro |
| [#88483](https://github.com/anthropics/claude-code/issues/88483) | \[BUG\] Desktop app never rebuilds its deferred-tool pool: tools/list\_changed and RefreshMcpTools are both no-ops (CLI 2.1.237 works with the identical server — carve-out from #66084) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, bug, has repro, platform:windows |
| [#88472](https://github.com/anthropics/claude-code/issues/88472) | \[MODEL\] Quite hard when you are working with a pentester because safeguards are always thrown while you just want to give him information or this kind of things when you want to make a plan | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, model, needs-repro |
| [#88463](https://github.com/anthropics/claude-code/issues/88463) | Artifact publish auto-arms a background "live updates" monitor with no opt-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:tools, enhancement |
| [#88462](https://github.com/anthropics/claude-code/issues/88462) | \[Data Loss\] Claude Code ran rm -rf on $HOME in auto mode — destructive code hidden inside a script the assistant wrote itself (5th report of this class) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:permissions, area:sandbox, bug, data-loss, high-priority, platform:wsl |

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
