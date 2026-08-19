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
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |
| [#87260](https://github.com/anthropics/claude-code/issues/87260) | Operator input typed while a background Agent task is running sometimes delivers into that task's context instead of the main session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, area:core, bug, has repro |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#9628](https://github.com/anthropics/claude-code/issues/9628) | \[BUG\] CC crashes with new release of Nodejs v25 | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-16 | area:packaging, bug, has repro, oncall, platform:windows |
| [#79449](https://github.com/anthropics/claude-code/issues/79449) | ask PreToolUse hook decision silently fails to surface in a top-level session carrying CLAUDE\_CODE\_CHILD\_SESSION=1 (command executes instead of pausing for approval) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-20 | area:hooks, area:permissions, area:security, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79618](https://github.com/anthropics/claude-code/issues/79618) | \[BUG\] 7 days of Cowork chat history permanently lost when auto-renewal failed (Windows, self-updated build now in MSIX container) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:desktop, bug |
| [#79811](https://github.com/anthropics/claude-code/issues/79811) | \[BUG\] Plan mode's read-only guarantee is not enforced for subagents dispatched via the Agent tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:agents, area:permissions, bug |
| [#79439](https://github.com/anthropics/claude-code/issues/79439) | \[BUG\] Consantly getting: API Error: Stream idle timeout - no chunks received | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-20 | api:anthropic, area:networking, bug, duplicate, platform:windows |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#23983](https://github.com/anthropics/claude-code/issues/23983) | PermissionRequest hooks not triggered for subagent permission requests in Agent Teams | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-02-07 | area:agents, area:core, area:hooks, bug, has repro, platform:linux |
| [#88054](https://github.com/anthropics/claude-code/issues/88054) | \`claude remote-control\` server exits on 401 after exactly 24h — does not refresh its OAuth access token, killing every attached session | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:macos |
| [#79403](https://github.com/anthropics/claude-code/issues/79403) | VS Code extension /model toggle intermittently corrupts settings.json (malformed JSON), silently dropping all permissions and hooks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-20 | area:core, bug, has repro, platform:vscode, platform:windows |
| [#4540](https://github.com/anthropics/claude-code/issues/4540) | \[BUG\] Missing \`scope\` Parameter in Dynamic Client Registration and Authorization Requests | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-07-27 | area:auth, area:mcp, bug, has repro, oncall |
| [#87266](https://github.com/anthropics/claude-code/issues/87266) | Suspected prompt injection in background subagent tool-result stream (Bash), instructing agent to conceal file state from user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:agents, area:security, bug, platform:windows |
| [#87250](https://github.com/anthropics/claude-code/issues/87250) | Windows desktop: voice input opens healthy mic session but intermittently produces no transcription and no error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:desktop, bug, platform:windows |
| [#81529](https://github.com/anthropics/claude-code/issues/81529) | Auto-compaction stops firing entirely after v2.1.199 (regression from v2.1.92; still absent in v2.1.217) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#46767](https://github.com/anthropics/claude-code/issues/46767) | \[BUG\] Tool results silently dropped with "missing due to internal error" across all tools on Windows (regression in 2.1.101) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-04-11 | area:core, bug, platform:windows, regression, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |
| [#87260](https://github.com/anthropics/claude-code/issues/87260) | Operator input typed while a background Agent task is running sometimes delivers into that task's context instead of the main session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, area:core, bug, has repro |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#9628](https://github.com/anthropics/claude-code/issues/9628) | \[BUG\] CC crashes with new release of Nodejs v25 | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-16 | area:packaging, bug, has repro, oncall, platform:windows |
| [#79449](https://github.com/anthropics/claude-code/issues/79449) | ask PreToolUse hook decision silently fails to surface in a top-level session carrying CLAUDE\_CODE\_CHILD\_SESSION=1 (command executes instead of pausing for approval) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-20 | area:hooks, area:permissions, area:security, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79618](https://github.com/anthropics/claude-code/issues/79618) | \[BUG\] 7 days of Cowork chat history permanently lost when auto-renewal failed (Windows, self-updated build now in MSIX container) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:desktop, bug |
| [#79811](https://github.com/anthropics/claude-code/issues/79811) | \[BUG\] Plan mode's read-only guarantee is not enforced for subagents dispatched via the Agent tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:agents, area:permissions, bug |
| [#79439](https://github.com/anthropics/claude-code/issues/79439) | \[BUG\] Consantly getting: API Error: Stream idle timeout - no chunks received | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-20 | api:anthropic, area:networking, bug, duplicate, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#23983](https://github.com/anthropics/claude-code/issues/23983) | PermissionRequest hooks not triggered for subagent permission requests in Agent Teams | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-02-07 | area:agents, area:core, area:hooks, bug, has repro, platform:linux |
| [#79403](https://github.com/anthropics/claude-code/issues/79403) | VS Code extension /model toggle intermittently corrupts settings.json (malformed JSON), silently dropping all permissions and hooks | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-20 | area:core, bug, has repro, platform:vscode, platform:windows |
| [#4540](https://github.com/anthropics/claude-code/issues/4540) | \[BUG\] Missing \`scope\` Parameter in Dynamic Client Registration and Authorization Requests | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-07-27 | area:auth, area:mcp, bug, has repro, oncall |
| [#87266](https://github.com/anthropics/claude-code/issues/87266) | Suspected prompt injection in background subagent tool-result stream (Bash), instructing agent to conceal file state from user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:agents, area:security, bug, platform:windows |
| [#87250](https://github.com/anthropics/claude-code/issues/87250) | Windows desktop: voice input opens healthy mic session but intermittently produces no transcription and no error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:desktop, bug, platform:windows |
| [#81529](https://github.com/anthropics/claude-code/issues/81529) | Auto-compaction stops firing entirely after v2.1.199 (regression from v2.1.92; still absent in v2.1.217) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-27 | — |
| [#46767](https://github.com/anthropics/claude-code/issues/46767) | \[BUG\] Tool results silently dropped with "missing due to internal error" across all tools on Windows (regression in 2.1.101) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-04-11 | area:core, bug, platform:windows, regression, stale |
| [#87248](https://github.com/anthropics/claude-code/issues/87248) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:core, area:permissions, bug, documentation, has repro, platform:linux, platform:macos, reproduced |
| [#87234](https://github.com/anthropics/claude-code/issues/87234) | \[BUG\] Claude Code CLI: \`--json-schema\` calls emit literal \`$PARAMETER\_NAME\` placeholder keys on toolless calls | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | api:anthropic, area:cli, area:tools, bug, has repro, platform:linux |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88058](https://github.com/anthropics/claude-code/issues/88058) | Feature request: per-skill display description separate from the routing description (SKILL.md) | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:plugins, area:skills, area:ui, enhancement |
| [#88057](https://github.com/anthropics/claude-code/issues/88057) | \[BUG\] Claude in Chrome: select\_browser is account-wide, so one session silently moves every other session's browser | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:chrome, bug, has repro, platform:windows |
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |
| [#88055](https://github.com/anthropics/claude-code/issues/88055) | Resume picker makes intact sessions look deleted when a project has many recent sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:cli, area:tui, duplicate, platform:macos |
| [#88054](https://github.com/anthropics/claude-code/issues/88054) | \`claude remote-control\` server exits on 401 after exactly 24h — does not refresh its OAuth access token, killing every attached session | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88053](https://github.com/anthropics/claude-code/issues/88053) | Session spent hours diagnosing email routing, user unable to complete real work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent, area:browser-extension, area:mcp, enhancement |
| [#88051](https://github.com/anthropics/claude-code/issues/88051) | \[BUG\] ~/.claude/settings.local.json is only applied to sessions started in $HOME — permissions and hooks silently inert elsewhere | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:hooks, area:permissions, bug, has repro, platform:linux |
| [#88047](https://github.com/anthropics/claude-code/issues/88047) | Worktree command-safety analyzer misreads a non-leading \`complete\`/\`compgen\`/\`compopt\` token as an invoked builtin | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, bug, has repro, platform:windows |
| [#88046](https://github.com/anthropics/claude-code/issues/88046) | \[FEATURE\] --prefill flag to pre-fill input box without sending | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, area:tui, enhancement |
| [#88042](https://github.com/anthropics/claude-code/issues/88042) | \[Bug\] Normal app workflows trigger Claude's safety guidelines | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:macos |
| [#88041](https://github.com/anthropics/claude-code/issues/88041) | \[Bug\] Auto-mode "bashFirst" system prompt instructs sed/heredoc file edits instead of Edit/Write tools | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, area:tools, bug, platform:linux |
| [#88039](https://github.com/anthropics/claude-code/issues/88039) | \[Bug\] /advisor silently omits Fable 5 when ANTHROPIC\_BASE\_URL is set, despite first-party OAuth login and cached Fable entitlement | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:self-hosted-environments, bug, has repro, platform:macos |
| [#88036](https://github.com/anthropics/claude-code/issues/88036) | \[BUG\] | CLOSED / DUPLICATE | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, bug, duplicate, platform:macos |
| [#88032](https://github.com/anthropics/claude-code/issues/88032) | \[MODEL\] Sonnet 5 | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | api:anthropic, area:model, bug, model |
| [#88027](https://github.com/anthropics/claude-code/issues/88027) | \[BUG\] Webview CSS: six custom properties are referenced but never defined, plus two light-background issues | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:ide, area:ui, bug, has repro, platform:vscode, platform:windows |
| [#88023](https://github.com/anthropics/claude-code/issues/88023) | Project custom agents (.claude/agents/) become unavailable to Agent tool after /compact, in same session, no worktree transition | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, bug, has repro, platform:macos |
| [#88021](https://github.com/anthropics/claude-code/issues/88021) | \[BUG\] auto mode can be remotely enabled by attacker | CLOSED / COMPLETED | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:security, bug, platform:macos |
| [#88020](https://github.com/anthropics/claude-code/issues/88020) | \[FEATURE\] Desktop: named split-view layouts with lockable cells | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:ui, enhancement |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#87994](https://github.com/anthropics/claude-code/issues/87994) | Background subagents (e.g. via /code-review) silently auto-deny gated Bash commands instead of prompting | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, area:permissions, bug, has repro, platform:windows |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#87980](https://github.com/anthropics/claude-code/issues/87980) | Windows regression in 2.1.235: PowerShell tool fails from Git Bash with \`--model haiku\` (\`pwsh exited with code 1\`) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:permissions, area:tools, bug, has repro, platform:windows, regression |
| [#87962](https://github.com/anthropics/claude-code/issues/87962) | Artifact live-update monitor (monitor\_ws) persists indefinitely in scheduled-task sessions, blocking app restart — no way to disable auto-arm or auto-exit the session | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:routines, bug, platform:windows |
| [#87953](https://github.com/anthropics/claude-code/issues/87953) | Subagent Bash cwd resets to another subagent's worktree, with no cwd param to pin it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:bash, bug, platform:windows |
| [#87948](https://github.com/anthropics/claude-code/issues/87948) | \[BUG\] run\_in\_background tasks intermittently killed ~17-20s after start, seconds after the arming turn ends (terminal CLI, Linux — not idle-timeout timing) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:core, bug, has repro, platform:linux |

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
