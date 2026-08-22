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
| [#88837](https://github.com/anthropics/claude-code/issues/88837) | \[MODEL\] CRITICAL PERMISSION BYPASS: Claude manufactures its own execution authority from a document it wrote, overrides an explicit in-context user prohibition, and runs unapproved privileged commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:permissions, area:security, bug, has repro, model, platform:linux, platform:vscode |
| [#54922](https://github.com/anthropics/claude-code/issues/54922) | \[Bug\] Remote Control session approval dropped, agent wedges indefinitely | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-30 | area:permissions, bug, has repro, platform:linux, stale |
| [#69649](https://github.com/anthropics/claude-code/issues/69649) | Connected HTTP MCP server's tools never appear in tool registry (ToolSearch) even after full app restart | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-06-19 | area:mcp, bug, has repro, platform:linux, platform:vscode |
| [#69581](https://github.com/anthropics/claude-code/issues/69581) | Injected, self-referential instructions appear inside Edit/Read tool results (twice, reproducible) — overlaps with #31447 / #49484 | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-06-19 | area:security, area:tools, bug, platform:wsl |
| [#88815](https://github.com/anthropics/claude-code/issues/88815) | \[MODEL\] Stated rules do not constrain subsequent behavior — with 2.5 months of session data | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:core, area:model, bug, model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88811](https://github.com/anthropics/claude-code/issues/88811) | \[Bug\]\[cyber\] False positive on source code security audit for secrets and injection flaws (req\_011CeHkQQYxDgGvYxjD1HFZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88806](https://github.com/anthropics/claude-code/issues/88806) | \[Bug\]\[cyber\] False positive on rotating hardcoded secret keys and updating signing certs (req\_011CeHjhJdNEc6SsqcmHyCSv) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#56119](https://github.com/anthropics/claude-code/issues/56119) | MCP Plugin Security: Systemic Risks Identified Through Plugin Investigation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-05-04 | area:mcp, area:plugins, area:security, enhancement, platform:macos, stale |
| [#60561](https://github.com/anthropics/claude-code/issues/60561) | CLAUDE\_CODE\_PROJECT\_DIR env var silently ignored — session JSONL still writes to in-tree .claude/projects/ (CLI 2.1.144, Windows) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-05-19 | area:cli, bug, platform:windows, stale |
| [#88807](https://github.com/anthropics/claude-code/issues/88807) | \[Bug\]\[cyber\] Rotating hardcoded application secrets and configuring certificate signing (req\_011CeHjrvsx8rQGQahiGpnPn) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81574](https://github.com/anthropics/claude-code/issues/81574) | \[BUG\] Windows: recurring forced logouts since ~Jul 22 — .credentials.json overwritten with test-fixture content ("fixture-claude-secret-value-x") | OPEN | security / trust boundary | 2026-08-22 | 2026-07-27 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#79948](https://github.com/anthropics/claude-code/issues/79948) | I double-dog-dare you: build the project-management layer Claude Code is missing — because I am tired of doing it for you, and I am WORN | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-21 | stale |
| [#88790](https://github.com/anthropics/claude-code/issues/88790) | \[FEATURE\] AskUserQuestion tool result cannot be distinguished from a genuine human response | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:agents, area:permissions, area:security, enhancement |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |
| [#88565](https://github.com/anthropics/claude-code/issues/88565) | \[BUG\] Auto mode silently disables path-scoped rules: it instructs the agent to edit files through Bash, and Bash edits never trigger rule injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-21 | area:bash, area:core, bug, has repro, platform:macos |
| [#60835](https://github.com/anthropics/claude-code/issues/60835) | \[MODEL\] Tests written by Claude wrote to production shared infrastructure (NAS) without isolation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-05-20 | area:model, bug, has repro, model, platform:macos, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88837](https://github.com/anthropics/claude-code/issues/88837) | \[MODEL\] CRITICAL PERMISSION BYPASS: Claude manufactures its own execution authority from a document it wrote, overrides an explicit in-context user prohibition, and runs unapproved privileged commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:permissions, area:security, bug, has repro, model, platform:linux, platform:vscode |
| [#54922](https://github.com/anthropics/claude-code/issues/54922) | \[Bug\] Remote Control session approval dropped, agent wedges indefinitely | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-30 | area:permissions, bug, has repro, platform:linux, stale |
| [#69649](https://github.com/anthropics/claude-code/issues/69649) | Connected HTTP MCP server's tools never appear in tool registry (ToolSearch) even after full app restart | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-06-19 | area:mcp, bug, has repro, platform:linux, platform:vscode |
| [#69581](https://github.com/anthropics/claude-code/issues/69581) | Injected, self-referential instructions appear inside Edit/Read tool results (twice, reproducible) — overlaps with #31447 / #49484 | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-06-19 | area:security, area:tools, bug, platform:wsl |
| [#88815](https://github.com/anthropics/claude-code/issues/88815) | \[MODEL\] Stated rules do not constrain subsequent behavior — with 2.5 months of session data | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:core, area:model, bug, model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88811](https://github.com/anthropics/claude-code/issues/88811) | \[Bug\]\[cyber\] False positive on source code security audit for secrets and injection flaws (req\_011CeHkQQYxDgGvYxjD1HFZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88806](https://github.com/anthropics/claude-code/issues/88806) | \[Bug\]\[cyber\] False positive on rotating hardcoded secret keys and updating signing certs (req\_011CeHjhJdNEc6SsqcmHyCSv) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#56119](https://github.com/anthropics/claude-code/issues/56119) | MCP Plugin Security: Systemic Risks Identified Through Plugin Investigation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-05-04 | area:mcp, area:plugins, area:security, enhancement, platform:macos, stale |
| [#60561](https://github.com/anthropics/claude-code/issues/60561) | CLAUDE\_CODE\_PROJECT\_DIR env var silently ignored — session JSONL still writes to in-tree .claude/projects/ (CLI 2.1.144, Windows) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-05-19 | area:cli, bug, platform:windows, stale |
| [#88807](https://github.com/anthropics/claude-code/issues/88807) | \[Bug\]\[cyber\] Rotating hardcoded application secrets and configuring certificate signing (req\_011CeHjrvsx8rQGQahiGpnPn) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#79948](https://github.com/anthropics/claude-code/issues/79948) | I double-dog-dare you: build the project-management layer Claude Code is missing — because I am tired of doing it for you, and I am WORN | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-21 | stale |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |
| [#88565](https://github.com/anthropics/claude-code/issues/88565) | \[BUG\] Auto mode silently disables path-scoped rules: it instructs the agent to edit files through Bash, and Bash edits never trigger rule injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-21 | area:bash, area:core, bug, has repro, platform:macos |
| [#60835](https://github.com/anthropics/claude-code/issues/60835) | \[MODEL\] Tests written by Claude wrote to production shared infrastructure (NAS) without isolation | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-05-20 | area:model, bug, has repro, model, platform:macos, stale |
| [#57164](https://github.com/anthropics/claude-code/issues/57164) | \[BUG\] Google OAuth login redirects to onboarding for existing Max subscriber, browser and desktop locked out while phone and CLI sessions remain authenticated | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-05-08 | area:auth, bug, platform:macos, stale |
| [#50516](https://github.com/anthropics/claude-code/issues/50516) | Allow opting out of the per-Read "malware" system-reminder — defense is porous and cost is non-consensual | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-18 | area:security, area:tools, enhancement, platform:macos, stale |
| [#88824](https://github.com/anthropics/claude-code/issues/88824) | \[BUG\] Desktop app: elevated-auth re-login navigates to /new and destroys the prompt being typed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:auth, area:desktop, bug, data-loss, has repro, platform:linux |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88849](https://github.com/anthropics/claude-code/issues/88849) | Agent tool: passing \`name:\` creates a teammate that never runs its prompt and never reports back | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#88848](https://github.com/anthropics/claude-code/issues/88848) | \[BUG\] Desktop: sessions sharing a working tree show each other's PRs in the PR tracker | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:agent-view, area:desktop, bug, has repro, platform:linux |
| [#88846](https://github.com/anthropics/claude-code/issues/88846) | /rename does not propagate to how the session appears in ListAgents on peer sessions | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:agent-view, bug, platform:linux |
| [#88845](https://github.com/anthropics/claude-code/issues/88845) | \[BUG\] /rename name survives into the pre-/clear conversation, so peers see the wrong session name | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:agent-view, area:core, bug, has repro, platform:macos |
| [#88842](https://github.com/anthropics/claude-code/issues/88842) | \[BUG\] \`effortLevel: "high"\` in settings.json but requests are sent at \`low\` — local terminal, no Remote Control; session transcript records \`high\` | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:core, bug, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88841](https://github.com/anthropics/claude-code/issues/88841) | \[Feature Request\] Add token cost visibility and guardrails for subagent fork context inheritance | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:agents, area:cost, enhancement, platform:windows |
| [#88840](https://github.com/anthropics/claude-code/issues/88840) | \`claude remote-control --permission-mode\` is silently ignored (plus: held cross-session messages have no approval surface) | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:permissions, bug, has repro, platform:macos |
| [#88839](https://github.com/anthropics/claude-code/issues/88839) | AskUserQuestion option picker is unusable with NVDA screen reader | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:a11y, area:tui, bug, platform:windows |
| [#88838](https://github.com/anthropics/claude-code/issues/88838) | \[BUG\] Two plugins can claim the same skill name and both install silently — and it ships in a real config today | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:plugins, area:skills, bug, has repro, platform:linux |
| [#88837](https://github.com/anthropics/claude-code/issues/88837) | \[MODEL\] CRITICAL PERMISSION BYPASS: Claude manufactures its own execution authority from a document it wrote, overrides an explicit in-context user prohibition, and runs unapproved privileged commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:permissions, area:security, bug, has repro, model, platform:linux, platform:vscode |
| [#88836](https://github.com/anthropics/claude-code/issues/88836) | AskUserQuestion option descriptions: newlines replaced with U+FFFD since 2.1.235 (regression, last good 2.1.234) | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:tui, bug, has repro, platform:macos, regression |
| [#88835](https://github.com/anthropics/claude-code/issues/88835) | \[BUG\] Desktop SSH connections fail when ~/.ssh is an iCloud Drive symlink — spawned ssh/ssh-keygen can't read known\_hosts or config | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:desktop, bug, has repro, platform:macos |
| [#88834](https://github.com/anthropics/claude-code/issues/88834) | \[BUG\] Claude installer fails with timeout | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:installation, bug, platform:linux |
| [#88833](https://github.com/anthropics/claude-code/issues/88833) | \[Bug\] Agentic reasoning fails on multi-step iOS development tasks—six exchanges to open simulator with stale state | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:macos |
| [#88832](https://github.com/anthropics/claude-code/issues/88832) | \[Bug\] Tool sandboxing feature flagged as policy violation | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, needs-repro, platform:linux |
| [#88831](https://github.com/anthropics/claude-code/issues/88831) | Custom MCP OAuth connector: token exchange succeeds server-side, connector never becomes 'Connected' | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:auth, area:mcp, bug |
| [#88830](https://github.com/anthropics/claude-code/issues/88830) | Hook execution failures are invisible in the desktop app and carry zero diagnostics (hook\_non\_blocking\_error attachments with empty content) | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:desktop, area:hooks, bug, has repro, platform:macos |
| [#88829](https://github.com/anthropics/claude-code/issues/88829) | \[Bug\] False positive in security/cypher detection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:security, bug, needs-repro, platform:macos |
| [#88828](https://github.com/anthropics/claude-code/issues/88828) | \[MODEL\] Claude Code pushed to git without waiting for user confirmation despite instructions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, bug, model |
| [#88827](https://github.com/anthropics/claude-code/issues/88827) | \[BUG\] Claude in Chrome: "Could not verify this site's safety category" blocks all sites, including claude.ai (persists after reinstall) | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:browser-extension, area:chrome, bug, platform:macos |
| [#88825](https://github.com/anthropics/claude-code/issues/88825) | \[BUG\] Cloud routines stall before their first turn: 'Claude Code process started', then no init, no result - while other routines on the same environment run green | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:routines, bug, platform:web |
| [#88824](https://github.com/anthropics/claude-code/issues/88824) | \[BUG\] Desktop app: elevated-auth re-login navigates to /new and destroys the prompt being typed | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:auth, area:desktop, bug, data-loss, has repro, platform:linux |
| [#88823](https://github.com/anthropics/claude-code/issues/88823) | \[BUG\] VS Code extension: Session History empty / generic "Claude Code" title, despite valid .jsonl files with resolvable titles on disk — non-deterministic over time | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:ide, bug, platform:vscode, platform:windows |
| [#88820](https://github.com/anthropics/claude-code/issues/88820) | \[BUG\] runtime segfault at non-canonical address 0xFFFFFFFFFFFFFFFF kills the CLI mid-session (Windows, v2.1.239) | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | bug, external, platform:windows |
| [#88818](https://github.com/anthropics/claude-code/issues/88818) | \[BUG\] Claude Desktop (Windows, MSIX) fails to launch after spontaneous close — "reinstall required" dialog, Repair does not fix it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:cowork, area:desktop, area:installation, bug, platform:windows |

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
