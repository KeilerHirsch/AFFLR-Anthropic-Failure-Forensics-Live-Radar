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
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#23315](https://github.com/anthropics/claude-code/issues/23315) | 🐛 Bug: Claude Code charges users twice - API billing AND prepaid credits consumed simultaneously | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-02-05 | area:api, area:auth, area:cost, bug, stale |
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#69417](https://github.com/anthropics/claude-code/issues/69417) | claude.ai-synced connectors require /login every session — never persisted locally | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-18 | area:auth, area:mcp, bug, has repro, platform:macos |
| [#60613](https://github.com/anthropics/claude-code/issues/60613) | \[BUG\] Auto-mode classifier hard-blocks all mongosh invocations once a "prod"-named DB appears in context, even after user explicit authorization and switch to a separate database | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:permissions, bug, has repro, platform:macos, stale |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88553](https://github.com/anthropics/claude-code/issues/88553) | Sandbox network egress allowlist not consistently enforced (non-allowlisted hosts intermittently reachable) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:sandbox, area:security, duplicate, platform:macos |
| [#84323](https://github.com/anthropics/claude-code/issues/84323) | \[Feature Request\] Implement session token limit warnings and graceful degradation for multi-agent orchestration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-05 | area:agents |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#86140](https://github.com/anthropics/claude-code/issues/86140) | Cowork fails with VM service not running. The service failed to start. CoworkVMService never starts — packaged-service activation fails with ERROR\_INVALID\_PARAMETER (87) on Windows 11 25H2 (26200) - workaround found | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#23315](https://github.com/anthropics/claude-code/issues/23315) | 🐛 Bug: Claude Code charges users twice - API billing AND prepaid credits consumed simultaneously | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-02-05 | area:api, area:auth, area:cost, bug, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#53983](https://github.com/anthropics/claude-code/issues/53983) | Claude systematically claims migration/porting tasks complete when critical logic is dormant or missing | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-27 | area:agents, area:model, bug, stale |
| [#54682](https://github.com/anthropics/claude-code/issues/54682) | Opus 4.7 in autonomous mode: registers placeholder as completed, claims unverified deploys, fails to close — catastrophic for production work | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-29 | area:model, bug, platform:macos, stale |
| [#60395](https://github.com/anthropics/claude-code/issues/60395) | \[BUG\]  OAuth Token Exchange not completed in 2.1.143 with non-DCR AS (Cloudflare Access for SaaS) — server side curl-verified, regression suspected from 2.1.80 | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:auth, area:mcp, bug, has repro, platform:windows, stale |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-17 | area:model, bug |
| [#69417](https://github.com/anthropics/claude-code/issues/69417) | claude.ai-synced connectors require /login every session — never persisted locally | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-18 | area:auth, area:mcp, bug, has repro, platform:macos |
| [#60613](https://github.com/anthropics/claude-code/issues/60613) | \[BUG\] Auto-mode classifier hard-blocks all mongosh invocations once a "prod"-named DB appears in context, even after user explicit authorization and switch to a separate database | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-05-19 | area:permissions, bug, has repro, platform:macos, stale |
| [#86616](https://github.com/anthropics/claude-code/issues/86616) | macOS login keychain corrupted twice in 3 days (CSSMERR\_CSP\_INVALID\_DATA); corruption timing matches Claude Code credential writes under ~20 concurrent instances | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-14 | area:auth, bug, has repro, platform:macos |
| [#73120](https://github.com/anthropics/claude-code/issues/73120) | \[Bug\]\[cyber\] Safeguard blocked drone protocol reverse-engineering for FOSS ground control (req\_011CccTGmJJsqjDGWVZEokuA) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | api:anthropic, area:model, area:security, bug, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#73141](https://github.com/anthropics/claude-code/issues/73141) | \[Bug\]\[cyber\] Safety block halted legitimate reverse engineering of drone flight-controller commands (req\_011CccWVCDC6TrSVKtHBAUKK) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, duplicate, platform:linux, stale |
| [#73130](https://github.com/anthropics/claude-code/issues/73130) | \[Bug\]\[cyber\] Safety filter blocks message about building a personal ground control station tool for owned hard (req\_011CccTSF8NeF5hp4ncbpJhy) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#78253](https://github.com/anthropics/claude-code/issues/78253) | \[BUG\] Bash tool fails with spawn E2BIG — sandbox profile size scales with working-tree file count, gated by git-repo detection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-16 | area:sandbox, bug, has repro, platform:macos, stale |
| [#77293](https://github.com/anthropics/claude-code/issues/77293) | auto-mode permission classifier denies allowlisted calls (Agent, Bash(python3 \*)) with mismatched/stale reasoning | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-13 | area:agents, area:permissions, bug, has repro, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88553](https://github.com/anthropics/claude-code/issues/88553) | Sandbox network egress allowlist not consistently enforced (non-allowlisted hosts intermittently reachable) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:sandbox, area:security, duplicate, platform:macos |
| [#84323](https://github.com/anthropics/claude-code/issues/84323) | \[Feature Request\] Implement session token limit warnings and graceful degradation for multi-agent orchestration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-05 | area:agents |
| [#60360](https://github.com/anthropics/claude-code/issues/60360) | Model occasionally emits or fabricates \`Human:\` turns when woken by Monitor task-notifications with no fresh user input | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-05-18 | area:core, duplicate, platform:linux, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#88582](https://github.com/anthropics/claude-code/issues/88582) | \[BUG\] macOS: hostnames from /etc/hosts and /etc/resolver/\* fail with getaddrinfo ENOTFOUND while a VPN's DNS is active, breaking local HTTP MCP servers | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:mcp, area:networking, bug, has repro, platform:macos |
| [#88581](https://github.com/anthropics/claude-code/issues/88581) | You've hit your session limit · resets 7:10pm (America/Sao\_Paulo) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cost, duplicate, platform:windows |
| [#88580](https://github.com/anthropics/claude-code/issues/88580) | Subagent returns a description of its deliverable instead of the deliverable; work is unrecoverable (v2.1.238) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:agents, bug, platform:macos |
| [#88579](https://github.com/anthropics/claude-code/issues/88579) | Persistent memory: ships but is invisible, per-directory, and unverifiable — why a 91k-star third-party replacement exists | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | enhancement, memory |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88578](https://github.com/anthropics/claude-code/issues/88578) | \[BUG\] Windows hook commands with backslash paths silently never execute (bash eats the backslashes) — killed my memory hooks for 46 days | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:hooks, bug, has repro, platform:windows |
| [#88577](https://github.com/anthropics/claude-code/issues/88577) | Resuming a session re-arms the comment monitor for only one Artifact, though several are persisted as armed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:core, bug, platform:linux |
| [#88576](https://github.com/anthropics/claude-code/issues/88576) | macOS: versioned install paths invalidate TCC folder permissions on every auto-update (and mid-session for running sessions) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:packaging, bug, has repro, platform:macos |
| [#88575](https://github.com/anthropics/claude-code/issues/88575) | \[Bug\] Auto mode classifier denies MCP tool calls already in permissions allow list | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:mcp, area:permissions, bug, platform:macos |
| [#88574](https://github.com/anthropics/claude-code/issues/88574) | \[BUG\] Stale plan preview in claude desktop | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:macos |
| [#88573](https://github.com/anthropics/claude-code/issues/88573) | Add a bindable action to toggle the TUI renderer (fullscreen ↔ default) at runtime | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, enhancement, platform:macos |
| [#88572](https://github.com/anthropics/claude-code/issues/88572) | Generated commands don't match the user's known OS/shell (Bash emitted for Windows/PowerShell) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, area:model, bug, platform:vscode, platform:windows |
| [#88571](https://github.com/anthropics/claude-code/issues/88571) | Generated shell commands contain unreplaced &lt;placeholder&gt; tokens (pasted verbatim -&gt; broken/destructive runs) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:vscode, platform:windows |
| [#88570](https://github.com/anthropics/claude-code/issues/88570) | \[BUG\] "Out of usage credits" blocks chat while Plan usage limits panel shows headroom (Pro plan) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |
| [#88568](https://github.com/anthropics/claude-code/issues/88568) | \[BUG\] Desktop sessions with local file access have no memory tool at all — file access and the rules governing it are mutually exclusive | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, bug, memory, platform:macos |
| [#88567](https://github.com/anthropics/claude-code/issues/88567) | \[FEATURE\] Task-first sessions: infer the working directory instead of requiring it up front (Claude Desktop, local Code) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, area:ui, enhancement |
| [#88566](https://github.com/anthropics/claude-code/issues/88566) | \[BUG\] MCP Apps widgets never render in third-party (custom-3p) deployment mode — empty feature-flag payload disables the epitaxy MCP Apps gate | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:mcp, bug, platform:macos |
| [#88565](https://github.com/anthropics/claude-code/issues/88565) | \[BUG\] Auto mode silently disables path-scoped rules: it instructs the agent to edit files through Bash, and Bash edits never trigger rule injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, area:core, bug, has repro, platform:macos |
| [#88564](https://github.com/anthropics/claude-code/issues/88564) | \[FEATURE\] Settings schema validation failures should result in more fault-tolerant behavior | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:permissions, area:security, enhancement |
| [#88563](https://github.com/anthropics/claude-code/issues/88563) | Hooks: unrecognized keys (e.g. \`args\`) are dropped silently, and hook stdout reaches the terminal with control sequences intact | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:hooks, bug, platform:windows |
| [#88562](https://github.com/anthropics/claude-code/issues/88562) | \[BUG\] Code tab in Claude Desktop hangs on "Sending..." forever — embedded CLI, chat tab, auth and MCP all work in isolation (Windows) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88561](https://github.com/anthropics/claude-code/issues/88561) | Bash tool silently collapses \`\\\\\` to \`\\\` in command text, corrupting regex and paths | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, bug, has repro, platform:windows |
| [#88560](https://github.com/anthropics/claude-code/issues/88560) | \[BUG\] VS Code extension: chat panel blank on non-secure (HTTP) origins — unguarded crypto.randomUUID() in webview bundle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:ide, bug, has repro, platform:linux, platform:vscode |
| [#88558](https://github.com/anthropics/claude-code/issues/88558) | Claude in Chrome extension stuck "not connected" after working earlier in same   session | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:chrome, bug, platform:macos |
| [#88557](https://github.com/anthropics/claude-code/issues/88557) | \[BUG\] Plugin without "version" in its manifest records the enclosing git repo HEAD (~/.claude) as its version | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:plugins, bug, duplicate, platform:macos |

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
