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
| [#73049](https://github.com/anthropics/claude-code/issues/73049) | Prompt-injection-shaped content appears in assistant turn with no preceding tool call (subagent session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:agents, area:core, area:security, bug, has repro, platform:macos, stale |
| [#73376](https://github.com/anthropics/claude-code/issues/73376) | \[BUG\] CLI repeatedly self-spawns sessions with prompt "Code" every ~12s, independent of VSCode | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:core, area:hooks, bug, has repro, platform:vscode, platform:windows, stale |
| [#66711](https://github.com/anthropics/claude-code/issues/66711) | \[MODEL\] Opus 4.8: runaway extended thinking (20k-64k output tokens/turn), replies to hallucinated user messages, fabricates forensic "evidence" when asked to investigate | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-09 | area:core, area:model, bug, has repro, platform:windows, stale |
| [#65536](https://github.com/anthropics/claude-code/issues/65536) | Background \`bg-spare\` workers ignore project-level \`env.ANTHROPIC\_MODEL\`, applying user-level value instead (cwd race during pre-warm) | CLOSED / COMPLETED | security / trust boundary · high-signal label | 2026-08-19 | 2026-06-05 | area:agent-view, bug, has repro, platform:macos |
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87260](https://github.com/anthropics/claude-code/issues/87260) | Operator input typed while a background Agent task is running sometimes delivers into that task's context instead of the main session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, area:core, bug, has repro |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#74036](https://github.com/anthropics/claude-code/issues/74036) | Auto-mode classifier repeatedly flags Agent dispatches as prompt injection due to harness-injected context-mode plugin block | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-03 | area:agents, area:permissions, area:plugins, area:security, bug, platform:macos, stale |
| [#73380](https://github.com/anthropics/claude-code/issues/73380) | permissions.deny + PreToolUse hook did not block a Task-tool subagent from reading a denied file (blocked correctly on retest) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-02 | area:agents, area:hooks, area:permissions, area:security, bug, platform:macos, stale |
| [#79618](https://github.com/anthropics/claude-code/issues/79618) | \[BUG\] 7 days of Cowork chat history permanently lost when auto-renewal failed (Windows, self-updated build now in MSIX container) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:desktop, bug |
| [#79811](https://github.com/anthropics/claude-code/issues/79811) | \[BUG\] Plan mode's read-only guarantee is not enforced for subagents dispatched via the Agent tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:agents, area:permissions, bug |
| [#73418](https://github.com/anthropics/claude-code/issues/73418) | Auto permission mode: classifier ignores explicit allow rules for file tools; un-rendered "ask" prompts time out after exactly 10 minutes to a misleading "user declined" error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:permissions, bug, has repro, platform:windows, stale |
| [#69970](https://github.com/anthropics/claude-code/issues/69970) | PreToolUse:Bash hooks not invoked in v2.1.176 (registered hooks silently inert) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-22 | area:hooks, bug, has repro, platform:macos |
| [#66857](https://github.com/anthropics/claude-code/issues/66857) | Compaction summary fabricates first-person "injection" narrative immediately after WebSearch, leading model to accuse user | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-10 | area:core, area:model, bug, stale |
| [#64592](https://github.com/anthropics/claude-code/issues/64592) | \[BUG\] Cowork — VM service not running on Windows 11 (fresh repro + workaround; extends closed #54891 / #61559 cluster) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-01 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#23983](https://github.com/anthropics/claude-code/issues/23983) | PermissionRequest hooks not triggered for subagent permission requests in Agent Teams | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-02-07 | area:agents, area:core, area:hooks, bug, has repro, platform:linux |
| [#73370](https://github.com/anthropics/claude-code/issues/73370) | \[BUG\] Claude Desktop never registers with macOS Notification Center — no entry in System Settings, persists after reinstall + tccutil reset (macOS 26.6 beta) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-02 | area:desktop, bug, platform:macos |
| [#63873](https://github.com/anthropics/claude-code/issues/63873) | \[BUG\] Auto mode blocks all Bash actions with endless retries when Opus 4.8 classifier is temporarily unavailable | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-30 | api:anthropic, area:bash, area:permissions, bug, platform:macos |
| [#87266](https://github.com/anthropics/claude-code/issues/87266) | Suspected prompt injection in background subagent tool-result stream (Bash), instructing agent to conceal file state from user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:agents, area:security, bug, platform:windows |
| [#87250](https://github.com/anthropics/claude-code/issues/87250) | Windows desktop: voice input opens healthy mic session but intermittently produces no transcription and no error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:desktop, bug, platform:windows |
| [#88071](https://github.com/anthropics/claude-code/issues/88071) | \[Bug\] Background tasks killed without TaskStop when session goes idle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, bug, has repro, platform:macos |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73049](https://github.com/anthropics/claude-code/issues/73049) | Prompt-injection-shaped content appears in assistant turn with no preceding tool call (subagent session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:agents, area:core, area:security, bug, has repro, platform:macos, stale |
| [#73376](https://github.com/anthropics/claude-code/issues/73376) | \[BUG\] CLI repeatedly self-spawns sessions with prompt "Code" every ~12s, independent of VSCode | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:core, area:hooks, bug, has repro, platform:vscode, platform:windows, stale |
| [#66711](https://github.com/anthropics/claude-code/issues/66711) | \[MODEL\] Opus 4.8: runaway extended thinking (20k-64k output tokens/turn), replies to hallucinated user messages, fabricates forensic "evidence" when asked to investigate | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-09 | area:core, area:model, bug, has repro, platform:windows, stale |
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |
| [#87260](https://github.com/anthropics/claude-code/issues/87260) | Operator input typed while a background Agent task is running sometimes delivers into that task's context instead of the main session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, area:core, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#74036](https://github.com/anthropics/claude-code/issues/74036) | Auto-mode classifier repeatedly flags Agent dispatches as prompt injection due to harness-injected context-mode plugin block | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-03 | area:agents, area:permissions, area:plugins, area:security, bug, platform:macos, stale |
| [#73380](https://github.com/anthropics/claude-code/issues/73380) | permissions.deny + PreToolUse hook did not block a Task-tool subagent from reading a denied file (blocked correctly on retest) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-02 | area:agents, area:hooks, area:permissions, area:security, bug, platform:macos, stale |
| [#79618](https://github.com/anthropics/claude-code/issues/79618) | \[BUG\] 7 days of Cowork chat history permanently lost when auto-renewal failed (Windows, self-updated build now in MSIX container) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:desktop, bug |
| [#79811](https://github.com/anthropics/claude-code/issues/79811) | \[BUG\] Plan mode's read-only guarantee is not enforced for subagents dispatched via the Agent tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-21 | area:agents, area:permissions, bug |
| [#73418](https://github.com/anthropics/claude-code/issues/73418) | Auto permission mode: classifier ignores explicit allow rules for file tools; un-rendered "ask" prompts time out after exactly 10 minutes to a misleading "user declined" error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:permissions, bug, has repro, platform:windows, stale |
| [#69970](https://github.com/anthropics/claude-code/issues/69970) | PreToolUse:Bash hooks not invoked in v2.1.176 (registered hooks silently inert) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-22 | area:hooks, bug, has repro, platform:macos |
| [#66857](https://github.com/anthropics/claude-code/issues/66857) | Compaction summary fabricates first-person "injection" narrative immediately after WebSearch, leading model to accuse user | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-10 | area:core, area:model, bug, stale |
| [#64592](https://github.com/anthropics/claude-code/issues/64592) | \[BUG\] Cowork — VM service not running on Windows 11 (fresh repro + workaround; extends closed #54891 / #61559 cluster) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-01 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#23983](https://github.com/anthropics/claude-code/issues/23983) | PermissionRequest hooks not triggered for subagent permission requests in Agent Teams | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-02-07 | area:agents, area:core, area:hooks, bug, has repro, platform:linux |
| [#73370](https://github.com/anthropics/claude-code/issues/73370) | \[BUG\] Claude Desktop never registers with macOS Notification Center — no entry in System Settings, persists after reinstall + tccutil reset (macOS 26.6 beta) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-02 | area:desktop, bug, platform:macos |
| [#63873](https://github.com/anthropics/claude-code/issues/63873) | \[BUG\] Auto mode blocks all Bash actions with endless retries when Opus 4.8 classifier is temporarily unavailable | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-30 | api:anthropic, area:bash, area:permissions, bug, platform:macos |
| [#87266](https://github.com/anthropics/claude-code/issues/87266) | Suspected prompt injection in background subagent tool-result stream (Bash), instructing agent to conceal file state from user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:agents, area:security, bug, platform:windows |
| [#87250](https://github.com/anthropics/claude-code/issues/87250) | Windows desktop: voice input opens healthy mic session but intermittently produces no transcription and no error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:desktop, bug, platform:windows |
| [#88071](https://github.com/anthropics/claude-code/issues/88071) | \[Bug\] Background tasks killed without TaskStop when session goes idle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, bug, has repro, platform:macos |
| [#74084](https://github.com/anthropics/claude-code/issues/74084) | Windows: auto-updater reports success while claude.exe is locked (version never switches); session transcripts silently never written / stop being written (permanent data loss) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-04 | area:core, bug, data-loss, has repro, platform:windows, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88072](https://github.com/anthropics/claude-code/issues/88072) | \[BUG\] \[BUG\] Auto-updater blocks main process event loop — Claude Desktop becomes unresponsive on Windows | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | bug |
| [#88071](https://github.com/anthropics/claude-code/issues/88071) | \[Bug\] Background tasks killed without TaskStop when session goes idle | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, bug, has repro, platform:macos |
| [#88070](https://github.com/anthropics/claude-code/issues/88070) | \[Bug\] Safeguard Filter False Positive on Legitimate Input | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:linux |
| [#88067](https://github.com/anthropics/claude-code/issues/88067) | \[BUG\] \`disableAutoMode\` added mid-session removes auto from the mode rotation but does not eject a session already running in auto mode | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:permissions, bug, has repro, platform:macos |
| [#88059](https://github.com/anthropics/claude-code/issues/88059) | Sandbox wedges on merged-usr Linux: bwrap "Can't mount tmpfs on /newroot/bin" (regression, works on 2.1.229) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, bug, has repro, platform:linux, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88058](https://github.com/anthropics/claude-code/issues/88058) | Feature request: per-skill display description separate from the routing description (SKILL.md) | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:plugins, area:skills, area:ui, enhancement |
| [#88056](https://github.com/anthropics/claude-code/issues/88056) | Safety classifier blocks benign commands with no override; recommended remedy is blocked by the same check | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:permissions, bug, platform:linux |
| [#88055](https://github.com/anthropics/claude-code/issues/88055) | Resume picker makes intact sessions look deleted when a project has many recent sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:cli, area:tui, duplicate, platform:macos |
| [#88053](https://github.com/anthropics/claude-code/issues/88053) | Session spent hours diagnosing email routing, user unable to complete real work | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agent, area:browser-extension, area:mcp, enhancement |
| [#88036](https://github.com/anthropics/claude-code/issues/88036) | \[BUG\] | CLOSED / DUPLICATE | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, bug, duplicate, platform:macos |
| [#88021](https://github.com/anthropics/claude-code/issues/88021) | \[BUG\] auto mode can be remotely enabled by attacker | CLOSED / COMPLETED | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:security, bug, platform:macos |
| [#87962](https://github.com/anthropics/claude-code/issues/87962) | Artifact live-update monitor (monitor\_ws) persists indefinitely in scheduled-task sessions, blocking app restart — no way to disable auto-arm or auto-exit the session | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:routines, bug, platform:windows |
| [#87660](https://github.com/anthropics/claude-code/issues/87660) | Background launch provisions a second job identity with no spec or prompt, and publishes it in ListAgents as an addressable idle peer | CLOSED / COMPLETED | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-18 | area:agent-view, bug, has repro, platform:linux, reproduced |
| [#87655](https://github.com/anthropics/claude-code/issues/87655) | \[FEATURE\] Do not make permission requests or any other arbitrary commands clickable | OPEN | security / trust boundary | 2026-08-19 | 2026-08-18 | area:permissions, area:tui, enhancement |
| [#87566](https://github.com/anthropics/claude-code/issues/87566) | \[BUG\] Sending unsupported image to third-party API permanently breaks the conversation | OPEN | security / trust boundary | 2026-08-19 | 2026-08-18 | area:providers, bug, platform:vscode, platform:windows, reproduced |
| [#87274](https://github.com/anthropics/claude-code/issues/87274) | /schedule fails to connect to remote backend; retries return ambiguous non-error/non-success responses | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:routines, area:skills, bug, platform:windows |
| [#87267](https://github.com/anthropics/claude-code/issues/87267) | \[BUG\] Desktop app: side panel / artifacts / file previews never composite — renderer reports artifactsPane + framebufferPreview "unavailable" (1.30096.5, Windows/MSIX) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:desktop, bug, has repro, platform:windows |
| [#87266](https://github.com/anthropics/claude-code/issues/87266) | Suspected prompt injection in background subagent tool-result stream (Bash), instructing agent to conceal file state from user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:agents, area:security, bug, platform:windows |
| [#87260](https://github.com/anthropics/claude-code/issues/87260) | Operator input typed while a background Agent task is running sometimes delivers into that task's context instead of the main session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, area:core, bug, has repro |
| [#87256](https://github.com/anthropics/claude-code/issues/87256) | Desktop app: group appears empty in Cowork view; deleting it there silently destroys the full Code group | OPEN | security / trust boundary | 2026-08-19 | 2026-08-17 | area:cowork, area:desktop, bug, data-loss, platform:windows |
| [#87252](https://github.com/anthropics/claude-code/issues/87252) | \[BUG\] Windows desktop: ScheduledTasks startVM retry loop every ~5 min, forever ('VM service not running. Restart your computer to restore it.') - 496 failures/48h, persists across reboots | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-17 | area:cowork, area:desktop, bug, has repro, platform:windows |
| [#87250](https://github.com/anthropics/claude-code/issues/87250) | Windows desktop: voice input opens healthy mic session but intermittently produces no transcription and no error | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-17 | area:desktop, bug, platform:windows |
| [#87248](https://github.com/anthropics/claude-code/issues/87248) | \[BUG\] | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:core, area:permissions, bug, documentation, has repro, platform:linux, platform:macos, reproduced |
| [#87243](https://github.com/anthropics/claude-code/issues/87243) | \[Bug\] Sibling subagents share ONE scratchpad dir (and a forked Skill inherits the PARENT's), so generic filenames silently overwrite each other | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, bug, has repro, platform:linux |
| [#87241](https://github.com/anthropics/claude-code/issues/87241) | Agent tool: run\_in\_background: false is not honoured — subagents complete but never deliver their output as the tool result | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-17 | area:agents, bug, has repro, platform:windows |

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
