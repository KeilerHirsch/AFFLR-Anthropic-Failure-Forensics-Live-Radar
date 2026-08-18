# AFFLR — Anthropic Failure Forensics Live Radar

AFFLR watches the public [`anthropics/claude-code`](https://github.com/anthropics/claude-code/issues) issue space and surfaces the strongest GitHub activity signals so interesting failures, regressions, and weird behavior are harder to miss.

> **Automation for productive laziness.** The radar does the repetitive watching; humans still decide what the evidence means.

## 🛰️ Live radar status

**⏱ Next automatic trigger:** every hour at **`:17 UTC`**  
**🔁 Schedule:** hourly  
**▶️ Manual trigger:** available in [GitHub Actions](../../actions/workflows/afflr.yml)  
**📡 Full radar output:** [`watchlist/candidates.md`](watchlist/candidates.md)

The **Top 5** of each view are visible directly below. Positions 6–25 stay one click away in the expandable sections.

<!-- AFFLR-RADAR:START -->
> Automated discovery metadata from public `anthropics/claude-code` issues. Primary ranking is **discovery-only** — not an AFF evidence level, vulnerability rating, or causal attribution.

The live README prioritizes security/trust-boundary and provenance/integrity signals. Popularity views remain in [`watchlist/candidates.md`](watchlist/candidates.md) as secondary discovery metadata.

### 🛡️ Security & trust-boundary signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#86814](https://github.com/anthropics/claude-code/issues/86814) | otelHeadersHelper headers silently dropped for gRPC OTLP exporters (metrics/logs/traces) — falls back to no auth | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-15 | area:networking, bug, has repro, platform:macos, reproduced |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-24 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87545](https://github.com/anthropics/claude-code/issues/87545) | \[BUG\] autoMode in project settings is silently ignored — settings schema does not mark it user-only, unlike sibling restricted keys | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cli, area:permissions, bug, platform:macos |
| [#87554](https://github.com/anthropics/claude-code/issues/87554) | \[BUG\] claude auth startup spins at 100% CPU indefinitely with no timeout (Bun runtime) — \`--version\` unaffected, CLAUDE\_CODE\_OAUTH\_TOKEN suspected trigger | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | api:anthropic, area:auth, bug, has repro, platform:linux |
| [#86298](https://github.com/anthropics/claude-code/issues/86298) | Desktop app (Windows): cross-session messages silently dropped — held for an approval the UI never offers, then expire (~5 min); regression since app 1.28929.0 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-13 | area:desktop, bug, has repro, platform:windows, regression |
| [#87547](https://github.com/anthropics/claude-code/issues/87547) | Worktree cleanup deletes live worktrees when a repo is opened from both Windows and WSL (gitdir path-spelling mismatch makes every cross-side worktree look prunable) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tools, bug, data-loss, has repro, platform:windows, platform:wsl |
| [#60705](https://github.com/anthropics/claude-code/issues/60705) | Model behavior: /goal Stop-hook directive cited as authorization for unrequested actions; absence-from-search treated as evidence of absence; structure-as-substance under pushback | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-05-19 | area:model, bug, platform:macos |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86237](https://github.com/anthropics/claude-code/issues/86237) | \[BUG\] Desktop app: cross-session messages render in target session's UI but never reach the runtime input queue (regression 2.1.222 -&gt; 2.1.227) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-13 | bug |
| [#87398](https://github.com/anthropics/claude-code/issues/87398) | \[BUG\] Unloadable legacy sessions silently defeat the desktop environment default (falls back to Local) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | — |
| [#87553](https://github.com/anthropics/claude-code/issues/87553) | \[BUG\] claude ignores SIGINT despite a registered handler — Ctrl+C dead during startup hang, only SIGKILL works (Bun runtime) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:core, bug, platform:linux |
| [#87413](https://github.com/anthropics/claude-code/issues/87413) | Remote Control on always-on machines: three reproducible edges (consent vs. service autostart, classifier mid-flow interruption, unstable environment identity) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | area:permissions, bug, platform:linux |
| [#81820](https://github.com/anthropics/claude-code/issues/81820) | \[Claude 5: Opus 5 + Fable 5\] Continuation of #57902 — receipt-ignoring, verdict-overclaiming, label-laundering, invented-deferral persist | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-28 | — |
| [#87581](https://github.com/anthropics/claude-code/issues/87581) | \[BUG\] Approving a forwarded teammate permission request with a message silently drops the message | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:agents, area:permissions, bug, has repro, platform:linux |
| [#87503](https://github.com/anthropics/claude-code/issues/87503) | \[BUG\] Cowork VM connection timeout after update to 1.32352.0 on Intel Mac (guest never connects) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, has repro, platform:macos, regression |
| [#86845](https://github.com/anthropics/claude-code/issues/86845) | \[MODEL\] Opus advising Opus | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-15 | api:anthropic, area:cost, area:model, bug, model |
| [#87316](https://github.com/anthropics/claude-code/issues/87316) | \[BUG\] VS Code extension silently closes and relaunches chat channels ("Closing Claude on channel") with no trigger — occasional config lock race on resume | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | bug, platform:vscode, platform:wsl |
| [#80444](https://github.com/anthropics/claude-code/issues/80444) | \[Windows\] Desktop app 1.24012.1: fatal GPU-process crash (0x060C201E) via in-app Browser tab; crash leaves MSIX package unlaunchable (appxState=2) until Repair | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-23 | — |
| [#87539](https://github.com/anthropics/claude-code/issues/87539) | You've hit your session limit · resets 6:20am (America/New\_York) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cost, bug, duplicate, platform:linux, platform:vscode |
| [#75043](https://github.com/anthropics/claude-code/issues/75043) | Nested subagents: children spawned by a subagent are always async (regardless of run\_in\_background), completion notifications never reach the subagent parent, and TaskStop fails with ownership errors after resume | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:agents, bug, has repro, platform:macos, reproduced |
| [#87574](https://github.com/anthropics/claude-code/issues/87574) | \[FEATURE\] Configurable / per-sender color for inbound peer (@ sender ›) and channel (← source:) message labels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:tui, enhancement |
| [#84689](https://github.com/anthropics/claude-code/issues/84689) | \[BUG\] CVP approved org still blocked by cyber safeguards — org ID confirmed matching, appeal form shows no fields | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-07 | bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87548](https://github.com/anthropics/claude-code/issues/87548) | \[BUG\] "MCP tool call requires approval" in an INTERACTIVE remote session — the approval is clicked and ignored, and the refusal is per-tool on one connector | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:claude-code-web, area:mcp, area:permissions, bug, has repro, platform:web |
| [#86814](https://github.com/anthropics/claude-code/issues/86814) | otelHeadersHelper headers silently dropped for gRPC OTLP exporters (metrics/logs/traces) — falls back to no auth | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-15 | area:networking, bug, has repro, platform:macos, reproduced |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-24 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87545](https://github.com/anthropics/claude-code/issues/87545) | \[BUG\] autoMode in project settings is silently ignored — settings schema does not mark it user-only, unlike sibling restricted keys | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cli, area:permissions, bug, platform:macos |
| [#87554](https://github.com/anthropics/claude-code/issues/87554) | \[BUG\] claude auth startup spins at 100% CPU indefinitely with no timeout (Bun runtime) — \`--version\` unaffected, CLAUDE\_CODE\_OAUTH\_TOKEN suspected trigger | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | api:anthropic, area:auth, bug, has repro, platform:linux |
| [#86298](https://github.com/anthropics/claude-code/issues/86298) | Desktop app (Windows): cross-session messages silently dropped — held for an approval the UI never offers, then expire (~5 min); regression since app 1.28929.0 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-13 | area:desktop, bug, has repro, platform:windows, regression |
| [#87547](https://github.com/anthropics/claude-code/issues/87547) | Worktree cleanup deletes live worktrees when a repo is opened from both Windows and WSL (gitdir path-spelling mismatch makes every cross-side worktree look prunable) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:tools, bug, data-loss, has repro, platform:windows, platform:wsl |
| [#60705](https://github.com/anthropics/claude-code/issues/60705) | Model behavior: /goal Stop-hook directive cited as authorization for unrequested actions; absence-from-search treated as evidence of absence; structure-as-substance under pushback | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-05-19 | area:model, bug, platform:macos |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86237](https://github.com/anthropics/claude-code/issues/86237) | \[BUG\] Desktop app: cross-session messages render in target session's UI but never reach the runtime input queue (regression 2.1.222 -&gt; 2.1.227) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-13 | bug |
| [#87398](https://github.com/anthropics/claude-code/issues/87398) | \[BUG\] Unloadable legacy sessions silently defeat the desktop environment default (falls back to Local) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | — |
| [#87553](https://github.com/anthropics/claude-code/issues/87553) | \[BUG\] claude ignores SIGINT despite a registered handler — Ctrl+C dead during startup hang, only SIGKILL works (Bun runtime) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:core, bug, platform:linux |
| [#87413](https://github.com/anthropics/claude-code/issues/87413) | Remote Control on always-on machines: three reproducible edges (consent vs. service autostart, classifier mid-flow interruption, unstable environment identity) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | area:permissions, bug, platform:linux |
| [#81820](https://github.com/anthropics/claude-code/issues/81820) | \[Claude 5: Opus 5 + Fable 5\] Continuation of #57902 — receipt-ignoring, verdict-overclaiming, label-laundering, invented-deferral persist | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-28 | — |
| [#87581](https://github.com/anthropics/claude-code/issues/87581) | \[BUG\] Approving a forwarded teammate permission request with a message silently drops the message | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:agents, area:permissions, bug, has repro, platform:linux |
| [#87503](https://github.com/anthropics/claude-code/issues/87503) | \[BUG\] Cowork VM connection timeout after update to 1.32352.0 on Intel Mac (guest never connects) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, bug, has repro, platform:macos, regression |
| [#87316](https://github.com/anthropics/claude-code/issues/87316) | \[BUG\] VS Code extension silently closes and relaunches chat channels ("Closing Claude on channel") with no trigger — occasional config lock race on resume | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-17 | bug, platform:vscode, platform:wsl |
| [#80444](https://github.com/anthropics/claude-code/issues/80444) | \[Windows\] Desktop app 1.24012.1: fatal GPU-process crash (0x060C201E) via in-app Browser tab; crash leaves MSIX package unlaunchable (appxState=2) until Repair | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-07-23 | — |
| [#87539](https://github.com/anthropics/claude-code/issues/87539) | You've hit your session limit · resets 6:20am (America/New\_York) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:cost, bug, duplicate, platform:linux, platform:vscode |
| [#75043](https://github.com/anthropics/claude-code/issues/75043) | Nested subagents: children spawned by a subagent are always async (regardless of run\_in\_background), completion notifications never reach the subagent parent, and TaskStop fails with ownership errors after resume | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-07-07 | area:agents, bug, has repro, platform:macos, reproduced |
| [#87574](https://github.com/anthropics/claude-code/issues/87574) | \[FEATURE\] Configurable / per-sender color for inbound peer (@ sender ›) and channel (← source:) message labels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:tui, enhancement |
| [#84689](https://github.com/anthropics/claude-code/issues/84689) | \[BUG\] CVP approved org still blocked by cyber safeguards — org ID confirmed matching, appeal form shows no fields | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-07 | bug |
| [#87139](https://github.com/anthropics/claude-code/issues/87139) | Permission rules: $HOME not expanded during startup validation when checking symlinked config | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-16 | area:permissions, bug |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87585](https://github.com/anthropics/claude-code/issues/87585) | \[Feature Request\] Add official read-only transcript viewer for session logs | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:tui, enhancement, platform:windows |
| [#87584](https://github.com/anthropics/claude-code/issues/87584) | claude-in-chrome tools report 'extension not connected' despite extension installed, correct profile, correct account, and working chat panel | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:chrome, duplicate, platform:macos |
| [#87582](https://github.com/anthropics/claude-code/issues/87582) | \[Bug\] Model version repeatedly downgrades to 4.8 despite stable operation | OPEN | observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:model, bug, needs-repro, platform:macos |
| [#87581](https://github.com/anthropics/claude-code/issues/87581) | \[BUG\] Approving a forwarded teammate permission request with a message silently drops the message | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:agents, area:permissions, bug, has repro, platform:linux |
| [#87580](https://github.com/anthropics/claude-code/issues/87580) | Feedback prompt is a single non-scrolling line — text disappears off-screen after a few words | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:tui, bug, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87578](https://github.com/anthropics/claude-code/issues/87578) | CVP 18 days as pending after regression. (I was allowed until 30/07). Cant work like this. | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:auth, bug, needs-info, platform:linux |
| [#87577](https://github.com/anthropics/claude-code/issues/87577) | Agent SDK bundled CLI stalls after final message: transcript has complete end\_turn message, but stream-json result is never emitted | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:agent-sdk, bug, platform:macos |
| [#87576](https://github.com/anthropics/claude-code/issues/87576) | Session not found on disk — all my sessions are affected | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | bug, duplicate, platform:macos |
| [#87575](https://github.com/anthropics/claude-code/issues/87575) | \[Bug\] Auto mode system prompt causes /rewind to silently fail on Bash-edited files | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:core, area:tools, bug, has repro, platform:wsl |
| [#87574](https://github.com/anthropics/claude-code/issues/87574) | \[FEATURE\] Configurable / per-sender color for inbound peer (@ sender ›) and channel (← source:) message labels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:tui, enhancement |
| [#87573](https://github.com/anthropics/claude-code/issues/87573) | Android app: no way to edit a file directly (markdown or otherwise) | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | invalid |
| [#87572](https://github.com/anthropics/claude-code/issues/87572) | Remote Control app: file delivery via SendUserFile fails silently (red error triangle), tool reports success | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:tools, bug |
| [#87571](https://github.com/anthropics/claude-code/issues/87571) | \[Feature Request\] Add theme tokens for code block background styling | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:tui, enhancement, platform:macos |
| [#87570](https://github.com/anthropics/claude-code/issues/87570) | \[BUG\] Claude Code installer hangs indefinitely at "Setting up Claude Code..." on Windows Server 2019 — process spins CPU with no network activity | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:installation, bug, platform:windows |
| [#87569](https://github.com/anthropics/claude-code/issues/87569) | \[BUG\] Sessions that exit with live background tasks stay "active" forever — orphan reconciliation only runs on resume | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-18 | 2026-08-18 | area:agent-view, bug, has repro, platform:macos |
| [#87568](https://github.com/anthropics/claude-code/issues/87568) | \[BUG\] The new renderer causes garbled text sometimes | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:tui, bug, platform:windows, regression |
| [#87567](https://github.com/anthropics/claude-code/issues/87567) | \[BUG\] Cowork VM regression on Intel Mac (x86\_64): guest never connects after bundle 2a762ad rollout — same app version works on arm64 | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:cowork, area:desktop, duplicate, platform:macos, regression |
| [#87566](https://github.com/anthropics/claude-code/issues/87566) | \[BUG\] Sending unsupported image to third-party API permanently breaks the conversation | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:providers, bug, platform:vscode, platform:windows |
| [#87565](https://github.com/anthropics/claude-code/issues/87565) | \[BUG\]vm\_workspace\_diagnosis | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:cowork, bug, has repro, platform:macos, regression |
| [#87564](https://github.com/anthropics/claude-code/issues/87564) | You've hit your session limit · resets 11:50am (Europe/Budapest) | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:cost, bug, platform:macos |
| [#87563](https://github.com/anthropics/claude-code/issues/87563) | \[BUG\] Any link generated by the CLI that contains a URL inside parentheses is unusable | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | bug |
| [#87562](https://github.com/anthropics/claude-code/issues/87562) | Sessions sidebar: option to limit sessions shown per project/folder group | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:desktop, area:ui, enhancement, platform:windows |
| [#87561](https://github.com/anthropics/claude-code/issues/87561) | \[Bug\] Conversation compacting hangs indefinitely during token reduction and uses huge tokens | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-18 | 2026-08-18 | area:core, bug, platform:windows |
| [#87560](https://github.com/anthropics/claude-code/issues/87560) | \[BUG\] Desktop app: after auto-update stealth-relaunch, the conversation view rewinds — navigation history is saved with a stale \`active\` index | OPEN | security / trust boundary · high-signal label | 2026-08-18 | 2026-08-18 | area:desktop, bug, has repro, platform:macos |
| [#87559](https://github.com/anthropics/claude-code/issues/87559) | \[FEATURE\] Add voice/audio output for Claude's responses in Claude Code | OPEN | security / trust boundary | 2026-08-18 | 2026-08-18 | area:ide, area:tui, enhancement |

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
