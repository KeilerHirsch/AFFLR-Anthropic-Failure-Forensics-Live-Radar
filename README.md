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
| [#87042](https://github.com/anthropics/claude-code/issues/87042) | \[MODEL\] | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:security, area:tools, bug, model |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:permissions, area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#86655](https://github.com/anthropics/claude-code/issues/86655) | PreToolUse hook on \`Edit\|Write\` is invoked and reaches a verdict, but its exit 2 is not enforced (Windows, agent-frontmatter and settings.json carriers) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-14 | area:hooks, area:security, bug, has repro, platform:windows |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#77045](https://github.com/anthropics/claude-code/issues/77045) | \[BUG\] Sandbox network allowedDomains not enforced on macOS: built-in proxy CONNECTs to non-allowlisted hosts (CLI 2.1.205) | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-07-13 | area:sandbox, area:security, bug, has repro, platform:macos |
| [#80606](https://github.com/anthropics/claude-code/issues/80606) | \[BUG\] Artifact tool not loaded in claude -p even with enableArtifact: true in user settings | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-23 | area:tools, bug |
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#86630](https://github.com/anthropics/claude-code/issues/86630) | \[Bug\] Windows-only permission gate in 2.1.232 bypasses auto mode classifier and overrides \`permissions.allow\` rules | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:permissions, bug, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | — |
| [#83766](https://github.com/anthropics/claude-code/issues/83766) | \[BUG\] permissions.ask rules never trigger when defaultMode is "auto" — matching commands auto-approved, including destructive ones | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:permissions, bug |
| [#84864](https://github.com/anthropics/claude-code/issues/84864) | \[BUG\] VS Code 60s init timeout fires on a VALID token with successful authenticated API calls — the error message blames auth and network, both provably fine (corroborates #80004) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:ide, bug |
| [#84698](https://github.com/anthropics/claude-code/issues/84698) | \[BUG\] Desktop: unrequested background \`git fetch\` to origin on diff/commit refresh — untraceable by design, and no setting disables it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:desktop, bug |
| [#84624](https://github.com/anthropics/claude-code/issues/84624) | \[BUG\] Desktop 1.25927.0: cannot add a plugin marketplace from a private GitHub repo — fails, then fails silently | OPEN | security / trust boundary | 2026-08-19 | 2026-08-06 | area:desktop, area:plugins, bug |
| [#84502](https://github.com/anthropics/claude-code/issues/84502) | \[BUG\] Desktop app: Code-tab sessions are never registered for Remote Control despite "Enable remote control by default" (remoteControlAtStartup ignored) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#83568](https://github.com/anthropics/claude-code/issues/83568) | \[BUG\] Plan Mode restriction not consistently enforced across turns | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:permissions, bug |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#83127](https://github.com/anthropics/claude-code/issues/83127) | \[BUG\] Claude accidentally executes arbitary code when writing commit message | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87042](https://github.com/anthropics/claude-code/issues/87042) | \[MODEL\] | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:security, area:tools, bug, model |
| [#86667](https://github.com/anthropics/claude-code/issues/86667) | Claude Code bypassed a blocked system-path guard via 'cmd /c rd', then a destructive command silently continued unsupervised in the background after timeout — wiped C:\\ drive root | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:permissions, area:sandbox, area:security, bug, data-loss, has repro, high-priority, platform:windows |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#80606](https://github.com/anthropics/claude-code/issues/80606) | \[BUG\] Artifact tool not loaded in claude -p even with enableArtifact: true in user settings | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-23 | area:tools, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#86630](https://github.com/anthropics/claude-code/issues/86630) | \[Bug\] Windows-only permission gate in 2.1.232 bypasses auto mode classifier and overrides \`permissions.allow\` rules | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:permissions, bug, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#80988](https://github.com/anthropics/claude-code/issues/80988) | \[BUG\] v2.1.219 \`heron\_brook\` prompt section injects "Do not call the AgentTool unless the user requested it" for Opus 5 only, silently overriding user-configured delegation policy, with no opt-out | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | — |
| [#83766](https://github.com/anthropics/claude-code/issues/83766) | \[BUG\] permissions.ask rules never trigger when defaultMode is "auto" — matching commands auto-approved, including destructive ones | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-04 | area:permissions, bug |
| [#84864](https://github.com/anthropics/claude-code/issues/84864) | \[BUG\] VS Code 60s init timeout fires on a VALID token with successful authenticated API calls — the error message blames auth and network, both provably fine (corroborates #80004) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:ide, bug |
| [#84698](https://github.com/anthropics/claude-code/issues/84698) | \[BUG\] Desktop: unrequested background \`git fetch\` to origin on diff/commit refresh — untraceable by design, and no setting disables it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-07 | area:desktop, bug |
| [#84502](https://github.com/anthropics/claude-code/issues/84502) | \[BUG\] Desktop app: Code-tab sessions are never registered for Remote Control despite "Enable remote control by default" (remoteControlAtStartup ignored) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | area:desktop, bug |
| [#83568](https://github.com/anthropics/claude-code/issues/83568) | \[BUG\] Plan Mode restriction not consistently enforced across turns | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-03 | area:permissions, bug |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |
| [#77016](https://github.com/anthropics/claude-code/issues/77016) | \[BUG\] subagent (Task/Agent tool) results intermittently replaced with a fabricated "system-authority" prompt-injection ordering destructive git actions (\`tool\_uses: 0\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:agent, area:agents, area:security, bug, platform:macos, platform:vscode, stale |
| [#86619](https://github.com/anthropics/claude-code/issues/86619) | \[BUG\] Windows Git Bash: static analysis false-positives on read-only cd-compound commands cause constant, unsuppressable permission prompts (since 2.1.232 / auto-mode rollout) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:bash, area:permissions, bug, has repro, platform:windows |
| [#78098](https://github.com/anthropics/claude-code/issues/78098) | \[Bug\] Auto-mode classifier latches onto stale "user rejection" from a meta-complaint; blocks explicitly re-authorized actions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-16 | area:permissions, bug, has repro, platform:macos |
| [#77821](https://github.com/anthropics/claude-code/issues/77821) | Subagent self-imposes a nonexistent 'time budget' and silently narrows scope; recurs after explicit correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, bug, platform:linux, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88106](https://github.com/anthropics/claude-code/issues/88106) | deep-research workflow: rate-limited verify votes are now reported honestly (#69883) but never retried — bounded retry-with-backoff recovers them (working patch included) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:agents, enhancement |
| [#88105](https://github.com/anthropics/claude-code/issues/88105) | \[BUG\] Auto-update to 2.1.237 leaves broken stub on Windows: claude-code-win32-x64@2.1.237 missing from npm registry (incomplete release) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:installation, area:packaging, bug, has repro, platform:windows |
| [#88104](https://github.com/anthropics/claude-code/issues/88104) | Claude in Chrome side panel: re-auth flow fails with "claude.ai refused to connect" (frame-blocked) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | invalid |
| [#88103](https://github.com/anthropics/claude-code/issues/88103) | \[BUG\] 2.1.237 tagged \`latest\` with its linux-x64, win32-x64 and linux-x64-musl native packages never published - installs land on a dead 500-byte stub | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:packaging, bug, has repro, high-priority, platform:linux, platform:windows |
| [#88102](https://github.com/anthropics/claude-code/issues/88102) | \[BUG\] Channels (research preview): async MCP tool calls hang when the same streamable-HTTP server is bound as a channel source | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88098](https://github.com/anthropics/claude-code/issues/88098) | \[BUG\] Claude Desktop freezes (spinning pinwheel) on Code tab and mic permission prompt on macOS 26.5.2 — reproduces in brand-new macOS user account | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:macos |
| [#88096](https://github.com/anthropics/claude-code/issues/88096) | MODEL444564531230..0 | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | model |
| [#88095](https://github.com/anthropics/claude-code/issues/88095) | VSCode extension: empty &lt;pre id="claude-error"&gt; forces a permanent 1px horizontal scrollbar in the webview | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:ide, bug, has repro, platform:macos, platform:vscode |
| [#88094](https://github.com/anthropics/claude-code/issues/88094) | \[BUG\] Remote Control Being Turned on by Default | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:tui, bug, platform:windows |
| [#88091](https://github.com/anthropics/claude-code/issues/88091) | Concurrent \`claude\` sessions racing on npm-global auto-update causes ENOTEMPTY + missing native binary | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:installation, area:packaging, bug, has repro, platform:macos |
| [#88088](https://github.com/anthropics/claude-code/issues/88088) | \[BUG\] Large sessions silently stop syncing to web/mobile, then fail to unarchive — host process running and connected throughout | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-19 | area:core, bug, platform:linux |
| [#88087](https://github.com/anthropics/claude-code/issues/88087) | \[BUG\] Desktop app CCD UserDialogBroker cancels every unknown dialog kind, making AskUserQuestion abort 100% of the time (root cause + proposed fix) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:desktop, area:tools, bug, has repro, platform:macos |
| [#88083](https://github.com/anthropics/claude-code/issues/88083) | \[BUG\] Long-lived --bg-pty-host process caches revoked macOS TCC grants; /exit and new terminals reattach to it, so file access cannot be restored without killing the daemon | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:core, bug, has repro, platform:macos |
| [#88080](https://github.com/anthropics/claude-code/issues/88080) | \[Bug\] Fable 5 safeguards flag triggering unexpectedly | OPEN | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:model, bug, needs-repro, platform:macos |
| [#88075](https://github.com/anthropics/claude-code/issues/88075) | \[BUG\] Claude Code v2.1.235 advertises empty \`elicitation: {}\` on MCP 2026-07-28 — URL-mode elicitation (InputRequiredResult) cannot be fulfilled | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:mcp, bug, has repro |
| [#88054](https://github.com/anthropics/claude-code/issues/88054) | \`claude remote-control\` server exits on 401 after exactly 24h — does not refresh its OAuth access token, killing every attached session | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, bug, has repro, platform:macos |
| [#88041](https://github.com/anthropics/claude-code/issues/88041) | \[Bug\] Auto-mode "bashFirst" system prompt instructs sed/heredoc file edits instead of Edit/Write tools | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-19 | area:core, area:tools, bug, platform:linux |
| [#88024](https://github.com/anthropics/claude-code/issues/88024) | \[BUG\] Claude Code fails to authenticate on MacOS in certain environments. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:security, bug, has repro, platform:macos |
| [#87950](https://github.com/anthropics/claude-code/issues/87950) | \[BUG\] Cowork forces a full account logout (auth\_kind=session\_stale\_relogin) roughly every 24-48h on Linux desktop | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-19 | area:auth, area:cowork, area:desktop, bug, has repro, platform:linux |
| [#87575](https://github.com/anthropics/claude-code/issues/87575) | \[Bug\] Auto mode system prompt causes /rewind to silently fail on Bash-edited files | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-18 | area:core, area:tools, bug, has repro, platform:wsl |
| [#87509](https://github.com/anthropics/claude-code/issues/87509) | \[BUG\] Windows Desktop: cross-session send\_message reports success and renders in the target UI, but is never enqueued/persisted (ghost delivery, lost on restart) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | area:agents, area:desktop, bug, platform:windows |
| [#87117](https://github.com/anthropics/claude-code/issues/87117) | Projects tool: project\_write silently destroys document content, with no append mode, no version history, and no recovery | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-16 | invalid |
| [#87110](https://github.com/anthropics/claude-code/issues/87110) | \[BUG\] send\_message\` (ccd\_session\_mgmt) renders in the recipient's UI but is never injected — regression between app 2.1.222 and 2.1.227 | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-16 | area:agents, area:desktop, bug, duplicate, platform:windows, regression |
| [#87107](https://github.com/anthropics/claude-code/issues/87107) | \[BUG\] Cowork (macOS): pending AskUserQuestion dialogue is lost when the user switches to another chat or artifact view, with no respawn path, and the agent is told the user rejected it | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-16 | area:cowork, area:desktop, area:tools, bug, has repro, platform:macos |
| [#87095](https://github.com/anthropics/claude-code/issues/87095) | \[BUG\] Agent view shows "esc to return" hint but Esc interrupts the agent instead | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-16 | area:agent-view, area:tui, bug, has repro, platform:macos |

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
