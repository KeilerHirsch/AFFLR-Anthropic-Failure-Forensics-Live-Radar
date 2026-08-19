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
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79439](https://github.com/anthropics/claude-code/issues/79439) | \[BUG\] Consantly getting: API Error: Stream idle timeout - no chunks received | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-20 | api:anthropic, area:networking, bug, duplicate, platform:windows |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#83380](https://github.com/anthropics/claude-code/issues/83380) | Credential handoff for browser logins: password manager integration for headless/mobile sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-02 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#11139](https://github.com/anthropics/claude-code/issues/11139) | \[BUG\] Claude Code Web Cannot Use gh CLI Commands (Permission Denied) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-11-06 | area:claude-code-web, area:core, area:tools, bug, has repro, oncall, platform:linux |
| [#8961](https://github.com/anthropics/claude-code/issues/8961) | Claude Code ignores deny rules in .claude/settings.local.json - security vulnerability | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-10-05 | area:core, area:permissions, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#79439](https://github.com/anthropics/claude-code/issues/79439) | \[BUG\] Consantly getting: API Error: Stream idle timeout - no chunks received | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-20 | api:anthropic, area:networking, bug, duplicate, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#83380](https://github.com/anthropics/claude-code/issues/83380) | Credential handoff for browser logins: password manager integration for headless/mobile sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-02 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#65036](https://github.com/anthropics/claude-code/issues/65036) | \[BUG\] MCP OAuth: Claude doesn't auto-refresh access tokens, daily "Connection expired" despite valid refresh token | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-03 | area:auth, area:mcp, bug |
| [#4540](https://github.com/anthropics/claude-code/issues/4540) | \[BUG\] Missing \`scope\` Parameter in Dynamic Client Registration and Authorization Requests | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2025-07-27 | area:auth, area:mcp, bug, has repro, oncall |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88044](https://github.com/anthropics/claude-code/issues/88044) | \[BUG\] Desktop app (Windows): delivered file cards open a claude.ai /api/.../files/{id}/contents URL in the browser — 404s or save-as with a corrupted filename | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, bug, platform:windows |
| [#88043](https://github.com/anthropics/claude-code/issues/88043) | \[BUG\] Desktop app hides "Auto" permission mode and shows "Bypass permissions — Disabled by your organization" on a personal Claude Max account (CLI unaffected) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, area:permissions, bug, platform:macos, regression |
| [#88042](https://github.com/anthropics/claude-code/issues/88042) | \[Bug\] Normal app workflows trigger Claude's safety guidelines | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:macos |
| [#88041](https://github.com/anthropics/claude-code/issues/88041) | \[Bug\] Auto-mode "bashFirst" system prompt instructs sed/heredoc file edits instead of Edit/Write tools | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, area:tools, bug, platform:linux |
| [#88039](https://github.com/anthropics/claude-code/issues/88039) | \[Bug\] /advisor silently omits Fable 5 when ANTHROPIC\_BASE\_URL is set, despite first-party OAuth login and cached Fable entitlement | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:self-hosted-environments, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88038](https://github.com/anthropics/claude-code/issues/88038) | Write tool does not enforce the working-directory sandbox that Bash enforces | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:permissions, area:sandbox, area:security, bug, has repro, platform:macos |
| [#88036](https://github.com/anthropics/claude-code/issues/88036) | \[BUG\] | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, bug, duplicate, platform:macos |
| [#88035](https://github.com/anthropics/claude-code/issues/88035) | Background forked skill completes before its subagents finish; SendMessage resume then fails with contradictory state | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, bug, platform:macos |
| [#88033](https://github.com/anthropics/claude-code/issues/88033) | \[BUG\] Windows service (CoworkVMService) flaps disabled/enabled during MSIX auto-update, blocked by EBUSY on chrome-native-host.exe | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:cowork, area:desktop, area:mcp, bug, has repro, platform:windows |
| [#88032](https://github.com/anthropics/claude-code/issues/88032) | \[MODEL\] Sonnet 5 | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | api:anthropic, area:model, bug, model |
| [#88029](https://github.com/anthropics/claude-code/issues/88029) | sandbox.enabled: true causes unbounded memory growth at startup, OOM (2.1.233-2.1.235, WSL2) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, bug, has repro, platform:wsl |
| [#88028](https://github.com/anthropics/claude-code/issues/88028) | \[BUG\] Claude Desktop (Windows) does not restore window positions/sizes after lock/unlock | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | invalid |
| [#88027](https://github.com/anthropics/claude-code/issues/88027) | \[BUG\] Webview CSS: six custom properties are referenced but never defined, plus two light-background issues | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:ide, area:ui, bug, has repro, platform:vscode, platform:windows |
| [#88026](https://github.com/anthropics/claude-code/issues/88026) | \[BUG\] Computer use returns black/empty screenshots on Intel i3 iGPU — Windows 11 Home, worked before system reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | invalid |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#88023](https://github.com/anthropics/claude-code/issues/88023) | Project custom agents (.claude/agents/) become unavailable to Agent tool after /compact, in same session, no worktree transition | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, bug, has repro, platform:macos |
| [#88021](https://github.com/anthropics/claude-code/issues/88021) | \[BUG\] auto mode can be remotely enabled by attacker | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:security, bug, platform:macos |
| [#88020](https://github.com/anthropics/claude-code/issues/88020) | \[FEATURE\] Desktop: named split-view layouts with lockable cells | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:ui, enhancement |
| [#88014](https://github.com/anthropics/claude-code/issues/88014) | \[Bug\] Cybersecurity classifier blocking defensive malware analysis tooling mid-conversation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, platform:macos |
| [#88010](https://github.com/anthropics/claude-code/issues/88010) | \[BUG\] Desktop app crashes when git repo discovery resolves to a stray ancestor .git above the project folder (Windows) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, bug, has repro, platform:windows |
| [#88005](https://github.com/anthropics/claude-code/issues/88005) | \[BUG\] Cowork stays pinned to stale plugin version from custom git marketplace; marketplace cannot be removed or re-added | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, area:plugins, bug |
| [#88004](https://github.com/anthropics/claude-code/issues/88004) | \[BUG\] Navigating left to the task list, then right into a new task, breaks the session with a misleading "login required" error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, area:auth, area:tui, bug, platform:linux |
| [#88001](https://github.com/anthropics/claude-code/issues/88001) | Background agent completion notification lost after messaging the agent mid-run | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#87995](https://github.com/anthropics/claude-code/issues/87995) | \[Bug\] ultrareview: All reviewer agents terminate at Verify stage, Dedupe never executes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:cost, area:skills, duplicate, platform:macos |

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
