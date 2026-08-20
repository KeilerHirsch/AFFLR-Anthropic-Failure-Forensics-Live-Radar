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
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |

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
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#39270](https://github.com/anthropics/claude-code/issues/39270) | \[BUG\]  Claude Code         process exited with code 1 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-03-26 | area:desktop, bug, platform:macos, platform:windows |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82092](https://github.com/anthropics/claude-code/issues/82092) | \[BUG\]  Apps gateway serves Claude Desktop an \`otlpEndpoint\` pointing at its own bearer-gated OTLP ingest but no \`otlpHeaders\`, so every Desktop telemetry flush is rejected with \`missing\_token\` | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | bug |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions, enhancement |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88315](https://github.com/anthropics/claude-code/issues/88315) | Desktop: settings changes (e.g. Instructions for Claude) don't reach live sessions and can't be inspected | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | — |
| [#88314](https://github.com/anthropics/claude-code/issues/88314) | Desktop app: SendUserFile markdown cards show download dialog instead of opening in MD viewer | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos, regression |
| [#88313](https://github.com/anthropics/claude-code/issues/88313) | \[Bug\] False positive security risk flagging for non-cybersecurity code | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, needs-repro, platform:linux |
| [#88312](https://github.com/anthropics/claude-code/issues/88312) | Worktree isolation: string-executing builtins (eval, enable) are matched in argument position — \`echo eval\` is refused | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:bash, area:sandbox, bug, platform:macos |
| [#88311](https://github.com/anthropics/claude-code/issues/88311) | Windows: Bash tool permanently broken in long-lived sessions - inlined shell snapshot exceeds command-line length and is truncated | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:bash, bug, has repro, platform:vscode, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88310](https://github.com/anthropics/claude-code/issues/88310) | \[BUG\] Scheduled Routine trigger fires on schedule but session doesn't execute until a browser tab is opened on it | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:claude-code-web, area:routines, bug, platform:web |
| [#88308](https://github.com/anthropics/claude-code/issues/88308) | \[BUG\] Scheduled-task MCP tools (list\_scheduled\_tasks / update\_scheduled\_task) missing from session context on Windows — existing local tasks can't be read or edited by prompt | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:cowork, area:mcp, area:routines, bug, has repro, platform:windows |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#88306](https://github.com/anthropics/claude-code/issues/88306) | Legacy Windows console (conhost): SI byte from reassertTerminalModes renders as a visible glyph in the input box; ambiguous-width glyphs corrupt partial repaints | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:tui, bug, platform:windows |
| [#88304](https://github.com/anthropics/claude-code/issues/88304) | \[Bug\] Fable rejection on \`jq -r\` command triggers automode safeguard | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:permissions, bug, platform:macos |
| [#88303](https://github.com/anthropics/claude-code/issues/88303) | \[Bug\] Fable 5 Safeguard Triggered Incorrectly | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-info, needs-repro, platform:macos |
| [#88302](https://github.com/anthropics/claude-code/issues/88302) | \[FEATURE\] Extend skillOverrides to plugin-namespaced skills | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:plugins, area:skills, enhancement |
| [#88301](https://github.com/anthropics/claude-code/issues/88301) | \[Bug\] Anthropic API Error: Intermittent false-positive safeguard errors with large MCP tool results | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, area:mcp, bug, platform:windows |
| [#88300](https://github.com/anthropics/claude-code/issues/88300) | \[Bug\] Artifact publish auto-arms live-updates monitor with no opt-out or agent control | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, duplicate, platform:macos |
| [#88299](https://github.com/anthropics/claude-code/issues/88299) | \[Bug\] Safety guardrails triggered unexpectedly without user input | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:model, bug, platform:macos |
| [#88298](https://github.com/anthropics/claude-code/issues/88298) | MCP tool results missing content blocks: accessibility tree never surfaced, screenshot intermittently dropped | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:mcp, bug, platform:macos |
| [#88296](https://github.com/anthropics/claude-code/issues/88296) | \[BUG\] "Prompt is too long" in a new session when another session        has an open plan | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:core, bug, has repro, platform:windows, platform:wsl |
| [#88294](https://github.com/anthropics/claude-code/issues/88294) | \[Bug\] Thinking mode incorrectly flagged as reasoning extraction during prompt generation benchmark | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:providers, bug, platform:macos |
| [#88293](https://github.com/anthropics/claude-code/issues/88293) | \[BUG\] Cursor jumps and overwrites text in VS Code integrated terminal after a few minutes (arrow keys trigger it) — continuation of #3116 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos, platform:vscode |
| [#88292](https://github.com/anthropics/claude-code/issues/88292) | \[BUG\] PreToolUse prompt-hook deny returns the hook's entire configured prompt to Claude in the tool error, not just the reason | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:windows |
| [#88290](https://github.com/anthropics/claude-code/issues/88290) | \[Bug\] Opus 5 model performance issues | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-info |
| [#88289](https://github.com/anthropics/claude-code/issues/88289) | Model fabricated a 'user' turn inside assistant output, then acted on it (unrequested ScheduleWakeup) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:vscode, platform:windows |
| [#88288](https://github.com/anthropics/claude-code/issues/88288) | \[Bug\] Resume workflow skips journal cache entries and re-runs completed agents | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, bug, has repro, platform:macos |
| [#88287](https://github.com/anthropics/claude-code/issues/88287) | \[VS Code\] Confirm before closing a tab with an active Claude session | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:ide, enhancement, platform:vscode |
| [#88286](https://github.com/anthropics/claude-code/issues/88286) | \[Bug\] Fable blocking explicitly permitted commands in settings.json | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:permissions, bug, platform:macos |

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
