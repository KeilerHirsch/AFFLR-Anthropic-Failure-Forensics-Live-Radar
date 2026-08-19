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
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#83380](https://github.com/anthropics/claude-code/issues/83380) | Credential handoff for browser logins: password manager integration for headless/mobile sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-02 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-06-17 | area:model, bug |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#83380](https://github.com/anthropics/claude-code/issues/83380) | Credential handoff for browser logins: password manager integration for headless/mobile sessions | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-02 | — |
| [#88000](https://github.com/anthropics/claude-code/issues/88000) | \[Opus 5\] Model insult to user | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | model |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |
| [#75291](https://github.com/anthropics/claude-code/issues/75291) | Structured user memory: typed graph + fetch-before-cite, on every surface | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-07 | enhancement, memory, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88039](https://github.com/anthropics/claude-code/issues/88039) | \[Bug\] /advisor silently omits Fable 5 when ANTHROPIC\_BASE\_URL is set, despite first-party OAuth login and cached Fable entitlement | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:self-hosted-environments, bug, has repro, platform:macos |
| [#88038](https://github.com/anthropics/claude-code/issues/88038) | Write tool does not enforce the working-directory sandbox that Bash enforces | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, area:security, bug, has repro, platform:macos |
| [#88036](https://github.com/anthropics/claude-code/issues/88036) | \[BUG\] | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:core, bug, duplicate, platform:macos |
| [#88035](https://github.com/anthropics/claude-code/issues/88035) | Background forked skill completes before its subagents finish; SendMessage resume then fails with contradictory state | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, bug, platform:macos |
| [#88033](https://github.com/anthropics/claude-code/issues/88033) | \[BUG\] Windows service (CoworkVMService) flaps disabled/enabled during MSIX auto-update, blocked by EBUSY on chrome-native-host.exe | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:cowork, area:mcp, bug, has repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88032](https://github.com/anthropics/claude-code/issues/88032) | \[MODEL\] Sonnet 5 | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | api:anthropic, area:model, bug, model |
| [#88031](https://github.com/anthropics/claude-code/issues/88031) | Desktop: add a persistent setting to always open chat links in the system default browser | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, enhancement, platform:macos |
| [#88029](https://github.com/anthropics/claude-code/issues/88029) | sandbox.enabled: true causes unbounded memory growth at startup, OOM (2.1.233-2.1.235, WSL2) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:sandbox, bug, has repro, platform:wsl |
| [#88028](https://github.com/anthropics/claude-code/issues/88028) | \[BUG\] Claude Desktop (Windows) does not restore window positions/sizes after lock/unlock | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | invalid |
| [#88027](https://github.com/anthropics/claude-code/issues/88027) | \[BUG\] Webview CSS: six custom properties are referenced but never defined, plus two light-background issues | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:ui, bug, has repro, platform:vscode, platform:windows |
| [#88026](https://github.com/anthropics/claude-code/issues/88026) | \[BUG\] Computer use returns black/empty screenshots on Intel i3 iGPU — Windows 11 Home, worked before system reset | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | invalid |
| [#88025](https://github.com/anthropics/claude-code/issues/88025) | Option to collapse/hide Edit and Write tool-call diffs in the CLI transcript | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:tui, enhancement |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#88023](https://github.com/anthropics/claude-code/issues/88023) | Project custom agents (.claude/agents/) become unavailable to Agent tool after /compact, in same session, no worktree transition | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, bug, has repro, platform:macos |
| [#88021](https://github.com/anthropics/claude-code/issues/88021) | \[BUG\] auto mode can be remotely enabled by attacker | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:permissions, area:security, bug, platform:macos |
| [#88020](https://github.com/anthropics/claude-code/issues/88020) | \[FEATURE\] Desktop: named split-view layouts with lockable cells | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:desktop, area:ui, enhancement |
| [#88018](https://github.com/anthropics/claude-code/issues/88018) | \[BUG\] Android app renders slash-command messages without their arguments | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:ui, bug, platform:android |
| [#88017](https://github.com/anthropics/claude-code/issues/88017) | \[BUG\] Multiple terminals attached to the same live session have locked/synced scroll position, and resizing one corrupts rendering in the other | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#88015](https://github.com/anthropics/claude-code/issues/88015) | \[Bug\] Anthropic API Error: Server rate limiting during request processing | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:anthropic, area:api, bug, platform:windows |
| [#88014](https://github.com/anthropics/claude-code/issues/88014) | \[Bug\] Cybersecurity classifier blocking defensive malware analysis tooling mid-conversation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, platform:macos |
| [#88012](https://github.com/anthropics/claude-code/issues/88012) | Desktop app: top-level "+ New" always prompts for a folder (regression, no longer remembers last working directory) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:desktop, bug, platform:windows, regression |
| [#88010](https://github.com/anthropics/claude-code/issues/88010) | \[BUG\] Desktop app crashes when git repo discovery resolves to a stray ancestor .git above the project folder (Windows) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, bug, has repro, platform:windows |
| [#88008](https://github.com/anthropics/claude-code/issues/88008) | Cowork MSIX stays Staged (0x80073D28, packaged service CoworkVMService) for standard users under machine-wide Add-AppxProvisionedPackage in split-account enterprise | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |
| [#88006](https://github.com/anthropics/claude-code/issues/88006) | iOS Simulator MCP: no way to pass launch arguments to the app (control action:"launch" runs bare simctl launch; \`text\` is silently ignored) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:mcp, enhancement, platform:macos |
| [#88005](https://github.com/anthropics/claude-code/issues/88005) | \[BUG\] Cowork stays pinned to stale plugin version from custom git marketplace; marketplace cannot be removed or re-added | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | bug |

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
