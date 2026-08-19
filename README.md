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
| [#80606](https://github.com/anthropics/claude-code/issues/80606) | \[BUG\] Artifact tool not loaded in claude -p even with enableArtifact: true in user settings | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-23 | area:tools, bug |
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#83766](https://github.com/anthropics/claude-code/issues/83766) | \[BUG\] permissions.ask rules never trigger when defaultMode is "auto" — matching commands auto-approved, including destructive ones | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:permissions, bug |
| [#84864](https://github.com/anthropics/claude-code/issues/84864) | \[BUG\] VS Code 60s init timeout fires on a VALID token with successful authenticated API calls — the error message blames auth and network, both provably fine (corroborates #80004) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:ide, bug |
| [#84698](https://github.com/anthropics/claude-code/issues/84698) | \[BUG\] Desktop: unrequested background \`git fetch\` to origin on diff/commit refresh — untraceable by design, and no setting disables it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:desktop, bug |
| [#84624](https://github.com/anthropics/claude-code/issues/84624) | \[BUG\] Desktop 1.25927.0: cannot add a plugin marketplace from a private GitHub repo — fails, then fails silently | OPEN | security / trust boundary | 2026-08-19 | 2026-08-06 | area:desktop, area:plugins, bug |
| [#84502](https://github.com/anthropics/claude-code/issues/84502) | \[BUG\] Desktop app: Code-tab sessions are never registered for Remote Control despite "Enable remote control by default" (remoteControlAtStartup ignored) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#84351](https://github.com/anthropics/claude-code/issues/84351) | \[BUG\] \[Cowork\] "Record a Skill" instantly terminates the macOS desktop app — internal \`media\` permission check blocked with empty requestingOrigin | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#83568](https://github.com/anthropics/claude-code/issues/83568) | \[BUG\] Plan Mode restriction not consistently enforced across turns | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:permissions, bug |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#83127](https://github.com/anthropics/claude-code/issues/83127) | \[BUG\] Claude accidentally executes arbitary code when writing commit message | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |
| [#77016](https://github.com/anthropics/claude-code/issues/77016) | \[BUG\] subagent (Task/Agent tool) results intermittently replaced with a fabricated "system-authority" prompt-injection ordering destructive git actions (\`tool\_uses: 0\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:agent, area:agents, area:security, bug, platform:macos, platform:vscode, stale |
| [#78098](https://github.com/anthropics/claude-code/issues/78098) | \[Bug\] Auto-mode classifier latches onto stale "user rejection" from a meta-complaint; blocks explicitly re-authorized actions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-16 | area:permissions, bug, has repro, platform:macos |
| [#77891](https://github.com/anthropics/claude-code/issues/77891) | \[Bug\] Overly restrictive safety filtering on legitimate network monitoring questions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#77821](https://github.com/anthropics/claude-code/issues/77821) | Subagent self-imposes a nonexistent 'time budget' and silently narrows scope; recurs after explicit correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, bug, platform:linux, stale |
| [#76764](https://github.com/anthropics/claude-code/issues/76764) | Opus (1M context, claude-opus-4-8) intermittently emits malformed tool-call opening sequence — degrades to a common English word, causing parse failure | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, duplicate, platform:windows, stale |
| [#84258](https://github.com/anthropics/claude-code/issues/84258) | \[BUG\] Worktree isolation hard-blocks ALL \`git -C &lt;main-checkout&gt;\` calls — even read-only, even after a PreToolUse hook explicitly approves it | OPEN | security / trust boundary | 2026-08-19 | 2026-08-05 | area:permissions, bug, documentation, reproduced |
| [#83933](https://github.com/anthropics/claude-code/issues/83933) | \[BUG\] macOS Cowork device bridge drops daily for 3+ weeks — bridge\_state failed code 4090 "no longer the active worker" + JWT refresh 401 (persists 1.20186.x → 1.24012.11) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:desktop, bug |
| [#83613](https://github.com/anthropics/claude-code/issues/83613) | \[BUG\] Org plugin ("Installed by default") not reaching non-owner Member — Team plan | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:plugins, bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#80606](https://github.com/anthropics/claude-code/issues/80606) | \[BUG\] Artifact tool not loaded in claude -p even with enableArtifact: true in user settings | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-23 | area:tools, bug |
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#83766](https://github.com/anthropics/claude-code/issues/83766) | \[BUG\] permissions.ask rules never trigger when defaultMode is "auto" — matching commands auto-approved, including destructive ones | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:permissions, bug |
| [#84864](https://github.com/anthropics/claude-code/issues/84864) | \[BUG\] VS Code 60s init timeout fires on a VALID token with successful authenticated API calls — the error message blames auth and network, both provably fine (corroborates #80004) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:ide, bug |
| [#84698](https://github.com/anthropics/claude-code/issues/84698) | \[BUG\] Desktop: unrequested background \`git fetch\` to origin on diff/commit refresh — untraceable by design, and no setting disables it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:desktop, bug |
| [#84502](https://github.com/anthropics/claude-code/issues/84502) | \[BUG\] Desktop app: Code-tab sessions are never registered for Remote Control despite "Enable remote control by default" (remoteControlAtStartup ignored) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#84351](https://github.com/anthropics/claude-code/issues/84351) | \[BUG\] \[Cowork\] "Record a Skill" instantly terminates the macOS desktop app — internal \`media\` permission check blocked with empty requestingOrigin | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#83568](https://github.com/anthropics/claude-code/issues/83568) | \[BUG\] Plan Mode restriction not consistently enforced across turns | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:permissions, bug |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |
| [#77016](https://github.com/anthropics/claude-code/issues/77016) | \[BUG\] subagent (Task/Agent tool) results intermittently replaced with a fabricated "system-authority" prompt-injection ordering destructive git actions (\`tool\_uses: 0\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:agent, area:agents, area:security, bug, platform:macos, platform:vscode, stale |
| [#78098](https://github.com/anthropics/claude-code/issues/78098) | \[Bug\] Auto-mode classifier latches onto stale "user rejection" from a meta-complaint; blocks explicitly re-authorized actions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-16 | area:permissions, bug, has repro, platform:macos |
| [#77891](https://github.com/anthropics/claude-code/issues/77891) | \[Bug\] Overly restrictive safety filtering on legitimate network monitoring questions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#77821](https://github.com/anthropics/claude-code/issues/77821) | Subagent self-imposes a nonexistent 'time budget' and silently narrows scope; recurs after explicit correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, bug, platform:linux, stale |
| [#76764](https://github.com/anthropics/claude-code/issues/76764) | Opus (1M context, claude-opus-4-8) intermittently emits malformed tool-call opening sequence — degrades to a common English word, causing parse failure | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, duplicate, platform:windows, stale |
| [#83933](https://github.com/anthropics/claude-code/issues/83933) | \[BUG\] macOS Cowork device bridge drops daily for 3+ weeks — bridge\_state failed code 4090 "no longer the active worker" + JWT refresh 401 (persists 1.20186.x → 1.24012.11) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:desktop, bug |
| [#83613](https://github.com/anthropics/claude-code/issues/83613) | \[BUG\] Org plugin ("Installed by default") not reaching non-owner Member — Team plan | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:plugins, bug |
| [#83428](https://github.com/anthropics/claude-code/issues/83428) | \[BUG\] Desktop: MCP servers needing Calendar/Reminders (EventKit) access still get silently denied — recurring, previously reported and auto-closed as stale (#55692, #76936, #58239) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-02 | area:desktop, area:mcp, bug |
| [#80600](https://github.com/anthropics/claude-code/issues/80600) | \[BUG\] Cached experiment payload injects system-prompt directives indefinitely; \`CLAUDE\_CODE\_DISABLE\_NONESSENTIAL\_TRAFFIC\` gates the fetch but not the read | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-23 | area:core, bug |
| [#81310](https://github.com/anthropics/claude-code/issues/81310) | \[BUG\] file-index-worker fails on all sessions rooted in ~/Documents (sandboxed git cannot read TCC-protected dirs) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:desktop, bug |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88087](https://github.com/anthropics/claude-code/issues/88087) | \[BUG\] Desktop app CCD UserDialogBroker cancels every unknown dialog kind, making AskUserQuestion abort 100% of the time (root cause + proposed fix) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:tools, bug, has repro, platform:macos |
| [#88086](https://github.com/anthropics/claude-code/issues/88086) | VS Code extension: SessionStart plugin hook additionalContext logged as succeeded but never injected into model context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:hooks, area:plugins, bug, has repro, platform:macos, platform:vscode |
| [#88085](https://github.com/anthropics/claude-code/issues/88085) | Feature request: "agent-hours" — a labor metric for agent teams (sum of active agent time) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-19 | area:agents, area:cost, enhancement |
| [#88083](https://github.com/anthropics/claude-code/issues/88083) | \[BUG\] Long-lived --bg-pty-host process caches revoked macOS TCC grants; /exit and new terminals reattach to it, so file access cannot be restored without killing the daemon | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:macos |
| [#88082](https://github.com/anthropics/claude-code/issues/88082) | \[BUG\] Session working directory becomes permanently unresolvable after using a git worktree (background job), breaking Bash, file tools, and the /cd command | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:bash, area:tools, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88080](https://github.com/anthropics/claude-code/issues/88080) | \[Bug\] Fable 5 safeguards flag triggering unexpectedly | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:macos |
| [#88077](https://github.com/anthropics/claude-code/issues/88077) | Rewind: disabling fileCheckpointingEnabled also removes both Summarize options | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:linux |
| [#88075](https://github.com/anthropics/claude-code/issues/88075) | \[BUG\] Claude Code v2.1.235 advertises empty \`elicitation: {}\` on MCP 2026-07-28 — URL-mode elicitation (InputRequiredResult) cannot be fulfilled | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:mcp, bug, has repro |
| [#88049](https://github.com/anthropics/claude-code/issues/88049) | MCP: one non-object tool inputSchema silently drops ALL tools from an HTTP server (no error either side) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:mcp, bug, has repro, platform:windows |
| [#88041](https://github.com/anthropics/claude-code/issues/88041) | \[Bug\] Auto-mode "bashFirst" system prompt instructs sed/heredoc file edits instead of Edit/Write tools | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, area:tools, bug, platform:linux |
| [#87575](https://github.com/anthropics/claude-code/issues/87575) | \[Bug\] Auto mode system prompt causes /rewind to silently fail on Bash-edited files | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-18 | area:core, area:tools, bug, has repro, platform:wsl |
| [#87509](https://github.com/anthropics/claude-code/issues/87509) | \[BUG\] Windows Desktop: cross-session send\_message reports success and renders in the target UI, but is never enqueued/persisted (ghost delivery, lost on restart) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | area:agents, area:desktop, bug, platform:windows |
| [#87194](https://github.com/anthropics/claude-code/issues/87194) | \[BUG\] Claude Desktop 1.30096.5 hangs before creating a window on macOS | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-16 | invalid |
| [#87117](https://github.com/anthropics/claude-code/issues/87117) | Projects tool: project\_write silently destroys document content, with no append mode, no version history, and no recovery | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-16 | invalid |
| [#87086](https://github.com/anthropics/claude-code/issues/87086) | \[EVAL/TRANSPARENCY\] Anthropic's regulation case rests on internal evals — apply the #86979 provenance standard to Glasswing and 'When AI Builds Itself' | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-16 | invalid |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86158](https://github.com/anthropics/claude-code/issues/86158) | \[Bug\] Anthropic API Error: Content Flagged by Sonnet 5 Safeguards | CLOSED / NOT\_PLANNED | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:model, bug, needs-repro, platform:macos |
| [#86002](https://github.com/anthropics/claude-code/issues/86002) | \[BUG\] SDK auth failed: redirect URI host "localhost:55385" is no longer supported (sunset 2026-08-01) | CLOSED / COMPLETED | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-12 | api:bedrock, area:auth, area:mcp, bug, platform:macos |
| [#85587](https://github.com/anthropics/claude-code/issues/85587) | \[BUG\] Plan file intermittently reported as non-existent while composing inline comments; unsaved comment text is lost | OPEN | security / trust boundary | 2026-08-19 | 2026-08-10 | area:desktop, bug |
| [#85459](https://github.com/anthropics/claude-code/issues/85459) | \[BUG/MODEL\] Model told incorrectly that all bash commands are blocked | OPEN | security / trust boundary | 2026-08-19 | 2026-08-10 | area:permissions, bug |
| [#85264](https://github.com/anthropics/claude-code/issues/85264) | \[BUG\] fork subagents spawn unauthorized nested sub-agents; at least one fabricated a completion report and wrote false claims into persistent memory/project files | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-09 | area:agents, bug |
| [#85212](https://github.com/anthropics/claude-code/issues/85212) | \[BUG\] Crashes and freezes are concentrated during operations like "searching for literature | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-09 | area:desktop, bug |
| [#85181](https://github.com/anthropics/claude-code/issues/85181) | \[BUG\] Session process restarts orphaning background tasks + lost tool results + MCP disconnect cycles | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-09 | area:core, bug |
| [#85174](https://github.com/anthropics/claude-code/issues/85174) | \[BUG\] Windows desktop app (MSIX) uninstalls itself and wipes all local data during silent auto-update when background sessions are running | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-09 | area:desktop, bug |
| [#85119](https://github.com/anthropics/claude-code/issues/85119) | \[BUG\] VS Code extension ignores WebFetch and WebSearch permission rules; CLI honors them | OPEN | security / trust boundary | 2026-08-19 | 2026-08-08 | area:ide, area:permissions, bug |

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
