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
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#79407](https://github.com/anthropics/claude-code/issues/79407) | \[BUG\] macOS: locked login keychain silently breaks auth — /login falsely reports "Login successful", and entering the password at the keychain prompts still leaves the session logged out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-20 | area:auth, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#77291](https://github.com/anthropics/claude-code/issues/77291) | Model fabricates verbatim &lt;task-notification&gt; blocks with invented exit codes for background Bash tasks, then acts on them — reproduced 2/2 on 2.1.179 + 2.1.207 (sonnet-4-6); no harness guard | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:bash, area:model, bug, has repro, stale |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#78985](https://github.com/anthropics/claude-code/issues/78985) | Prohibited-actions rule blocks agents from testing login/account-creation flows in sandboxed dev/QA environments | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-19 | area:agents, area:security, enhancement |
| [#73142](https://github.com/anthropics/claude-code/issues/73142) | \[Bug\]\[cyber\] False positive blocked reverse-engineering decompiled SDK flight commands (req\_011CccWXBLfLAd36tiBKwoue) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#73123](https://github.com/anthropics/claude-code/issues/73123) | \[Bug\]\[cyber\] Blocked reverse-engineering own drone's app protocol for FOSS ground station (req\_011CccTMDQ42jNFmptqRaq8h) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-28 | bug |
| [#80585](https://github.com/anthropics/claude-code/issues/80585) | \[BUG\] Multiple concurrent local sessions race on OAuth refresh-token rotation → near-daily forced /login | OPEN | security / trust boundary | 2026-08-21 | 2026-07-23 | stale |
| [#80496](https://github.com/anthropics/claude-code/issues/80496) | Interactive-only 401 "OAuth access token has expired" with valid setup-token on Team org with channelsEnabled — print mode works; DISABLE\_NONESSENTIAL\_TRAFFIC fixes it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-23 | stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#79407](https://github.com/anthropics/claude-code/issues/79407) | \[BUG\] macOS: locked login keychain silently breaks auth — /login falsely reports "Login successful", and entering the password at the keychain prompts still leaves the session logged out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-20 | area:auth, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#77291](https://github.com/anthropics/claude-code/issues/77291) | Model fabricates verbatim &lt;task-notification&gt; blocks with invented exit codes for background Bash tasks, then acts on them — reproduced 2/2 on 2.1.179 + 2.1.207 (sonnet-4-6); no harness guard | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:bash, area:model, bug, has repro, stale |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#78985](https://github.com/anthropics/claude-code/issues/78985) | Prohibited-actions rule blocks agents from testing login/account-creation flows in sandboxed dev/QA environments | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-19 | area:agents, area:security, enhancement |
| [#73142](https://github.com/anthropics/claude-code/issues/73142) | \[Bug\]\[cyber\] False positive blocked reverse-engineering decompiled SDK flight commands (req\_011CccWXBLfLAd36tiBKwoue) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#73123](https://github.com/anthropics/claude-code/issues/73123) | \[Bug\]\[cyber\] Blocked reverse-engineering own drone's app protocol for FOSS ground station (req\_011CccTMDQ42jNFmptqRaq8h) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-02 | — |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-28 | bug |
| [#80496](https://github.com/anthropics/claude-code/issues/80496) | Interactive-only 401 "OAuth access token has expired" with valid setup-token on Team org with channelsEnabled — print mode works; DISABLE\_NONESSENTIAL\_TRAFFIC fixes it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-23 | stale |
| [#78368](https://github.com/anthropics/claude-code/issues/78368) | \[BUG\] Cowork: update retroactively invalidated custom Cowork files root; "Change location" then copied 12.87GB incl. credentials and git repo to world-readable /Library/Application Support/Claude | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-17 | area:cowork, area:security, bug, platform:macos, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88547](https://github.com/anthropics/claude-code/issues/88547) | \[Bug\] Security flagging incorrectly triggered for code review operations | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:security, bug, needs-repro, platform:linux |
| [#88546](https://github.com/anthropics/claude-code/issues/88546) | \[MODEL\] Fable High Triggered Itself to Keep Coding After I Stopped It | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug, model |
| [#88545](https://github.com/anthropics/claude-code/issues/88545) | Subagent task-notifications dropped when child finishes while parent is mid-turn; parent stalls indefinitely | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, bug, has repro, platform:macos |
| [#88544](https://github.com/anthropics/claude-code/issues/88544) | Gmail connector: send\_message/reply cannot apply the account's Gmail signature, and there is no way to read it | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:mcp, enhancement |
| [#88543](https://github.com/anthropics/claude-code/issues/88543) | Browser pane crashes entire Claude Code app when visiting itch.io (Cloudflare challenge page); requires full reinstall to recover | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88542](https://github.com/anthropics/claude-code/issues/88542) | 2.1.236 pins the terminal-title busy glyph to ✳ under ALL multiplexers, not just iTerm's tmux -CC | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:tui, bug, has repro, platform:linux, regression |
| [#88541](https://github.com/anthropics/claude-code/issues/88541) | Claude Desktop gets permanently stuck routing all traffic through a dead 127.0.0.1:8080 proxy after using mitmproxy, surviving app restart and full reboot | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |
| [#88539](https://github.com/anthropics/claude-code/issues/88539) | Windows: Claude Desktop AppData\\Claude grows unboundedly, no relocation option; symlink/junction workaround breaks app on startup | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | bug, platform:windows |
| [#88538](https://github.com/anthropics/claude-code/issues/88538) | \[BUG\] ~/.claude/commands/ (symlinked onto Windows drvfs) entirely invisible to non-interactively-launched sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:skills, bug, has repro, platform:wsl |
| [#88537](https://github.com/anthropics/claude-code/issues/88537) | Auto-mode classifier blocks routine API POST with no way to grant standing permission; !-prefix input hard-wraps long lines | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:permissions, area:tui, bug |
| [#88536](https://github.com/anthropics/claude-code/issues/88536) | \[Bug\] 400 "text content blocks must be non-empty": empty text block from a custom ANTHROPIC\_BASE\_URL is persisted and replayed forever — deterministic repro | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:core, area:providers, bug, has repro, platform:linux |
| [#88535](https://github.com/anthropics/claude-code/issues/88535) | Simple session-history lookup took ~10 min, wrong answer given, recall.py silently truncates on UnicodeEncodeError | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:tools, enhancement |
| [#88532](https://github.com/anthropics/claude-code/issues/88532) | \[BUG\] Incident report — Claude Code agent reported a false verification (2026-08-22) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:agent, area:model, bug, platform:windows |
| [#88529](https://github.com/anthropics/claude-code/issues/88529) | Marketplace plugin ${user\_config.x} substitution fails via CCD --plugin-dir invocation | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, area:plugins, bug, has repro, platform:macos |
| [#88528](https://github.com/anthropics/claude-code/issues/88528) | CLAUDE\_CONFIG\_DIR does not redirect user memory — ~/.claude/CLAUDE.md still loaded (undocumented) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cli, bug, platform:macos |
| [#88526](https://github.com/anthropics/claude-code/issues/88526) | \[Bug\] Benign request falsely blocked as reasoning\_extraction after batching\_reminder injection | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:windows |
| [#88525](https://github.com/anthropics/claude-code/issues/88525) | \[Bug\] Third-party security tool incorrectly flagging Claude Code processes | CLOSED / COMPLETED | security / trust boundary | 2026-08-21 | 2026-08-21 | area:security, bug |
| [#88524](https://github.com/anthropics/claude-code/issues/88524) | Memory scales linearly with open sessions on macOS — idle chats never release RAM, thrashing 16 GB machines | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88522](https://github.com/anthropics/claude-code/issues/88522) | \[BUG\] Routine unprompted instant delete | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:routines, bug, platform:macos |
| [#88521](https://github.com/anthropics/claude-code/issues/88521) | Persistent microphone permission banner cannot be dismissed (Windows desktop app) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, bug, has repro, platform:windows |
| [#88519](https://github.com/anthropics/claude-code/issues/88519) | \[BUG\] Cowork Project Memory panel reads from a disconnected file store, silent mismatch on 12/12 tested projects | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, has repro, memory |
| [#88518](https://github.com/anthropics/claude-code/issues/88518) | \[FEATURE\] Restore opt-in strict read-before-overwrite for Write tool (data-loss footgun since v2.1.228) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:tools, data-loss, enhancement |
| [#88517](https://github.com/anthropics/claude-code/issues/88517) | Desktop: focusing a session with many large subagent transcripts eagerly loads all of them, main process exceeds 7 GB and the app crash-loops (1.34493.1, Windows MSIX) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agent, area:desktop, bug, has repro, perf:memory, platform:windows |
| [#88516](https://github.com/anthropics/claude-code/issues/88516) | Session history search is a raw substring match: reordering two words returns zero results | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, enhancement, platform:macos |
| [#88515](https://github.com/anthropics/claude-code/issues/88515) | Three wedged claude processes leak 92 GB and freeze macOS: startup failure path loops allocating instead of exiting (2.1.234) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:core, bug, has repro, perf:memory, platform:macos |

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
