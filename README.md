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
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#88292](https://github.com/anthropics/claude-code/issues/88292) | \[BUG\] PreToolUse prompt-hook deny returns the hook's entire configured prompt to Claude in the tool error, not just the reason | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:windows |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#88292](https://github.com/anthropics/claude-code/issues/88292) | \[BUG\] PreToolUse prompt-hook deny returns the hook's entire configured prompt to Claude in the tool error, not just the reason | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:windows |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#87291](https://github.com/anthropics/claude-code/issues/87291) | \[FEATURE\] Team seat usage is available in \`/usage\` but inaccessible to local integrations | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-17 | area:api, area:cli, area:cost, enhancement |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#78339](https://github.com/anthropics/claude-code/issues/78339) | Claude Code fabricated a factual claim from incomplete tool output, ignored contradicting evidence, and ran unauthorized state-changing commands | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:tools, bug, platform:vscode, platform:windows, stale |
| [#77185](https://github.com/anthropics/claude-code/issues/77185) | \[BUG\] Auto-mode classifier denial returned for a Bash command whose side effects were already applied (denial races with execution) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:permissions, bug, has repro, platform:linux, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88341](https://github.com/anthropics/claude-code/issues/88341) | \[BUG\] Desktop: Remote Control session pin state does not sync live across devices — the other device only picks it up after a full app restart | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos, platform:windows |
| [#88340](https://github.com/anthropics/claude-code/issues/88340) | Efficiency friction: noisy nudge reminders, safety-hook false positives, no file:// support in browser tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:mcp, enhancement, platform:macos |
| [#88339](https://github.com/anthropics/claude-code/issues/88339) | \[Bug\] Unable to continue conversation - API request failures across multiple sessions | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:api, bug, needs-repro, platform:macos |
| [#88338](https://github.com/anthropics/claude-code/issues/88338) | PostToolUse rewrite collisions are last-registered-wins, not "last-write-wins" — and a clobbered redaction is silent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, area:security, bug, has repro |
| [#88337](https://github.com/anthropics/claude-code/issues/88337) | \[FEATURE\] Desktop sidebar: indicate which projects have work running | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, area:ui, enhancement, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88336](https://github.com/anthropics/claude-code/issues/88336) | \[Bug\] False positive reasoning\_extraction flag when searching local Claude Code session transcripts | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:macos |
| [#88335](https://github.com/anthropics/claude-code/issues/88335) | \[BUG\] Windows: in-app browser hangs on Cloudflare interstitial and loses the preview pane ("No preview is open") | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, area:tools, bug, has repro, platform:windows |
| [#88334](https://github.com/anthropics/claude-code/issues/88334) | Project pane should show subfolders of an opened parent directory as a tree | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:ui, enhancement |
| [#88333](https://github.com/anthropics/claude-code/issues/88333) | \[BUG\] Claude Code on the web: GitHub write access (push/branch/tree creation) returns 403 "Resource not accessible by integration" despite working read access | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:auth, area:claude-code-web, bug, platform:web |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#88329](https://github.com/anthropics/claude-code/issues/88329) | \[Bug\] Unexpected "reasoning extraction" response when asked to commit and push changes | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:macos |
| [#88328](https://github.com/anthropics/claude-code/issues/88328) | PermissionRequest hooks never fire in --print mode on 2.1.237, while a PreToolUse control in the same settings file does | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, bug, has repro, platform:windows |
| [#88327](https://github.com/anthropics/claude-code/issues/88327) | \[BUG\] Claude in Chrome 1.0.85: navigate and page reading denied on every domain except google.com, no approval prompt ever renders | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:browser-extension, area:chrome, bug, duplicate, platform:windows |
| [#88326](https://github.com/anthropics/claude-code/issues/88326) | \[Bug\] Design canvas public share fails with "unscannable" content scan error | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:skills, bug, has repro, platform:macos |
| [#88325](https://github.com/anthropics/claude-code/issues/88325) | \[FEATURE\] MCP OAuth "URL &gt;" prompt should also accept a bare authorization code | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:auth, area:mcp, enhancement |
| [#88323](https://github.com/anthropics/claude-code/issues/88323) | Claude Desktop (Windows MSIX) bricks itself — package flagged "Modified" after Code Integrity blocks vk\_swiftshader.dll | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:windows |
| [#88322](https://github.com/anthropics/claude-code/issues/88322) | \[Bug\] Anthropic API Error: Security Policy Violation Blocks Tool Execution | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:macos |
| [#88321](https://github.com/anthropics/claude-code/issues/88321) | Interactive startup hangs forever (blank TUI, no timeout) when a plugin marketplace dir contains macOS File Provider dataless placeholders; plus silent infinite retry on rejected API key | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:plugins, area:tui, bug, has repro, platform:macos |
| [#88320](https://github.com/anthropics/claude-code/issues/88320) | Desktop app's GhRestClient burns the user's GitHub GraphQL rate limit: ~640 points per session focus, ~2,000 per turn start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos |
| [#88319](https://github.com/anthropics/claude-code/issues/88319) | Fable 5 safeguards false-positive \[reasoning\_extraction\] terminates code-review subagents (mutation-testing vocabulary) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:model, bug, duplicate, platform:macos |
| [#88318](https://github.com/anthropics/claude-code/issues/88318) | Severe instruction-following degradation: unrequested git commit/PR, ignored instructions, fabricated links — 6 weeks of dated transcript evidence | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:windows |
| [#88317](https://github.com/anthropics/claude-code/issues/88317) | \[BUG\] New session created via keyboard shortcut traps keyboard focus in the webview panel | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:vscode, bug, platform:macos, platform:vscode |
| [#88316](https://github.com/anthropics/claude-code/issues/88316) | \[BUG\] Embedded browser pane does not use the OS VPN / internal DNS | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, area:networking, bug, platform:windows |
| [#88315](https://github.com/anthropics/claude-code/issues/88315) | Desktop: settings changes (e.g. Instructions for Claude) don't reach live sessions and can't be inspected | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, enhancement |
| [#88314](https://github.com/anthropics/claude-code/issues/88314) | Desktop app: SendUserFile markdown cards show download dialog instead of opening in MD viewer | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos, regression |

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
