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
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#88292](https://github.com/anthropics/claude-code/issues/88292) | \[BUG\] PreToolUse prompt-hook deny returns the hook's entire configured prompt to Claude in the tool error, not just the reason | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:windows |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88380](https://github.com/anthropics/claude-code/issues/88380) | \[FEATURE\] Detect and offer to mask secrets in pasted text before it enters the transcript | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:security, area:tui, enhancement |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#77738](https://github.com/anthropics/claude-code/issues/77738) | \[Bug\] Fable 5 safeguard over-flags defensive security hardening as offensive activity | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-15 | area:model, bug, platform:macos |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#88292](https://github.com/anthropics/claude-code/issues/88292) | \[BUG\] PreToolUse prompt-hook deny returns the hook's entire configured prompt to Claude in the tool error, not just the reason | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:windows |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#50624](https://github.com/anthropics/claude-code/issues/50624) | auto-mode permission-deny envelope returned without intercepting Bash dispatch (silent-bypass on git push origin main, CLI 2.1.114, Opus 4.7) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-04-19 | area:bash, area:permissions, area:security, bug, has repro, platform:macos, stale |
| [#60305](https://github.com/anthropics/claude-code/issues/60305) | Cloud sessions: non-interactive Azure CLI auth path | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-05-18 | area:auth, area:claude-code-web, area:hooks, enhancement, platform:web, stale |
| [#86706](https://github.com/anthropics/claude-code/issues/86706) | \[BUG\] macOS permission prompts identify Claude Code as a version number ("2.1.232") instead of "Claude Code" — root cause + fix | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:packaging, bug, has repro, platform:macos |
| [#88244](https://github.com/anthropics/claude-code/issues/88244) | \[MODEL\] Fable 5 writes a fabricated future work history — including the user's approval — into a persistent work-log file; self-caught in the very next thinking block | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | api:anthropic, area:model, bug |
| [#78773](https://github.com/anthropics/claude-code/issues/78773) | Fable 5 safeguards repeatedly flag routine desktop-app development (input hooks, WASAPI capture, path validation) and auto-switch the session model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-18 | area:model, bug, platform:windows, stale |
| [#77214](https://github.com/anthropics/claude-code/issues/77214) | \[BUG\] Model fabricates user messages after interrupt + long extended thinking, executes the fabricated “request”, and attributes it to external injection | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | area:model, bug, memory, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88380](https://github.com/anthropics/claude-code/issues/88380) | \[FEATURE\] Detect and offer to mask secrets in pasted text before it enters the transcript | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:security, area:tui, enhancement |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#82115](https://github.com/anthropics/claude-code/issues/82115) | \[FEATURE\] Authoritative Workflow Execution — process compliance, not outcome equivalence | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-28 | area:core, enhancement |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#81138](https://github.com/anthropics/claude-code/issues/81138) | \[BUG\] Account email (PII) is injected into the model's system prompt without consent, disclosure, | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | bug |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-11 | area:cost, bug, platform:macos |
| [#83062](https://github.com/anthropics/claude-code/issues/83062) | \[Billing\]\[Bug\] $995.67 in two Individual-plan auto-recharges after included limits reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | — |
| [#81703](https://github.com/anthropics/claude-code/issues/81703) | \[BUG\] July 17 mass billing incident: usage credits charged despite plan allowance; $604.71 automatic recharges disputed | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | — |
| [#50903](https://github.com/anthropics/claude-code/issues/50903) | Channels feature regressed between 2.1.104 and 2.1.114 on personal Max: tengu\_harbor evaluates false despite cached true | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-04-19 | area:plugins, duplicate, platform:macos, stale |
| [#88364](https://github.com/anthropics/claude-code/issues/88364) | \[Bug\] Fable 5 \`reasoning\_extraction\` refusals track a client-injected batching reminder new in 2.1.236 (version bisect + same-day cross-version control) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:model, bug, has repro, platform:macos |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88381](https://github.com/anthropics/claude-code/issues/88381) | \[Bug\] Artifact version history shows stale cached versions and prevents deletion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, platform:macos |
| [#88380](https://github.com/anthropics/claude-code/issues/88380) | \[FEATURE\] Detect and offer to mask secrets in pasted text before it enters the transcript | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:security, area:tui, enhancement |
| [#88379](https://github.com/anthropics/claude-code/issues/88379) | \[BUG\] Worktree isolation refuses \`git -C .\` inside its own worktree — a leading \`./\` is read as "computed at runtime" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:sandbox, bug, has repro, platform:wsl |
| [#88378](https://github.com/anthropics/claude-code/issues/88378) | Background task notifications stay queued until the next user message in SDK streaming mode | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agent-sdk, bug, platform:linux |
| [#88377](https://github.com/anthropics/claude-code/issues/88377) | \[BUG\] Vim mode: after a paste, Shift+Enter intermittently submits instead of inserting a newline (Ghostty/macOS, stock keytab) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88375](https://github.com/anthropics/claude-code/issues/88375) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:windows |
| [#88372](https://github.com/anthropics/claude-code/issues/88372) | \[Bug\] Fullscreen TUI mode missing draggable scrollbar and position indicator | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:tui, bug, platform:linux |
| [#88371](https://github.com/anthropics/claude-code/issues/88371) | Claude Chrome extension doesn't connect | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:chrome, bug, needs-info |
| [#88370](https://github.com/anthropics/claude-code/issues/88370) | MCP Apps widgets stopped rendering after staged rollout of server/discover version negotiation (2.1.234) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:mcp, bug, platform:macos |
| [#88368](https://github.com/anthropics/claude-code/issues/88368) | \[FEATURE\] Plugin API: let plugins provide prompt suggestions via a provides\_prompt\_suggestions component | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:plugins, area:tui, enhancement |
| [#88367](https://github.com/anthropics/claude-code/issues/88367) | \[Bug\] Clear command removes custom session name despite maintaining session context | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:tui, bug, platform:macos |
| [#88366](https://github.com/anthropics/claude-code/issues/88366) | Agent Delegation / CLAUDE.md rules get ignored mid-session even after repeated explicit correction in the same conversation | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:agents, area:core, area:model, bug |
| [#88365](https://github.com/anthropics/claude-code/issues/88365) | \[BUG\] Desktop app helper \`disclaimer\` lacks entitlements for ~/Library/Mobile Documents (iCloud Drive) — extends #34554 | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:macos |
| [#88364](https://github.com/anthropics/claude-code/issues/88364) | \[Bug\] Fable 5 \`reasoning\_extraction\` refusals track a client-injected batching reminder new in 2.1.236 (version bisect + same-day cross-version control) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:model, bug, has repro, platform:macos |
| [#88363](https://github.com/anthropics/claude-code/issues/88363) | \[FEATURE\] Desktop: remember the link destination and reuse the open Browser pane, instead of a chooser on every external link | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, enhancement |
| [#88362](https://github.com/anthropics/claude-code/issues/88362) | \[Bug\] Interactive startup hangs indefinitely (blank screen) when TERM\_PROGRAM=Apple\_Terminal (v2.1.237, macOS) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |
| [#88361](https://github.com/anthropics/claude-code/issues/88361) | \[Bug\] False positive error during OS troubleshooting on tablet | OPEN | observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, needs-info, platform:macos |
| [#88360](https://github.com/anthropics/claude-code/issues/88360) | Terminal title rewritten every 960ms (activity glyph is part of the title payload), restarting terminal status animations | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |
| [#88358](https://github.com/anthropics/claude-code/issues/88358) | Windows: telegram plugin's stale-poller eviction never fires — \`ps -p &lt;pid&gt; -o args=\` is unsupported by Cygwin ps, failure swallowed, bot.pid overwritten anyway | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:plugins, bug, has repro, platform:windows |
| [#88357](https://github.com/anthropics/claude-code/issues/88357) | SendMessage (cross-session/teammate) silently discards queued messages to a busy session: \`queue-operation: remove\` instead of \`dequeue\` | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:mcp, bug, platform:linux |
| [#88356](https://github.com/anthropics/claude-code/issues/88356) | I don't have any bug report content to analyze. You've provided what appear to be Anthropic API request IDs, but no actual bug description, error message, or issue details.  Please provide the bug report information including: - What happened (the problem/ | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:macos |
| [#88354](https://github.com/anthropics/claude-code/issues/88354) | Personal instructions should have one source of truth across local and cloud sessions | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:claude-code-web, area:core, enhancement |
| [#88353](https://github.com/anthropics/claude-code/issues/88353) | \[BUG\] Weekly limit stays at 99% after Pro → Max 20x re-login; rateLimitTier now correct but counter not recalculated | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:auth, area:cost, bug, platform:linux, platform:wsl |
| [#88352](https://github.com/anthropics/claude-code/issues/88352) | Weekly quota pool shrank 43.5% across three consecutive windows with identical promo conditions (Max 20x) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:cost, platform:linux, question |
| [#88351](https://github.com/anthropics/claude-code/issues/88351) | Desktop app ignores \`respondToBashCommands: false\` (bundled 2.1.234); terminal CLI honors it | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:bash, area:desktop, bug, platform:macos |

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
