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
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |
| [#56268](https://github.com/anthropics/claude-code/issues/56268) | claude -p silent-freeze when spawned from a long-running orchestrator (no stdout, deterministic 100% from direct spawn, probabilistic with bash wrap) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-05 | area:cli, bug, has repro, platform:linux, stale |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#58513](https://github.com/anthropics/claude-code/issues/58513) | \[Bug\] Permission-mode cycling causes misplaced system-reminder attachments flagged as prompt injection | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-12 | area:permissions, area:tui, bug, platform:linux |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#49136](https://github.com/anthropics/claude-code/issues/49136) | Feature Request: SSH-agent-style credential forwarding for remote Claude Code sessions | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-16 | area:auth, area:security, enhancement |
| [#48011](https://github.com/anthropics/claude-code/issues/48011) | \[FEATURE\] Make OAuth/admin base URL configurable like ANTHROPIC\_BASE\_URL | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-04-14 | area:auth, enhancement |
| [#58768](https://github.com/anthropics/claude-code/issues/58768) | AskUserQuestion answers invisible to auto-mode permission classifier — destructive calls re-blocked after explicit consent | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-13 | area:permissions, area:tools, bug, stale |
| [#56268](https://github.com/anthropics/claude-code/issues/56268) | claude -p silent-freeze when spawned from a long-running orchestrator (no stdout, deterministic 100% from direct spawn, probabilistic with bash wrap) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-05-05 | area:cli, bug, has repro, platform:linux, stale |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87938](https://github.com/anthropics/claude-code/issues/87938) | \[BUG\] cyber safeguard model-fallback is now session-scoped (2.1.229) and false-positives on legitimate security work — reproduced live on Opus 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:security, bug, has repro |
| [#87920](https://github.com/anthropics/claude-code/issues/87920) | \[BUG\] Bash sleep-block guidance prescribes the Monitor tool in sessions where the harness itself reports "Monitor is disabled for this session" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:linux |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-14 | area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#76700](https://github.com/anthropics/claude-code/issues/76700) | Background Opus subagents intermittently stall on first turn, leaking system-prompt fragments (incl. authorization-shaped text) as their only output | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:security, bug, has repro, platform:windows, stale |
| [#76648](https://github.com/anthropics/claude-code/issues/76648) | Formal Complaint — Recurring False-Positive Safeguard Flags on Claude Fable 5 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, model, platform:vscode, stale |
| [#76620](https://github.com/anthropics/claude-code/issues/76620) | \[Bug\] Fable 5 safeguards persistently escalate a benign health-corpus + security-governance project to Opus | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, area:security, bug, platform:macos, stale |
| [#76583](https://github.com/anthropics/claude-code/issues/76583) | \[Bug\] Cyber Safeguard false positives blocking defensive monitoring work at session start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | api:anthropic, area:model, area:security, bug, platform:linux, stale |
| [#76561](https://github.com/anthropics/claude-code/issues/76561) | Credential writes replace symlinks and clobber shared state: concurrent instances sharing .credentials.json cascade each other (and the user) to logged-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:agents, area:auth, bug, platform:wsl, stale |
| [#75655](https://github.com/anthropics/claude-code/issues/75655) | \[BUG\] Fable 5 appended a fabricated user turn to the end of its own assistant response (JSONL-verified, ~30% of 1M context) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-08 | area:model, duplicate, has repro, platform:windows, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#68249](https://github.com/anthropics/claude-code/issues/68249) | Permission model forces an unsafe binary (alarm fatigue vs. full bypass) — make risk-stratified approval available to individual users | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-13 | duplicate |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#58513](https://github.com/anthropics/claude-code/issues/58513) | \[Bug\] Permission-mode cycling causes misplaced system-reminder attachments flagged as prompt injection | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-12 | area:permissions, area:tui, bug, platform:linux |
| [#59904](https://github.com/anthropics/claude-code/issues/59904) | \[FEATURE\] Dreaming: surface CLAUDE.md promotion candidates to humans | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-05-17 | enhancement, memory, stale |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-24 | — |
| [#75949](https://github.com/anthropics/claude-code/issues/75949) | Fable 5 safeguard false positive (category: cyber) on routine platform-engineering code causes silent, sticky model downgrade to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-09 | stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87997](https://github.com/anthropics/claude-code/issues/87997) | Expose session name as a variable (e.g. $session\_name) for use in shell/loop commands | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87996](https://github.com/anthropics/claude-code/issues/87996) | Background-session git rule "Never push to main/master, force-push, or merge" has no precedence clause, so agents refuse merges their repo CLAUDE.md explicitly requires | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | — |
| [#87995](https://github.com/anthropics/claude-code/issues/87995) | \[Bug\] ultrareview: All reviewer agents terminate at Verify stage, Dedupe never executes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:cost, area:skills, duplicate, platform:macos |
| [#87994](https://github.com/anthropics/claude-code/issues/87994) | Background subagents (e.g. via /code-review) silently auto-deny gated Bash commands instead of prompting | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, area:permissions, bug, has repro, platform:windows |
| [#87993](https://github.com/anthropics/claude-code/issues/87993) | Claude in Chrome: silent-reauth failure latches startupReauthState={terminal:true} with no cooldown, permanently killing the bridge until manual sign-out/sign-in | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87992](https://github.com/anthropics/claude-code/issues/87992) | \[Bug\] Anthropic API Error: False positive safety classifier blocking legitimate mental health detection software | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, duplicate, platform:linux, platform:vscode |
| [#87991](https://github.com/anthropics/claude-code/issues/87991) | OTEL\_RESOURCE\_ATTRIBUTES set via settings.json env or OS-level env var never applied to Claude Code's own OTLP export | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:windows |
| [#87988](https://github.com/anthropics/claude-code/issues/87988) | \[FEATURE\] | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:ide, enhancement, platform:intellij, platform:windows |
| [#87987](https://github.com/anthropics/claude-code/issues/87987) | Subagent stream dies silently on transient network failure — no retry/reconnect, watchdog kills after 600s of silence | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agents, area:networking, duplicate, has repro, platform:windows |
| [#87986](https://github.com/anthropics/claude-code/issues/87986) | \[Bug\] Claude Code performance degradation after service outage - Opus 5.0 failing basic tasks | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, area:tui, bug, platform:windows |
| [#87985](https://github.com/anthropics/claude-code/issues/87985) | Ink UI leaves stale placeholder text when TERM\_PROGRAM=ghostty and new content is shorter | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:linux |
| [#87984](https://github.com/anthropics/claude-code/issues/87984) | \[BUG\] Backgrounding a conversation (left arrow) continues it under a new session id; --resume shows a stalled duplicate of the original | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:macos |
| [#87983](https://github.com/anthropics/claude-code/issues/87983) | \[BUG\] \`claude -p "/usage" --output-format json\` intermittently fails right after a long print-mode run — exit 5, or \`is\_error:false\` envelope with no \`result\` | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, bug, platform:linux |
| [#87982](https://github.com/anthropics/claude-code/issues/87982) | \[Bug\] Firefox browser not supported by Claude Code CLI | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:cli, enhancement, platform:windows |
| [#87981](https://github.com/anthropics/claude-code/issues/87981) | Pre-commit hook interaction leads Claude Code to rm -rf files from a concurrent, unrelated session | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:hooks, bug, data-loss, platform:macos |
| [#87980](https://github.com/anthropics/claude-code/issues/87980) | Windows regression in 2.1.235: PowerShell tool fails from Git Bash with \`--model haiku\` (\`pwsh exited with code 1\`) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:permissions, bug, has repro, platform:windows, regression |
| [#87979](https://github.com/anthropics/claude-code/issues/87979) | Feature request: bind --watch-artifact to an existing session; make auto-acknowledgment replies optional | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:agents, area:cli, enhancement |
| [#87978](https://github.com/anthropics/claude-code/issues/87978) | \[A11y\] CLI with VoiceOver: no way to know when a turn is done, and streaming output is exhausting to listen to | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:a11y, area:tui, enhancement, platform:macos |
| [#87977](https://github.com/anthropics/claude-code/issues/87977) | \[A11y\] macOS desktop app: VoiceOver navigation jumps the cursor around; sidebar and sessions hard to move through | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:a11y, area:desktop, bug, platform:macos |
| [#87974](https://github.com/anthropics/claude-code/issues/87974) | Out-of-bounds read past end of 1 GiB mapping on CPUs without AVX/SSE4 (SIGSEGV, not SIGILL) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:packaging, duplicate, platform:linux |
| [#87973](https://github.com/anthropics/claude-code/issues/87973) | \[FEATURE\] Option to COMPLETELY disable "accept edits" on | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:permissions, enhancement |
| [#87970](https://github.com/anthropics/claude-code/issues/87970) | I don't see a bug report in the content you've shared. What you've provided is an email from Anthropic's Safeguards Team confirming approval into the Cyber Verification Program (CVP).  To generate a GitHub issue title for Claude Code, I would need:  1. A d | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:tui, bug, platform:linux |
| [#87968](https://github.com/anthropics/claude-code/issues/87968) | Backgrounding a named session duplicates its name in the session list | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:agent-view, bug, has repro, platform:macos |
| [#87967](https://github.com/anthropics/claude-code/issues/87967) | Worktree isolation: session guidance suggests the ! prefix as a workaround, but ! runs in the same session and hits the identical block | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:bash, area:sandbox, bug, reproduced |
| [#87965](https://github.com/anthropics/claude-code/issues/87965) | Model fabricates a "prompt injection" incident — quotes a fake attack string that never appears in any tool\_result | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | api:bedrock, area:model, bug |

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
