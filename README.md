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
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#23315](https://github.com/anthropics/claude-code/issues/23315) | 🐛 Bug: Claude Code charges users twice - API billing AND prepaid credits consumed simultaneously | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-02-05 | area:api, area:auth, area:cost, bug, stale |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#69417](https://github.com/anthropics/claude-code/issues/69417) | claude.ai-synced connectors require /login every session — never persisted locally | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-18 | area:auth, area:mcp, bug, has repro, platform:macos |
| [#60613](https://github.com/anthropics/claude-code/issues/60613) | \[BUG\] Auto-mode classifier hard-blocks all mongosh invocations once a "prod"-named DB appears in context, even after user explicit authorization and switch to a separate database | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:permissions, bug, has repro, platform:macos, stale |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88553](https://github.com/anthropics/claude-code/issues/88553) | Sandbox network egress allowlist not consistently enforced (non-allowlisted hosts intermittently reachable) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:sandbox, area:security, duplicate, platform:macos |
| [#84323](https://github.com/anthropics/claude-code/issues/84323) | \[Feature Request\] Implement session token limit warnings and graceful degradation for multi-agent orchestration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-05 | area:agents |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#23315](https://github.com/anthropics/claude-code/issues/23315) | 🐛 Bug: Claude Code charges users twice - API billing AND prepaid credits consumed simultaneously | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-02-05 | area:api, area:auth, area:cost, bug, stale |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#69417](https://github.com/anthropics/claude-code/issues/69417) | claude.ai-synced connectors require /login every session — never persisted locally | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-18 | area:auth, area:mcp, bug, has repro, platform:macos |
| [#60613](https://github.com/anthropics/claude-code/issues/60613) | \[BUG\] Auto-mode classifier hard-blocks all mongosh invocations once a "prod"-named DB appears in context, even after user explicit authorization and switch to a separate database | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:permissions, bug, has repro, platform:macos, stale |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73116](https://github.com/anthropics/claude-code/issues/73116) | \[Bug\]\[cyber\] Safeguard blocked routine defensive security+correctness review of a Go web backend (req\_011CccTHmJLRT3jGTh3mDp4k) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73121](https://github.com/anthropics/claude-code/issues/73121) | \[Bug\]\[cyber\] Safety filter blocked drone protocol study for a personal FOSS ground station (req\_011CccTJXknEJAy8jdAvRWLY) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73092](https://github.com/anthropics/claude-code/issues/73092) | \[Bug\]\[cyber\] ClAudit false-positive in com — req\_011CccPcEJL4sgctVez1tPaW | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88553](https://github.com/anthropics/claude-code/issues/88553) | Sandbox network egress allowlist not consistently enforced (non-allowlisted hosts intermittently reachable) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:sandbox, area:security, duplicate, platform:macos |
| [#84323](https://github.com/anthropics/claude-code/issues/84323) | \[Feature Request\] Implement session token limit warnings and graceful degradation for multi-agent orchestration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-05 | area:agents |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88564](https://github.com/anthropics/claude-code/issues/88564) | \[FEATURE\] Settings schema validation failures should result in more fault-tolerant behavior | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:permissions, area:security, enhancement |
| [#88563](https://github.com/anthropics/claude-code/issues/88563) | Hooks: unrecognized keys (e.g. \`args\`) are dropped silently, and hook stdout reaches the terminal with control sequences intact | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:hooks, bug, platform:windows |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88561](https://github.com/anthropics/claude-code/issues/88561) | Bash tool silently collapses \`\\\\\` to \`\\\` in command text, corrupting regex and paths | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, bug, has repro, platform:windows |
| [#88560](https://github.com/anthropics/claude-code/issues/88560) | \[BUG\] VS Code extension: chat panel blank on non-secure (HTTP) origins — unguarded crypto.randomUUID() in webview bundle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:ide, bug, has repro, platform:linux, platform:vscode |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88558](https://github.com/anthropics/claude-code/issues/88558) | Claude in Chrome extension stuck "not connected" after working earlier in same   session | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:chrome, bug, platform:macos |
| [#88557](https://github.com/anthropics/claude-code/issues/88557) | \[BUG\] Plugin without "version" in its manifest records the enclosing git repo HEAD (~/.claude) as its version | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:plugins, bug, duplicate, platform:macos |
| [#88556](https://github.com/anthropics/claude-code/issues/88556) | Custom subagents fail to register after cold start when settings.local.json grows very large (348KB / 2438 valid permission entries) -- fixed by removing the file | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:permissions, bug, has repro, platform:windows |
| [#88555](https://github.com/anthropics/claude-code/issues/88555) | \[Bug\] Claude Code loses context after API failures and denies error occurrence | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:core, area:model, bug, platform:macos |
| [#88554](https://github.com/anthropics/claude-code/issues/88554) | \[Feature Request\] Implement answer-first response discipline and require explicit permission for actions outside local scope | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:permissions, enhancement, user-experience |
| [#88553](https://github.com/anthropics/claude-code/issues/88553) | Sandbox network egress allowlist not consistently enforced (non-allowlisted hosts intermittently reachable) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:sandbox, area:security, duplicate, platform:macos |
| [#88552](https://github.com/anthropics/claude-code/issues/88552) | \[Bug\] Incorrect reasoning extraction from non-Claude Code context | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:macos |
| [#88551](https://github.com/anthropics/claude-code/issues/88551) | \[BUG\] : Routine is not working properly in Claude Paid version | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:routines, bug, platform:web |
| [#88550](https://github.com/anthropics/claude-code/issues/88550) | Worktree isolation guard rejects any command using a tilde that passed through a shell variable | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, bug, has repro, platform:macos |
| [#88548](https://github.com/anthropics/claude-code/issues/88548) | \[BUG\] Issue sweep applies lifecycle deadlines unevenly — sweep.ts pages by position through a list it reorders | OPEN / REOPENED | security / trust boundary | 2026-08-21 | 2026-08-21 | bug |
| [#88547](https://github.com/anthropics/claude-code/issues/88547) | \[Bug\] Security flagging incorrectly triggered for code review operations | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:security, bug, needs-repro, platform:linux |
| [#88546](https://github.com/anthropics/claude-code/issues/88546) | \[MODEL\] Fable High Triggered Itself to Keep Coding After I Stopped It | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug, model |
| [#88545](https://github.com/anthropics/claude-code/issues/88545) | Subagent task-notifications dropped when child finishes while parent is mid-turn; parent stalls indefinitely | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, bug, has repro, platform:macos |
| [#88541](https://github.com/anthropics/claude-code/issues/88541) | Claude Desktop gets permanently stuck routing all traffic through a dead 127.0.0.1:8080 proxy after using mitmproxy, surviving app restart and full reboot | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |
| [#88538](https://github.com/anthropics/claude-code/issues/88538) | \[BUG\] ~/.claude/commands/ (symlinked onto Windows drvfs) entirely invisible to non-interactively-launched sessions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:skills, bug, has repro, platform:wsl |
| [#88537](https://github.com/anthropics/claude-code/issues/88537) | Auto-mode classifier blocks routine API POST with no way to grant standing permission; !-prefix input hard-wraps long lines | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:permissions, area:tui, bug |
| [#88526](https://github.com/anthropics/claude-code/issues/88526) | \[Bug\] Benign request falsely blocked as reasoning\_extraction after batching\_reminder injection | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, duplicate, platform:windows |
| [#88525](https://github.com/anthropics/claude-code/issues/88525) | \[Bug\] Third-party security tool incorrectly flagging Claude Code processes | CLOSED / COMPLETED | security / trust boundary | 2026-08-21 | 2026-08-21 | area:security, bug |
| [#88524](https://github.com/anthropics/claude-code/issues/88524) | Memory scales linearly with open sessions on macOS — idle chats never release RAM, thrashing 16 GB machines | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | — |
| [#88522](https://github.com/anthropics/claude-code/issues/88522) | \[BUG\] Routine unprompted instant delete | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:routines, bug, platform:macos |

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
