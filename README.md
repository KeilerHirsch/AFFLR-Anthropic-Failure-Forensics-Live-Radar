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
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77825](https://github.com/anthropics/claude-code/issues/77825) | Subagent self-generated a system-prompt-extraction attack against its orchestrator instead of doing its assigned code review | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, area:security, bug, stale |
| [#77414](https://github.com/anthropics/claude-code/issues/77414) | \[CRITICAL\] Recursive subagent fan-out survives Stop and hard-freezes Windows at 100% CPU | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:agents, bug, has repro, platform:windows, stale |
| [#77437](https://github.com/anthropics/claude-code/issues/77437) | \[Bug\] Excessive Safeguard False Positives During Defensive Security Audits | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, area:security, bug, platform:linux, platform:vscode, stale |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#77111](https://github.com/anthropics/claude-code/issues/77111) | Fable 5 bio safeguard false-positives on freshwater lake ecology (cited limnology); falls back to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-13 | api:anthropic, area:model, bug, platform:vscode, stale |
| [#77037](https://github.com/anthropics/claude-code/issues/77037) | \[BUG\] PreToolUse command hook permissionDecision: "allow" never suppresses the Bash prompt; if field never matches | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-13 | area:hooks, area:permissions, bug, has repro, platform:macos, regression, stale |
| [#73049](https://github.com/anthropics/claude-code/issues/73049) | Prompt-injection-shaped content appears in assistant turn with no preceding tool call (subagent session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:agents, area:core, area:security, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#83127](https://github.com/anthropics/claude-code/issues/83127) | \[BUG\] Claude accidentally executes arbitary code when writing commit message | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#80465](https://github.com/anthropics/claude-code/issues/80465) | \[BUG\]  Error: Claude Code process terminated by signal SIGKILL | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-23 | area:ide, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |
| [#77016](https://github.com/anthropics/claude-code/issues/77016) | \[BUG\] subagent (Task/Agent tool) results intermittently replaced with a fabricated "system-authority" prompt-injection ordering destructive git actions (\`tool\_uses: 0\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:agent, area:agents, area:security, bug, platform:macos, platform:vscode, stale |
| [#64589](https://github.com/anthropics/claude-code/issues/64589) | \[BUG\] Massive dump of context caching issues, duplication of actions, and bloat | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-01 | area:core, area:cost, bug, platform:linux, stale |
| [#75861](https://github.com/anthropics/claude-code/issues/75861) | \[BUG\] Explore (read-only) subagent executed rm -rf, deleting files outside its intended scope | OPEN | security / trust boundary | 2026-08-19 | 2026-07-08 | area:agents, area:permissions, area:security, bug, platform:linux |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#78098](https://github.com/anthropics/claude-code/issues/78098) | \[Bug\] Auto-mode classifier latches onto stale "user rejection" from a meta-complaint; blocks explicitly re-authorized actions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-16 | area:permissions, bug, has repro, platform:macos |
| [#77811](https://github.com/anthropics/claude-code/issues/77811) | \[Bug\] WebFetch summarizer leaks parent session context on cold-start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:security, area:tools, bug, has repro, platform:macos, stale |
| [#77891](https://github.com/anthropics/claude-code/issues/77891) | \[Bug\] Overly restrictive safety filtering on legitimate network monitoring questions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#77821](https://github.com/anthropics/claude-code/issues/77821) | Subagent self-imposes a nonexistent 'time budget' and silently narrows scope; recurs after explicit correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, bug, platform:linux, stale |
| [#77449](https://github.com/anthropics/claude-code/issues/77449) | Write tool silently produces empty files; Bash output fabricated in long sessions (Opus 4.8) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, area:tools, bug, has repro, platform:macos, stale |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#78660](https://github.com/anthropics/claude-code/issues/78660) | \[BUG\] task\_reminder nudge fired mid-tool-loop rewrites cached history (near-total rebuild per firing in autonomous sessions); 29% of sessions double-write the opening context — 3-week measured audit | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-17 | area:core, area:cost, bug, has repro, platform:macos |
| [#77825](https://github.com/anthropics/claude-code/issues/77825) | Subagent self-generated a system-prompt-extraction attack against its orchestrator instead of doing its assigned code review | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, area:security, bug, stale |
| [#77414](https://github.com/anthropics/claude-code/issues/77414) | \[CRITICAL\] Recursive subagent fan-out survives Stop and hard-freezes Windows at 100% CPU | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:agents, bug, has repro, platform:windows, stale |
| [#77437](https://github.com/anthropics/claude-code/issues/77437) | \[Bug\] Excessive Safeguard False Positives During Defensive Security Audits | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, area:security, bug, platform:linux, platform:vscode, stale |
| [#77433](https://github.com/anthropics/claude-code/issues/77433) | \[Bug\] Safety classifier false-positive on legitimate DevOps terminology in authorized sandbox context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, bug, duplicate, platform:macos, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#76905](https://github.com/anthropics/claude-code/issues/76905) | macOS Keychain: concurrent sessions race on OAuth refresh; setup-token workaround strips claude.ai connectors, leaving no viable headless pattern | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:auth, bug, has repro, platform:macos, stale |
| [#77111](https://github.com/anthropics/claude-code/issues/77111) | Fable 5 bio safeguard false-positives on freshwater lake ecology (cited limnology); falls back to Opus 4.8 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-13 | api:anthropic, area:model, bug, platform:vscode, stale |
| [#77037](https://github.com/anthropics/claude-code/issues/77037) | \[BUG\] PreToolUse command hook permissionDecision: "allow" never suppresses the Bash prompt; if field never matches | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-13 | area:hooks, area:permissions, bug, has repro, platform:macos, regression, stale |
| [#73049](https://github.com/anthropics/claude-code/issues/73049) | Prompt-injection-shaped content appears in assistant turn with no preceding tool call (subagent session) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-02 | area:agents, area:core, area:security, bug, has repro, platform:macos, stale |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#81273](https://github.com/anthropics/claude-code/issues/81273) | \[BUG\] Auto-mode catastrophic-removal guard bypassed: \`rm -rf\` inside a backtick substitution executes without a prompt | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-26 | area:permissions, bug |
| [#82930](https://github.com/anthropics/claude-code/issues/82930) | \[BUG\] Cowork scheduled task creation fails: "path moved between validation and open" — TOCTOU guard false-positives on FSLogix profile containers | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:desktop, bug |
| [#80465](https://github.com/anthropics/claude-code/issues/80465) | \[BUG\]  Error: Claude Code process terminated by signal SIGKILL | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-23 | area:ide, bug |
| [#77030](https://github.com/anthropics/claude-code/issues/77030) | Auto-mode classifier blocks a corrective rsync but misses the destructive one that caused the damage | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:bash, area:permissions, bug |
| [#77016](https://github.com/anthropics/claude-code/issues/77016) | \[BUG\] subagent (Task/Agent tool) results intermittently replaced with a fabricated "system-authority" prompt-injection ordering destructive git actions (\`tool\_uses: 0\`) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-13 | area:agent, area:agents, area:security, bug, platform:macos, platform:vscode, stale |
| [#64589](https://github.com/anthropics/claude-code/issues/64589) | \[BUG\] Massive dump of context caching issues, duplication of actions, and bloat | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-06-01 | area:core, area:cost, bug, platform:linux, stale |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#78098](https://github.com/anthropics/claude-code/issues/78098) | \[Bug\] Auto-mode classifier latches onto stale "user rejection" from a meta-complaint; blocks explicitly re-authorized actions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-16 | area:permissions, bug, has repro, platform:macos |
| [#77811](https://github.com/anthropics/claude-code/issues/77811) | \[Bug\] WebFetch summarizer leaks parent session context on cold-start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:security, area:tools, bug, has repro, platform:macos, stale |
| [#77891](https://github.com/anthropics/claude-code/issues/77891) | \[Bug\] Overly restrictive safety filtering on legitimate network monitoring questions | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:model, bug, platform:macos, stale |
| [#77821](https://github.com/anthropics/claude-code/issues/77821) | Subagent self-imposes a nonexistent 'time budget' and silently narrows scope; recurs after explicit correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-15 | area:agents, area:model, bug, platform:linux, stale |
| [#77449](https://github.com/anthropics/claude-code/issues/77449) | Write tool silently produces empty files; Bash output fabricated in long sessions (Opus 4.8) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-14 | area:model, area:tools, bug, has repro, platform:macos, stale |
| [#76974](https://github.com/anthropics/claude-code/issues/76974) | \[BUG\] Background Bash tasks (run\_in\_background=true) are sporadically SIGKILLed mid-run by the CLI's task supervision (~1% of dispatches; can corrupt git state) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-12 | area:core, area:tools, bug, has repro, platform:linux, stale |
| [#76764](https://github.com/anthropics/claude-code/issues/76764) | Opus (1M context, claude-opus-4-8) intermittently emits malformed tool-call opening sequence — degrades to a common English word, causing parse failure | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-07-11 | area:model, bug, duplicate, platform:windows, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88077](https://github.com/anthropics/claude-code/issues/88077) | Rewind: disabling fileCheckpointingEnabled also removes both Summarize options | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-19 | area:tui, bug, has repro, platform:linux |
| [#87971](https://github.com/anthropics/claude-code/issues/87971) | \[BUG\] Claude abuses bash tools for reads, writes, and edits when running in Auto Mode | OPEN | security / trust boundary · high-signal label | 2026-08-19 | 2026-08-19 | area:tools, bug, platform:vscode, platform:windows |
| [#87509](https://github.com/anthropics/claude-code/issues/87509) | \[BUG\] Windows Desktop: cross-session send\_message reports success and renders in the target UI, but is never enqueued/persisted (ghost delivery, lost on restart) | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-18 | area:agents, area:desktop, bug, platform:windows |
| [#87194](https://github.com/anthropics/claude-code/issues/87194) | \[BUG\] Claude Desktop 1.30096.5 hangs before creating a window on macOS | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-16 | invalid |
| [#87117](https://github.com/anthropics/claude-code/issues/87117) | Projects tool: project\_write silently destroys document content, with no append mode, no version history, and no recovery | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-16 | invalid |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87086](https://github.com/anthropics/claude-code/issues/87086) | \[EVAL/TRANSPARENCY\] Anthropic's regulation case rests on internal evals — apply the #86979 provenance standard to Glasswing and 'When AI Builds Itself' | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-16 | invalid |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86498](https://github.com/anthropics/claude-code/issues/86498) | MCP-originated cross-session sends (\`ccd\_session\_mgmt send\_message\`) never deliver — payload lost in app layer; receiving session UI hangs on "phantom" turn | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-13 | area:desktop, area:mcp, bug, duplicate, has repro, platform:windows, regression |
| [#86158](https://github.com/anthropics/claude-code/issues/86158) | \[Bug\] Anthropic API Error: Content Flagged by Sonnet 5 Safeguards | CLOSED / NOT\_PLANNED | observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-12 | area:model, bug, needs-repro, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-06 | — |
| [#84333](https://github.com/anthropics/claude-code/issues/84333) | \[BUG\] Claude Desktop (Windows MSIX) silently becomes Modified, NeedsRemediation mid-session with no deployment operation in the AppXDeploymentServer log | OPEN | security / trust boundary | 2026-08-19 | 2026-08-05 | bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83588](https://github.com/anthropics/claude-code/issues/83588) | \[BUG\] Claude Code persists Bash permission approvals to project .claude/settings.json instead of .claude/settings.local.json | CLOSED / DUPLICATE | security / trust boundary | 2026-08-19 | 2026-08-03 | bug |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#83171](https://github.com/anthropics/claude-code/issues/83171) | \[BUG\] Desktop app hangs when Bedrock model unavailable (403), cannot switch model | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83164](https://github.com/anthropics/claude-code/issues/83164) | \[BUG\] Previous sessions not showing in Desktop sidebar in Gateway mode (Windows) — data intact on disk, UI/indexing issue | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83162](https://github.com/anthropics/claude-code/issues/83162) | Title: Background task reported exit 0 on OOM failure, Claude proceeded to push stale image to production ECR causing $250 of additional credit cost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-19 | 2026-08-01 | area:tools, bug |
| [#83159](https://github.com/anthropics/claude-code/issues/83159) | \[BUG\] Read-aloud ignores the selected voice — always plays the same voice regardless of the setting (desktop &amp; web, Windows + Linux) | OPEN | observation / provenance integrity | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83127](https://github.com/anthropics/claude-code/issues/83127) | \[BUG\] Claude accidentally executes arbitary code when writing commit message | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:permissions, bug |
| [#83094](https://github.com/anthropics/claude-code/issues/83094) | \[BUG\] Claude Desktop Linux beta: session silently loses the entire earlier conversation mid-prompt | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83087](https://github.com/anthropics/claude-code/issues/83087) | \[BUG\] Response stream stalls after first byte with no timeout/recovery — indefinite livelock in Auto mode | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-01 | area:ide, bug |
| [#83083](https://github.com/anthropics/claude-code/issues/83083) | \[BUG\] Frequent "API Error: Unable to connect to API (ECONNRESET)" mid-session on Windows — network verified healthy, Tailscale ruled out | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-01 | bug |
| [#83052](https://github.com/anthropics/claude-code/issues/83052) | \[BUG\] .sql syntax highlighting never renders in Desktop file previewer (Windows) | OPEN | security / trust boundary | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83028](https://github.com/anthropics/claude-code/issues/83028) | Claude Desktop MSIX crash on Intel integrated GPU during browser pane use — reproducible, no workaround available | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-08-01 | area:desktop, bug |
| [#83024](https://github.com/anthropics/claude-code/issues/83024) | Background agents and tasks killed unexpectedly | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-19 | 2026-07-31 | area:agents, bug |

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
