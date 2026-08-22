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
| [#88815](https://github.com/anthropics/claude-code/issues/88815) | \[MODEL\] Stated rules do not constrain subsequent behavior — with 2.5 months of session data | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:core, area:model, bug, model |
| [#88811](https://github.com/anthropics/claude-code/issues/88811) | \[Bug\]\[cyber\] False positive on source code security audit for secrets and injection flaws (req\_011CeHkQQYxDgGvYxjD1HFZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88806](https://github.com/anthropics/claude-code/issues/88806) | \[Bug\]\[cyber\] False positive on rotating hardcoded secret keys and updating signing certs (req\_011CeHjhJdNEc6SsqcmHyCSv) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88583](https://github.com/anthropics/claude-code/issues/88583) | \[BUG\] claudeAiOauth wiped from Keychain (tokens blanked, expiresAt:0) when concurrent Desktop sessions race the single-use refresh token — refresh failure clobbers the winner's rotated credential | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#87419](https://github.com/anthropics/claude-code/issues/87419) | \[BUG\] Weekly + Fable scoped meters deplete 1.7-5x faster since Aug 17 reset on Max 20x; OAuth token carried rateLimitTier default\_claude\_max\_5x | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-17 | area:auth, area:cost, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88795](https://github.com/anthropics/claude-code/issues/88795) | Read tool ignores permissions.deny Read(/Users/\*\*) rules in managed-settings.json and user settings.json | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:permissions, area:security, bug, has repro, platform:macos |
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#77993](https://github.com/anthropics/claude-code/issues/77993) | \[FEATURE\] Make the billing identity (account/org) visible and attribute all limit messages to it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-16 | area:auth, enhancement, platform:macos, stale |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88807](https://github.com/anthropics/claude-code/issues/88807) | \[Bug\]\[cyber\] Rotating hardcoded application secrets and configuring certificate signing (req\_011CeHjrvsx8rQGQahiGpnPn) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#73273](https://github.com/anthropics/claude-code/issues/73273) | Remote/cloud sandbox: GitHub credential-injection proxy returns 502, blocking all git/GitHub access | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-02 | area:agents, area:networking, area:sandbox, bug, stale |
| [#81923](https://github.com/anthropics/claude-code/issues/81923) | HTTP MCP OAuth reconnect fails with "MCP endpoint not found at &lt;origin&gt;" right after successful token exchange | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81545](https://github.com/anthropics/claude-code/issues/81545) | Non-interactive login: a supported way to obtain the authorization URL programmatically | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81876](https://github.com/anthropics/claude-code/issues/81876) | \[Bug\] Cyber safeguards falsely blocking subagents on defensive security work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81830](https://github.com/anthropics/claude-code/issues/81830) | \[BUG\] Cowork/Code fail with 403 "Invalid authorization" for 10+ days — Chat works fine | OPEN | security / trust boundary | 2026-08-22 | 2026-07-28 | bug, stale |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81583](https://github.com/anthropics/claude-code/issues/81583) | \[Bug\] Fable 5 Safeguards Block Legitimate Workspace Admin Operations on Tool Results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81574](https://github.com/anthropics/claude-code/issues/81574) | \[BUG\] Windows: recurring forced logouts since ~Jul 22 — .credentials.json overwritten with test-fixture content ("fixture-claude-secret-value-x") | OPEN | security / trust boundary | 2026-08-22 | 2026-07-27 | stale |
| [#81552](https://github.com/anthropics/claude-code/issues/81552) | \[Bug\] Anthropic API Error: False positive cyber policy block on defensive security audit tooling | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81521](https://github.com/anthropics/claude-code/issues/81521) | \[BUG\] Event loop busy-waits ~30s at ~1.3 cores when the embedded resolver has no usable nameservers (EPOLLERR on UDP sockets never serviced); interactive startup then hard-fails with misleading ETIMEOUT — amplifies #78529 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88815](https://github.com/anthropics/claude-code/issues/88815) | \[MODEL\] Stated rules do not constrain subsequent behavior — with 2.5 months of session data | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:core, area:model, bug, model |
| [#88811](https://github.com/anthropics/claude-code/issues/88811) | \[Bug\]\[cyber\] False positive on source code security audit for secrets and injection flaws (req\_011CeHkQQYxDgGvYxjD1HFZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88806](https://github.com/anthropics/claude-code/issues/88806) | \[Bug\]\[cyber\] False positive on rotating hardcoded secret keys and updating signing certs (req\_011CeHjhJdNEc6SsqcmHyCSv) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#75568](https://github.com/anthropics/claude-code/issues/75568) | \[BUG\] Model hallucinates tool executions, then self-reports the hallucinated output as a "prompt injection attack" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-08 | area:model, bug, has repro, platform:macos, stale |
| [#77993](https://github.com/anthropics/claude-code/issues/77993) | \[FEATURE\] Make the billing identity (account/org) visible and attribute all limit messages to it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-07-16 | area:auth, enhancement, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88807](https://github.com/anthropics/claude-code/issues/88807) | \[Bug\]\[cyber\] Rotating hardcoded application secrets and configuring certificate signing (req\_011CeHjrvsx8rQGQahiGpnPn) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-06 | — |
| [#87149](https://github.com/anthropics/claude-code/issues/87149) | claude auto-mode critique returns "No critique was generated" for a large autoMode block; works with a small one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-16 | area:cli, bug, platform:windows |
| [#73273](https://github.com/anthropics/claude-code/issues/73273) | Remote/cloud sandbox: GitHub credential-injection proxy returns 502, blocking all git/GitHub access | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-02 | area:agents, area:networking, area:sandbox, bug, stale |
| [#81923](https://github.com/anthropics/claude-code/issues/81923) | HTTP MCP OAuth reconnect fails with "MCP endpoint not found at &lt;origin&gt;" right after successful token exchange | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81545](https://github.com/anthropics/claude-code/issues/81545) | Non-interactive login: a supported way to obtain the authorization URL programmatically | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81876](https://github.com/anthropics/claude-code/issues/81876) | \[Bug\] Cyber safeguards falsely blocking subagents on defensive security work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-28 | stale |
| [#81385](https://github.com/anthropics/claude-code/issues/81385) | I triple-dog-dare you: ship the other half. Four weeks of fuck-all — and you locked me out of the model I pay for, for doing effect sizes. | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-26 | stale |
| [#81583](https://github.com/anthropics/claude-code/issues/81583) | \[Bug\] Fable 5 Safeguards Block Legitimate Workspace Admin Operations on Tool Results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81552](https://github.com/anthropics/claude-code/issues/81552) | \[Bug\] Anthropic API Error: False positive cyber policy block on defensive security audit tooling | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81524](https://github.com/anthropics/claude-code/issues/81524) | Subagent fabricated a &lt;task-notification&gt; as its own assistant output, with a malicious payload inside, then reported it as a real prompt injection | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | stale |
| [#81521](https://github.com/anthropics/claude-code/issues/81521) | \[BUG\] Event loop busy-waits ~30s at ~1.3 cores when the embedded resolver has no usable nameservers (EPOLLERR on UDP sockets never serviced); interactive startup then hard-fails with misleading ETIMEOUT — amplifies #78529 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-27 | bug, stale |
| [#79948](https://github.com/anthropics/claude-code/issues/79948) | I double-dog-dare you: build the project-management layer Claude Code is missing — because I am tired of doing it for you, and I am WORN | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-21 | stale |
| [#80358](https://github.com/anthropics/claude-code/issues/80358) | \[FEATURE\] Tool manifest — a third tool-loading mode between preload and on-demand | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-07-22 | enhancement, stale |
| [#88753](https://github.com/anthropics/claude-code/issues/88753) | \[BUG\] Compaction led to writing to wrong database in a way that could have destroyed production data | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:core, bug, data-loss, high-priority, platform:macos |
| [#80910](https://github.com/anthropics/claude-code/issues/80910) | \[MODEL\]   Working file-injection technique (DataTransfer onto input\[type=file\]) now blocked by auto-mode classifier, no accessible override | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | model, stale |
| [#80878](https://github.com/anthropics/claude-code/issues/80878) | Agent scaled an unverified destructive fix to ~98% of a user's data, causing a Plex library collapse (classifier friction also noted) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-07-24 | stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88821](https://github.com/anthropics/claude-code/issues/88821) | Claude Code desktop app fails to launch after crash — "Não é possível abrir este aplicativo" / requires Repair, happened twice | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:desktop, bug, platform:windows |
| [#88820](https://github.com/anthropics/claude-code/issues/88820) | \[BUG\] runtime segfault at non-canonical address 0xFFFFFFFFFFFFFFFF kills the CLI mid-session (Windows, v2.1.239) | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | bug, external, platform:windows |
| [#88818](https://github.com/anthropics/claude-code/issues/88818) | \[BUG\] Claude Desktop (Windows, MSIX) fails to launch after spontaneous close — "reinstall required" dialog, Repair does not fix it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:cowork, area:desktop, area:installation, bug, platform:windows |
| [#88817](https://github.com/anthropics/claude-code/issues/88817) | Opening Cloudflare dashboard in Browser pane crashes GPU process (exitCode 101457950), app becomes unlaunchable and requires OS repair | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, bug, duplicate, platform:windows |
| [#88816](https://github.com/anthropics/claude-code/issues/88816) | \[Bug\]\[cyber\] Checking remote access commands to verify post-deployment worker queue metrics (req\_011CeHp2Ls4EaupSRSJaYEPj) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88815](https://github.com/anthropics/claude-code/issues/88815) | \[MODEL\] Stated rules do not constrain subsequent behavior — with 2.5 months of session data | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:core, area:model, bug, model |
| [#88814](https://github.com/anthropics/claude-code/issues/88814) | Skill/slash command names containing a space only match on the first word | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:cli, area:skills, bug, platform:windows |
| [#88813](https://github.com/anthropics/claude-code/issues/88813) | Unresolvable \`@import\` in CLAUDE.md fails completely silently — no warning, and /context shows nothing missing | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:core, bug, has repro, platform:macos |
| [#88812](https://github.com/anthropics/claude-code/issues/88812) | \[Bug\] Desktop app stalls indefinitely on large payloads while CLI completes same tasks normally | OPEN | security / trust boundary | 2026-08-22 | 2026-08-22 | area:desktop, bug, platform:macos |
| [#88811](https://github.com/anthropics/claude-code/issues/88811) | \[Bug\]\[cyber\] False positive on source code security audit for secrets and injection flaws (req\_011CeHkQQYxDgGvYxjD1HFZL) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88810](https://github.com/anthropics/claude-code/issues/88810) | \[Bug\]\[cyber\] False positive on codebase architecture mapping and structured threat modeling (req\_011CeHkPqwedVQPnXRP6YjA8) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88808](https://github.com/anthropics/claude-code/issues/88808) | \[Bug\]\[cyber\] False positive during timeline data rendering and UI shader debugging (req\_011CeHjtCYYzNRTxMpVYSxSe) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88807](https://github.com/anthropics/claude-code/issues/88807) | \[Bug\]\[cyber\] Rotating hardcoded application secrets and configuring certificate signing (req\_011CeHjrvsx8rQGQahiGpnPn) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | — |
| [#88806](https://github.com/anthropics/claude-code/issues/88806) | \[Bug\]\[cyber\] False positive on rotating hardcoded secret keys and updating signing certs (req\_011CeHjhJdNEc6SsqcmHyCSv) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | api:anthropic, area:model, area:security, bug, duplicate, platform:linux |
| [#88805](https://github.com/anthropics/claude-code/issues/88805) | \[BUG\] Native CLI install: macOS TCC network-volume grant keyed to versioned binary path — every auto-update silently drops SMB file access (EPERM) | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:packaging, bug, has repro, platform:macos |
| [#88804](https://github.com/anthropics/claude-code/issues/88804) | Feature Request: Per-project Telegram bot token support | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:plugins, enhancement |
| [#88803](https://github.com/anthropics/claude-code/issues/88803) | Android app parity with desktop: eleven filed gaps, one underlying problem | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:ui, enhancement, platform:android |
| [#88802](https://github.com/anthropics/claude-code/issues/88802) | Shell grep shim: inline \`grep -v\` returns an inverted exit code when output is suppressed (-q or &gt;/dev/null) — answers a file-level question instead of line-level | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:bash, bug, has repro, platform:macos |
| [#88801](https://github.com/anthropics/claude-code/issues/88801) | \[Bug\]\[cyber\] Technical security audit and document review halted mid-session (req\_011CeHhxpi4HBhGJxUwJ5VtB) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, area:security, bug, duplicate, platform:linux |
| [#88800](https://github.com/anthropics/claude-code/issues/88800) | Background/bridge session launch silently writes project .mcp.json servers into disabledMcpjsonServers, persistently disabling them | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:mcp, bug, has repro, platform:macos |
| [#88799](https://github.com/anthropics/claude-code/issues/88799) | Cloud routine (CCR) session 卡死在 "Claude Code process started" 之後，即使不使用任何 MCP 工具 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:routines, bug, has repro |
| [#88798](https://github.com/anthropics/claude-code/issues/88798) | Opus 5: less work actually gets completed per session than with 4.8 | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:model, bug, platform:windows, regression |
| [#88797](https://github.com/anthropics/claude-code/issues/88797) | \[Feature Request\] Add allowlist for approved security research use cases with Claude Opus models | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-22 | 2026-08-22 | area:model, enhancement, platform:macos |
| [#88796](https://github.com/anthropics/claude-code/issues/88796) | \[BUG\] Artifact mit artifact-Capability zeigt dauerhaft "Nur Lesezugriff" für den Eigentümer – Schreibvorgänge werden nicht gespeichert | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-22 | 2026-08-22 | area:claude-code-web, bug, platform:windows |
| [#88795](https://github.com/anthropics/claude-code/issues/88795) | Read tool ignores permissions.deny Read(/Users/\*\*) rules in managed-settings.json and user settings.json | OPEN | security / trust boundary · high-signal label | 2026-08-22 | 2026-08-22 | area:permissions, area:security, bug, has repro, platform:macos |

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
