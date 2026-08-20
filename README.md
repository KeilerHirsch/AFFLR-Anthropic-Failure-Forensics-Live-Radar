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
| [#88113](https://github.com/anthropics/claude-code/issues/88113) | settings.json writes silently strip unknown keys from hook groups and hook items | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:macos |
| [#84981](https://github.com/anthropics/claude-code/issues/84981) | Background tasks SIGTERMed on an exact 30-minute internal timer (macOS CLI, long-lived session) — undocumented kill path, exit 144 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-08 | area:tools |
| [#87042](https://github.com/anthropics/claude-code/issues/87042) | \[MODEL\] | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:security, area:tools, bug, model |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83058](https://github.com/anthropics/claude-code/issues/83058) | \[BUG\] Recursive rm deleted ~200 GB of home directory — no approval prompt for a delete outside the project cwd | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | area:permissions |
| [#83707](https://github.com/anthropics/claude-code/issues/83707) | MCP OAuth never completes: 11 cached registrations all have an empty accessToken, including clients where DCR succeeded | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-04 | area:mcp |
| [#83556](https://github.com/anthropics/claude-code/issues/83556) | \`/code-review\` can silently destroy uncommitted work — a premature "completed" status opens the write race, and the harness's own safeguard is told to hide it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:agents |
| [#83589](https://github.com/anthropics/claude-code/issues/83589) | Agent loop: a parallel subagent result that lands after the final turn is never consumed — and the 2.1.218 nudge does not cover it (only fires on empty turns) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:core |
| [#83459](https://github.com/anthropics/claude-code/issues/83459) | Auto-mode permission classifier reads the command string, so a sensitive action moved into a script file isn't gated | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:permissions |
| [#84268](https://github.com/anthropics/claude-code/issues/84268) | Cowork 'record a demonstration': mic control shown but narration silently dropped — WatchRecordVoiceover 'no api credentials configured' (coworkWatchRecord gate off while watchRecordEnabled on) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:desktop |
| [#80603](https://github.com/anthropics/claude-code/issues/80603) | \[BUG\] 2.1.218 (native build): OAuth MCP servers report "requires authentication" in --print/headless sessions despite valid keychain tokens (regression from 2.1.210) | CLOSED / DUPLICATE | security / trust boundary | 2026-08-20 | 2026-07-23 | needs-repro |
| [#84273](https://github.com/anthropics/claude-code/issues/84273) | \[BUG\] Background/Workflow subagents all 401 at OAuth token rollover while the parent session refreshes successfully (spawn-time token capture) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:agents |
| [#84274](https://github.com/anthropics/claude-code/issues/84274) | MCP OAuth: access token never persisted — server silently reverts to unauthenticated after restart | OPEN | security / trust boundary | 2026-08-20 | 2026-08-05 | area:mcp |
| [#84275](https://github.com/anthropics/claude-code/issues/84275) | Keychain: Claude Code-credentials-\* items created daily and never cleaned up (75 items, 1156 duplicated OAuth tokens) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-05 | area:core |
| [#84299](https://github.com/anthropics/claude-code/issues/84299) | \[BUG\] claude mcp list reports "✔ Connected" for unauthorized stateless claude.ai connectors | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:mcp |
| [#83848](https://github.com/anthropics/claude-code/issues/83848) | Background subagents intermittently stall with no final text, harness still reports status:completed (fresh subagent types only, not fork) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-04 | area:agents |
| [#83611](https://github.com/anthropics/claude-code/issues/83611) | A tool listed in permissions.allow is denied by the permission classifier | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:mcp, area:permissions |
| [#83635](https://github.com/anthropics/claude-code/issues/83635) | Daemon bg job wedged in 'blocked' after safety-classifier API error, then silently resumes 4 days later and runs tools on stale context | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:core |
| [#84125](https://github.com/anthropics/claude-code/issues/84125) | \[BUG\] LSP tool is pruned from all subagent tool sets in interactive sessions (present in the parent, and in subagents under -p) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:agents |
| [#85411](https://github.com/anthropics/claude-code/issues/85411) | Auto mode: safety classifier blocks read-only MCP tools when the conversation model is unavailable | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-10 | area:mcp, area:permissions |
| [#85274](https://github.com/anthropics/claude-code/issues/85274) | PreToolUse Bash guard &amp; permission prompt are string-level: model-authored destructive commands inside a script bypass the approval gate | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-09 | area:hooks, area:permissions |
| [#85294](https://github.com/anthropics/claude-code/issues/85294) | \[BUG\] Desktop account switch does not isolate local state: app storage is not account-keyed and ~/.claude.json is never reconciled | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-09 | area:desktop |
| [#87369](https://github.com/anthropics/claude-code/issues/87369) | \[MODEL\] Background fork's AskUserQuestion silently resolves to its own "Recommended" answer with no human involved, then acts on that as authorization to overwrite files outside its scope | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-17 | area:agents |
| [#85603](https://github.com/anthropics/claude-code/issues/85603) | Typed input queued mid-turn is silently dropped at turn end (end\_turn, no Escape involved) -- interactive TUI | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-10 | area:tui |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88113](https://github.com/anthropics/claude-code/issues/88113) | settings.json writes silently strip unknown keys from hook groups and hook items | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:macos |
| [#84981](https://github.com/anthropics/claude-code/issues/84981) | Background tasks SIGTERMed on an exact 30-minute internal timer (macOS CLI, long-lived session) — undocumented kill path, exit 144 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-08 | area:tools |
| [#87042](https://github.com/anthropics/claude-code/issues/87042) | \[MODEL\] | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:security, area:tools, bug, model |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#83058](https://github.com/anthropics/claude-code/issues/83058) | \[BUG\] Recursive rm deleted ~200 GB of home directory — no approval prompt for a delete outside the project cwd | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-01 | area:permissions |
| [#83707](https://github.com/anthropics/claude-code/issues/83707) | MCP OAuth never completes: 11 cached registrations all have an empty accessToken, including clients where DCR succeeded | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-04 | area:mcp |
| [#83556](https://github.com/anthropics/claude-code/issues/83556) | \`/code-review\` can silently destroy uncommitted work — a premature "completed" status opens the write race, and the harness's own safeguard is told to hide it | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:agents |
| [#83589](https://github.com/anthropics/claude-code/issues/83589) | Agent loop: a parallel subagent result that lands after the final turn is never consumed — and the 2.1.218 nudge does not cover it (only fires on empty turns) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:core |
| [#83459](https://github.com/anthropics/claude-code/issues/83459) | Auto-mode permission classifier reads the command string, so a sensitive action moved into a script file isn't gated | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:permissions |
| [#84268](https://github.com/anthropics/claude-code/issues/84268) | Cowork 'record a demonstration': mic control shown but narration silently dropped — WatchRecordVoiceover 'no api credentials configured' (coworkWatchRecord gate off while watchRecordEnabled on) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:desktop |
| [#84273](https://github.com/anthropics/claude-code/issues/84273) | \[BUG\] Background/Workflow subagents all 401 at OAuth token rollover while the parent session refreshes successfully (spawn-time token capture) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:agents |
| [#84299](https://github.com/anthropics/claude-code/issues/84299) | \[BUG\] claude mcp list reports "✔ Connected" for unauthorized stateless claude.ai connectors | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:mcp |
| [#83848](https://github.com/anthropics/claude-code/issues/83848) | Background subagents intermittently stall with no final text, harness still reports status:completed (fresh subagent types only, not fork) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-04 | area:agents |
| [#83611](https://github.com/anthropics/claude-code/issues/83611) | A tool listed in permissions.allow is denied by the permission classifier | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:mcp, area:permissions |
| [#83635](https://github.com/anthropics/claude-code/issues/83635) | Daemon bg job wedged in 'blocked' after safety-classifier API error, then silently resumes 4 days later and runs tools on stale context | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-03 | area:core |
| [#84125](https://github.com/anthropics/claude-code/issues/84125) | \[BUG\] LSP tool is pruned from all subagent tool sets in interactive sessions (present in the parent, and in subagents under -p) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-05 | area:agents |
| [#85411](https://github.com/anthropics/claude-code/issues/85411) | Auto mode: safety classifier blocks read-only MCP tools when the conversation model is unavailable | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-10 | area:mcp, area:permissions |
| [#85274](https://github.com/anthropics/claude-code/issues/85274) | PreToolUse Bash guard &amp; permission prompt are string-level: model-authored destructive commands inside a script bypass the approval gate | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-09 | area:hooks, area:permissions |
| [#85294](https://github.com/anthropics/claude-code/issues/85294) | \[BUG\] Desktop account switch does not isolate local state: app storage is not account-keyed and ~/.claude.json is never reconciled | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-09 | area:desktop |
| [#87369](https://github.com/anthropics/claude-code/issues/87369) | \[MODEL\] Background fork's AskUserQuestion silently resolves to its own "Recommended" answer with no human involved, then acts on that as authorization to overwrite files outside its scope | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-17 | area:agents |
| [#85603](https://github.com/anthropics/claude-code/issues/85603) | Typed input queued mid-turn is silently dropped at turn end (end\_turn, no Escape involved) -- interactive TUI | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-10 | area:tui |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |
| [#83820](https://github.com/anthropics/claude-code/issues/83820) | Bash tool rm permanently deletes files (bypasses Recycle Bin), no built-in safeguard against agent-initiated data loss | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-04 | area:tools |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88116](https://github.com/anthropics/claude-code/issues/88116) | \[BUG\] Background workers (bg-spare) never release memory after jobs complete — monotonic RSS growth saturates 24GB RAM in ~7 days on always-on machines | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, bug, has repro, perf:memory, platform:macos |
| [#88115](https://github.com/anthropics/claude-code/issues/88115) | \[Security\] Assistant-generated text injected into USER message turn after advisor tool call | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, area:security, area:tools, bug, platform:macos |
| [#88114](https://github.com/anthropics/claude-code/issues/88114) | VSCode extension: diff preview fails (String not found in file) for multi-line edits on CRLF files | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:ide, duplicate, has repro, platform:vscode, platform:windows |
| [#88113](https://github.com/anthropics/claude-code/issues/88113) | settings.json writes silently strip unknown keys from hook groups and hook items | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, bug, has repro, platform:macos |
| [#88105](https://github.com/anthropics/claude-code/issues/88105) | \[BUG\] Auto-update to 2.1.237 leaves broken stub on Windows: claude-code-win32-x64@2.1.237 missing from npm registry (incomplete release) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:installation, area:packaging, bug, has repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88103](https://github.com/anthropics/claude-code/issues/88103) | \[BUG\] 2.1.237 tagged \`latest\` with its linux-x64, win32-x64 and linux-x64-musl native packages never published - installs land on a dead 500-byte stub | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:packaging, bug, has repro, high-priority, platform:linux, platform:windows |
| [#88102](https://github.com/anthropics/claude-code/issues/88102) | \[BUG\] Channels (research preview): async MCP tool calls hang when the same streamable-HTTP server is bound as a channel source | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro |
| [#88096](https://github.com/anthropics/claude-code/issues/88096) | MODEL444564531230..0 | CLOSED / NOT\_PLANNED | security / trust boundary | 2026-08-20 | 2026-08-20 | model |
| [#87893](https://github.com/anthropics/claude-code/issues/87893) | \[Bug\] Session state inconsistency after /rewind and /resume with file state mismatch | OPEN | security / trust boundary | 2026-08-20 | 2026-08-19 | area:core |
| [#87884](https://github.com/anthropics/claude-code/issues/87884) | Auto-compact should continue the same session instead of starting a new one | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:core |
| [#87881](https://github.com/anthropics/claude-code/issues/87881) | \[FEATURE\] Auto mode classifier should evaluate declared intent, not just the action | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-19 | area:permissions |
| [#87617](https://github.com/anthropics/claude-code/issues/87617) | \[BUG\] Cowork VM connection timeout after 60 seconds — Intel Mac, guest kernel stalls ~2.2s into boot | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-18 | area:cowork, area:desktop, duplicate, platform:macos |
| [#87495](https://github.com/anthropics/claude-code/issues/87495) | Orphaned interactive session with no visible window keeps receiving cross-session messages as held-for-approval | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-18 | area:agents |
| [#87398](https://github.com/anthropics/claude-code/issues/87398) | \[BUG\] Unloadable legacy sessions silently defeat the desktop environment default (falls back to Local) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-17 | area:desktop |
| [#87369](https://github.com/anthropics/claude-code/issues/87369) | \[MODEL\] Background fork's AskUserQuestion silently resolves to its own "Recommended" answer with no human involved, then acts on that as authorization to overwrite files outside its scope | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-17 | area:agents |
| [#87321](https://github.com/anthropics/claude-code/issues/87321) | Telegram channel plugin: forum Topics support (message\_thread\_id in channel meta + reply tool) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-17 | area:plugins, enhancement |
| [#87095](https://github.com/anthropics/claude-code/issues/87095) | \[BUG\] Agent view shows "esc to return" hint but Esc interrupts the agent instead | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-16 | area:agent-view, area:tui, bug, has repro, platform:macos |
| [#87086](https://github.com/anthropics/claude-code/issues/87086) | \[EVAL/TRANSPARENCY\] Anthropic's regulation case rests on internal evals — apply the #86979 provenance standard to Glasswing and 'When AI Builds Itself' | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-16 | invalid |
| [#87042](https://github.com/anthropics/claude-code/issues/87042) | \[MODEL\] | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-16 | area:security, area:tools, bug, model |
| [#86998](https://github.com/anthropics/claude-code/issues/86998) | \[BUG\] ReportFindings tool description overrides a caller-defined subagent output contract; parent gets \[\] | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-15 | area:agents, area:tools, bug, platform:macos |
| [#86979](https://github.com/anthropics/claude-code/issues/86979) | \[EVAL/TRANSPARENCY\] Published coding scores conflate task solving with known-fix retrieval — disclose leakage rate and strict-harness result | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-15 | invalid |
| [#86752](https://github.com/anthropics/claude-code/issues/86752) | \[BUG\] "Can't rewind to this message" for every target older than the newest mid-turn queued message — \`queued\_command\` uuid rewrite breaks the Desktop active-chain walk | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-14 | area:desktop, bug, has repro, platform:macos |
| [#86730](https://github.com/anthropics/claude-code/issues/86730) | \[BUG\] Default cleanupPeriodDays silently deleted 58 of 69 session transcripts; sidebar shows ghost entries with "Session not found on disk" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:core, area:desktop, bug, data-loss, platform:macos |
| [#86720](https://github.com/anthropics/claude-code/issues/86720) | Message delivered to an idle session cold-starts a "ghost turn" (no assistant output), and the queued message is silently lost on app restart — no transcript record remains | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:agents, area:desktop, bug, data-loss, platform:windows |
| [#86643](https://github.com/anthropics/claude-code/issues/86643) | \[BUG\] Runaway memory growth in Claude Code child process causes full system freeze (Ubuntu 24.04, requires hard reboot) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-14 | area:core, duplicate, perf:memory, platform:linux |

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
