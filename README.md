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
> Automated discovery metadata from public `anthropics/claude-code` issues. Popularity is a discovery signal, not evidence.

### 🔥 Most reacted

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5913 (👍 4566 · 👎 10 · 😄 33 · 🎉 296 · 😕 5 · ❤️ 400 · 🚀 333 · 👀 270) | 349 | 2026-08-14 | 2025-08-21 | area:core, enhancement, memory |
| [#42796](https://github.com/anthropics/claude-code/issues/42796) | \[MODEL\] Claude Code is unusable for complex engineering tasks with the Feb updates | stellaraccident | CLOSED / COMPLETED | 3286 (👍 2072 · 👎 8 · 😄 149 · 🎉 114 · 😕 59 · ❤️ 436 · 🚀 231 · 👀 217) | 583 | 2026-04-24 | 2026-04-02 | area:model, bug, model |
| [#45596](https://github.com/anthropics/claude-code/issues/45596) | Bring Back Buddy — A Consolidated Plea from the Community | Hujoepandiselvan | OPEN | 2069 (👍 1168 · 👎 5 · 😄 36 · 🎉 1 · ❤️ 639 · 🚀 68 · 👀 152) | 266 | 2026-08-12 | 2026-04-09 | area:skills, area:tui, duplicate, enhancement |
| [#17118](https://github.com/anthropics/claude-code/issues/17118) | \[Feature Request\] Support for OpenCode and Max plan | shawnyeager | CLOSED / COMPLETED | 1416 (👍 797 · 👎 8 · 😄 12 · 😕 4 · ❤️ 514 · 🚀 81) | 410 | 2026-02-09 | 2026-01-09 | area:auth, bug, has repro, oncall, platform:linux |
| [#3382](https://github.com/anthropics/claude-code/issues/3382) | \[BUG\] Claude says "You're absolutely right!" about everything | scottleibrand | CLOSED / COMPLETED | 1375 (👍 873 · 😄 337 · ❤️ 126 · 👀 39) | 179 | 2025-09-20 | 2025-07-12 | area:core, area:model, bug, duplicate |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#34229](https://github.com/anthropics/claude-code/issues/34229) | \[BUG\] Phone verification | jpiabrantes | OPEN | 892 (👍 821 · 🎉 15 · ❤️ 21 · 🚀 19 · 👀 16) | 742 | 2026-07-19 | 2026-03-14 | invalid |
| [#3648](https://github.com/anthropics/claude-code/issues/3648) | Terminal Scrolling Uncontrollably During Claude Code Interaction | JacobGoldenArt | CLOSED / COMPLETED | 837 (👍 694 · 👎 3 · 😄 2 · 🎉 4 · 😕 45 · ❤️ 31 · 🚀 16 · 👀 42) | 337 | 2026-02-06 | 2025-07-16 | area:auth, area:ide, area:tui, bug, oncall, platform:macos |
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 824 (👍 727 · ❤️ 48 · 🚀 35 · 👀 14) | 166 | 2026-08-14 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#826](https://github.com/anthropics/claude-code/issues/826) | \[BUG\] Console scrolling top of history when claude add text to the console | ocontant | OPEN / REOPENED | 823 (👍 691 · 😄 15 · 🎉 2 · 😕 15 · ❤️ 7 · 🚀 15 · 👀 78) | 354 | 2026-07-29 | 2025-04-19 | bug, duplicate, oncall, platform:macos |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 805 (👍 592 · ❤️ 172 · 🚀 41) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#65697](https://github.com/anthropics/claude-code/issues/65697) | \[FEATURE\] Official Claude Desktop build for Linux (Ubuntu LTS / Debian) | powell-clark | CLOSED / COMPLETED | 655 (👍 498 · 👎 4 · 🎉 28 · ❤️ 65 · 🚀 35 · 👀 25) | 53 | 2026-08-13 | 2026-06-05 | area:desktop, enhancement, platform:linux |
| [#17432](https://github.com/anthropics/claude-code/issues/17432) | Feature Request: India-Specific Pricing Plans (INR) for Claude &amp; Claude Code | saidev-pbi-fabric | OPEN | 622 (👍 486 · ❤️ 40 · 🚀 81 · 👀 15) | 212 | 2026-08-07 | 2026-01-11 | area:cost, enhancement, external |
| [#2511](https://github.com/anthropics/claude-code/issues/2511) | Feature request: Connect Claude code to Claude projects  | salimmallick | OPEN | 596 (👍 385 · ❤️ 116 · 🚀 59 · 👀 36) | 49 | 2026-07-29 | 2025-06-24 | area:core, enhancement |
| [#6686](https://github.com/anthropics/claude-code/issues/6686) | Feature Request: Add support for Agent Client Protocol (ACP) | coygeek | CLOSED / NOT\_PLANNED | 551 (👍 437 · ❤️ 114) | 37 | 2026-02-19 | 2025-08-27 | area:ide, enhancement, external |
| [#38335](https://github.com/anthropics/claude-code/issues/38335) | \[BUG\] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) | karenrebecag | OPEN | 543 (👍 474 · 😕 42 · 👀 27) | 835 | 2026-08-14 | 2026-03-24 | invalid |
| [#53262](https://github.com/anthropics/claude-code/issues/53262) | HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota | sasha-id | CLOSED / COMPLETED | 532 (👍 213 · 👎 3 · 😄 66 · 😕 230 · 🚀 6 · 👀 14) | 93 | 2026-07-11 | 2026-04-25 | area:cost, bug, has repro, platform:macos |
| [#15942](https://github.com/anthropics/claude-code/issues/15942) | Add support for Visual Studio 2026 Integration | ovftank | OPEN | 518 (👍 416 · 🎉 25 · ❤️ 27 · 🚀 29 · 👀 21) | 149 | 2026-08-11 | 2026-01-01 | area:ide, enhancement, platform:windows |
| [#27302](https://github.com/anthropics/claude-code/issues/27302) | \[FEATURE\] Support multiple Connector accounts (same connector, different accounts) in Claude and Claude Code on the web (claude.ai/code) | nathanmargaglio | OPEN | 485 (👍 346 · ❤️ 110 · 🚀 16 · 👀 13) | 227 | 2026-08-12 | 2026-02-21 | enhancement |
| [#1455](https://github.com/anthropics/claude-code/issues/1455) | Claude Code does not respect the XDG Base Directory specification | jennifgcrl | OPEN | 435 (👍 418 · 👎 1 · 😄 3 · 🎉 4 · ❤️ 6 · 👀 3) | 65 | 2026-08-12 | 2025-05-31 | bug, enhancement, platform:linux |
| [#73125](https://github.com/anthropics/claude-code/issues/73125) | \[BUG\] AskUserQuestion: "No response after 60s — continued without an answer" | ANogin | CLOSED / COMPLETED | 414 (👍 388 · 😄 1 · 😕 16 · 🚀 9) | 143 | 2026-07-09 | 2026-07-02 | api:bedrock, area:tools, area:tui, bug, platform:linux, platform:vscode |
| [#31005](https://github.com/anthropics/claude-code/issues/31005) | Support for AGENTS.md and .agents/skills/, the community has been asking since August 2025 | kvnwolf | OPEN | 413 (👍 310 · 🎉 2 · ❤️ 70 · 👀 31) | 19 | 2026-08-10 | 2026-03-05 | area:core, duplicate, enhancement, memory |
| [#6915](https://github.com/anthropics/claude-code/issues/6915) | Allow MCP tools to be available only to subagent | eli0shin | CLOSED / COMPLETED | 378 (👍 271 · ❤️ 57 · 🚀 40 · 👀 10) | 89 | 2026-03-23 | 2025-08-31 | area:mcp, duplicate, enhancement |
| [#8477](https://github.com/anthropics/claude-code/issues/8477) | \[FEATURE\] Add Option to Always Show Claude's Thinking | janbam | OPEN | 356 (👍 329 · 👎 1 · 👀 26) | 92 | 2026-07-26 | 2025-09-30 | area:tui, enhancement |
| [#46829](https://github.com/anthropics/claude-code/issues/46829) | Cache TTL silently regressed from 1h to 5m around early March 2026, causing quota and cost inflation | seanGSISG | CLOSED / NOT\_PLANNED | 342 (👍 245 · 😕 24 · ❤️ 24 · 👀 49) | 56 | 2026-06-28 | 2026-04-12 | api:anthropic, area:cost, bug, has repro |

</details>

### 💬 Most discussed

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#38335](https://github.com/anthropics/claude-code/issues/38335) | \[BUG\] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) | karenrebecag | OPEN | 543 (👍 474 · 😕 42 · 👀 27) | 835 | 2026-08-14 | 2026-03-24 | invalid |
| [#34229](https://github.com/anthropics/claude-code/issues/34229) | \[BUG\] Phone verification | jpiabrantes | OPEN | 892 (👍 821 · 🎉 15 · ❤️ 21 · 🚀 19 · 👀 16) | 742 | 2026-07-19 | 2026-03-14 | invalid |
| [#42796](https://github.com/anthropics/claude-code/issues/42796) | \[MODEL\] Claude Code is unusable for complex engineering tasks with the Feb updates | stellaraccident | CLOSED / COMPLETED | 3286 (👍 2072 · 👎 8 · 😄 149 · 🎉 114 · 😕 59 · ❤️ 436 · 🚀 231 · 👀 217) | 583 | 2026-04-24 | 2026-04-02 | area:model, bug, model |
| [#17118](https://github.com/anthropics/claude-code/issues/17118) | \[Feature Request\] Support for OpenCode and Max plan | shawnyeager | CLOSED / COMPLETED | 1416 (👍 797 · 👎 8 · 😄 12 · 😕 4 · ❤️ 514 · 🚀 81) | 410 | 2026-02-09 | 2026-01-09 | area:auth, bug, has repro, oncall, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#826](https://github.com/anthropics/claude-code/issues/826) | \[BUG\] Console scrolling top of history when claude add text to the console | ocontant | OPEN / REOPENED | 823 (👍 691 · 😄 15 · 🎉 2 · 😕 15 · ❤️ 7 · 🚀 15 · 👀 78) | 354 | 2026-07-29 | 2025-04-19 | bug, duplicate, oncall, platform:macos |
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5913 (👍 4566 · 👎 10 · 😄 33 · 🎉 296 · 😕 5 · ❤️ 400 · 🚀 333 · 👀 270) | 349 | 2026-08-14 | 2025-08-21 | area:core, enhancement, memory |
| [#3648](https://github.com/anthropics/claude-code/issues/3648) | Terminal Scrolling Uncontrollably During Claude Code Interaction | JacobGoldenArt | CLOSED / COMPLETED | 837 (👍 694 · 👎 3 · 😄 2 · 🎉 4 · 😕 45 · ❤️ 31 · 🚀 16 · 👀 42) | 337 | 2026-02-06 | 2025-07-16 | area:auth, area:ide, area:tui, bug, oncall, platform:macos |
| [#769](https://github.com/anthropics/claude-code/issues/769) | \[BUG\]  In-progress Call causes Screen Flickering | Cheffromspace | OPEN / REOPENED | 335 (👍 300 · 😄 3 · 😕 13 · 👀 19) | 307 | 2026-07-16 | 2025-04-12 | area:tools, area:tui, bug, oncall |
| [#3572](https://github.com/anthropics/claude-code/issues/3572) | Anthropic API Overloaded Error with Repeated 529 Status Codes | wepajoli | CLOSED / COMPLETED | 142 (👍 124 · 😕 10 · 👀 8) | 274 | 2025-08-02 | 2025-07-15 | area:api, area:auth, area:packaging, bug, has repro, platform:macos |
| [#8763](https://github.com/anthropics/claude-code/issues/8763) | API Error: 400 due to tool use concurrency issues. Run /rewind to recover the conversation. - \[Bug\] Anthropic API Error: Unexpected 400 Bad Request Response | ariccio | CLOSED / COMPLETED | 277 (👍 238 · 😕 36 · 👀 3) | 270 | 2025-11-27 | 2025-10-02 | area:api, area:core, area:tools, bug, has repro, oncall, platform:macos |
| [#45596](https://github.com/anthropics/claude-code/issues/45596) | Bring Back Buddy — A Consolidated Plea from the Community | Hujoepandiselvan | OPEN | 2069 (👍 1168 · 👎 5 · 😄 36 · 🎉 1 · ❤️ 639 · 🚀 68 · 👀 152) | 266 | 2026-08-12 | 2026-04-09 | area:skills, area:tui, duplicate, enhancement |
| [#27302](https://github.com/anthropics/claude-code/issues/27302) | \[FEATURE\] Support multiple Connector accounts (same connector, different accounts) in Claude and Claude Code on the web (claude.ai/code) | nathanmargaglio | OPEN | 485 (👍 346 · ❤️ 110 · 🚀 16 · 👀 13) | 227 | 2026-08-12 | 2026-02-21 | enhancement |
| [#17432](https://github.com/anthropics/claude-code/issues/17432) | Feature Request: India-Specific Pricing Plans (INR) for Claude &amp; Claude Code | saidev-pbi-fabric | OPEN | 622 (👍 486 · ❤️ 40 · 🚀 81 · 👀 15) | 212 | 2026-08-07 | 2026-01-11 | area:cost, enhancement, external |
| [#1913](https://github.com/anthropics/claude-code/issues/1913) | Terminal Flickering | PierrunoYT | OPEN | 321 (👍 321) | 187 | 2026-07-09 | 2025-06-10 | area:tui, bug, duplicate, oncall |
| [#4928](https://github.com/anthropics/claude-code/issues/4928) | \[BUG\] file named nul created on windows | rweijnen | CLOSED / COMPLETED | 235 (👍 235) | 184 | 2026-03-23 | 2025-08-01 | area:tools, bug, has repro, oncall, platform:windows |
| [#46987](https://github.com/anthropics/claude-code/issues/46987) | \[BUG\]  API Error: Stream idle timeout - partial response received - multiple time today | ac-monty | OPEN | 197 (👍 168 · 😕 20 · 👀 9) | 184 | 2026-07-09 | 2026-04-12 | api:anthropic, duplicate, platform:macos |
| [#5088](https://github.com/anthropics/claude-code/issues/5088) | Claude Account Disabled After Payment for Claude Code Max 5x Plan | thinhbuzz | OPEN | 66 (👍 60 · 👀 6) | 181 | 2026-07-20 | 2025-08-04 | area:auth, area:cost, bug, oncall |
| [#3382](https://github.com/anthropics/claude-code/issues/3382) | \[BUG\] Claude says "You're absolutely right!" about everything | scottleibrand | CLOSED / COMPLETED | 1375 (👍 873 · 😄 337 · ❤️ 126 · 👀 39) | 179 | 2025-09-20 | 2025-07-12 | area:core, area:model, bug, duplicate |
| [#18866](https://github.com/anthropics/claude-code/issues/18866) | \[BUG\] Auto-compact not triggering on Claude.ai (web &amp; desktop) despite being marked as fixed | solangerainha | CLOSED / COMPLETED | 65 (👍 65) | 176 | 2026-02-28 | 2026-01-17 | bug, invalid |
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 824 (👍 727 · ❤️ 48 · 🚀 35 · 👀 14) | 166 | 2026-08-14 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#24964](https://github.com/anthropics/claude-code/issues/24964) | \[BUG\] Cowork: Folder picker rejects folders outside home directory, symlinks/junctions also blocked | aviy009 | CLOSED / COMPLETED | 190 (👍 189 · 😕 1) | 157 | 2026-04-19 | 2026-02-11 | area:ide, bug, has repro, oncall, platform:macos, platform:windows |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 805 (👍 592 · ❤️ 172 · 🚀 41) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#29579](https://github.com/anthropics/claude-code/issues/29579) | \[BUG\] API Error: Rate limit reached despite Claude Max subscription and only 16% usage | CaptainDaredevil | OPEN | 94 (👍 94) | 153 | 2026-07-27 | 2026-02-28 | area:api, area:auth, bug, has repro, platform:vscode, platform:windows |
| [#33238](https://github.com/anthropics/claude-code/issues/33238) | Claude Code OAuth login fails with a timeout error. \`auth.anthropic.com\` does not resolve via DNS, making it impossible to authenticate. | lokasquad1 | OPEN | 47 (👍 45 · 👀 2) | 153 | 2026-07-20 | 2026-03-11 | area:auth, bug, platform:windows |

</details>

### 🆕 Recently active

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#84780](https://github.com/anthropics/claude-code/issues/84780) | \[BUG\] Thinking block summaries truncated mid-sentence (showThinkingSummaries: true) | fishshadow26 | OPEN | 5 (👍 5) | 8 | 2026-08-15 | 2026-08-07 | — |
| [#85923](https://github.com/anthropics/claude-code/issues/85923) | \[Feature Request\] Add "continue" option when usage limits are reached to resume after reset | nik2208 | OPEN | 0 | 1 | 2026-08-15 | 2026-08-11 | area:tui, enhancement, platform:macos |
| [#86887](https://github.com/anthropics/claude-code/issues/86887) | XProtect behavioral false positive kills ordinary Ghostty CLI sessions on macOS 26.5.1 | bolfeteml | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:bash, area:security, bug, platform:macos |
| [#86886](https://github.com/anthropics/claude-code/issues/86886) | There's an issue with the selected model (invalid-model). It may not exist or you may not have access to it. Run /model to pick a different model. | shridlock | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:model, bug, needs-info, platform:linux |
| [#77684](https://github.com/anthropics/claude-code/issues/77684) | SendMessage to a completed agent resumes it and re-executes side-effectful plans without fresh approval | arockwell | OPEN | 0 | 2 | 2026-08-15 | 2026-07-15 | area:agents, bug |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#54393](https://github.com/anthropics/claude-code/issues/54393) | Post-mortem 2026-04-28: 12 multi-agent coordination bugs surfaced across a single autonomous-overnight cycle | ThatDragonOverThere | OPEN | 0 | 29 | 2026-08-15 | 2026-04-28 | area:agents, area:hooks, area:permissions, enhancement |
| [#86885](https://github.com/anthropics/claude-code/issues/86885) | Gmail MCP connector: search\_threads resultCountEstimate wildly wrong for in:inbox | TheAviv | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:mcp, bug |
| [#86884](https://github.com/anthropics/claude-code/issues/86884) | \[BUG\] Archived Sessions group silently truncates on scroll — no load-more, no count | dochunt01 | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:desktop, area:ui, bug, has repro, platform:macos |
| [#86883](https://github.com/anthropics/claude-code/issues/86883) | \[BUG\] Open Code session in no sidebar group, including Ungrouped | dochunt01 | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:desktop, area:ui, bug, platform:macos |
| [#86882](https://github.com/anthropics/claude-code/issues/86882) | \[BUG\] Recurring SIGSEGV on \`HTTP Client\` thread during SSE streaming — tagged JSValue dereferenced as pointer (Bun 1.4.0, macOS arm64, 2.1.220) | ddomeke | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:packaging, bug, has repro, platform:macos, platform:vscode |
| [#68574](https://github.com/anthropics/claude-code/issues/68574) | \[BUG\] "Weekly limit approaching" warning shown despite only 26% weekly usage | RRY | CLOSED / COMPLETED | 0 | 3 | 2026-08-15 | 2026-06-15 | area:cost, area:tui, bug, has repro, platform:macos |
| [#86385](https://github.com/anthropics/claude-code/issues/86385) | Cross-session send\_message delivers to the target session's queue but never triggers a responding turn (regression in desktop 1.28929.0 / CC runtime 2.1.227, still broken in 2.1.231) | RNPS | OPEN | 1 (👍 1) | 4 | 2026-08-15 | 2026-08-13 | area:agents, area:desktop, bug, has repro, platform:windows, regression |
| [#86326](https://github.com/anthropics/claude-code/issues/86326) | \[BUG\] Desktop app: a message delivered to a session that is still starting up is silently lost — the query never starts and the session is dead for the full ~16min watchdog | randie3503 | OPEN | 0 | 1 | 2026-08-15 | 2026-08-13 | area:desktop, bug, data-loss, has repro, platform:windows |
| [#86238](https://github.com/anthropics/claude-code/issues/86238) | Bundled ugrep runs with no memory limit or timeout — model-generated regex consumed 13.6 GB and thrashed the host | hizawye | OPEN | 1 (👍 1) | 2 | 2026-08-15 | 2026-08-13 | — |
| [#86881](https://github.com/anthropics/claude-code/issues/86881) | Desktop: ccd\_session\_mgmt\_\_send\_message reports "Message sent" but never delivers | ivan-barbato | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:desktop, area:mcp, bug, duplicate, platform:windows, regression |
| [#86707](https://github.com/anthropics/claude-code/issues/86707) | \[FEATURE\] Redact credential-shaped values when writing session transcripts | KevinAMullen | OPEN | 0 | 2 | 2026-08-15 | 2026-08-14 | area:core, area:security, enhancement |
| [#61044](https://github.com/anthropics/claude-code/issues/61044) | \[BUG\] MCP tool calls in CCR Routines fail with "requires approval" — no approval UI shown, reconnect does not resolve | beer89447-spec | OPEN | 6 (👍 6) | 14 | 2026-08-15 | 2026-05-21 | area:mcp, area:permissions, area:routines, bug, duplicate, platform:web |
| [#86880](https://github.com/anthropics/claude-code/issues/86880) | You've hit your session limit · resets 3:40pm (Europe/Rome) | CarloSchillaci | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:cost, bug, platform:macos, platform:vscode |
| [#86879](https://github.com/anthropics/claude-code/issues/86879) | Feature request: a supported way to disable the agent\_summary spinner (22.7% of requests, ~18% of weighted tokens in a subagent-heavy session) | rflcrz | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:agents, area:cost, enhancement, platform:macos |
| [#86878](https://github.com/anthropics/claude-code/issues/86878) | \[Bug\] Claude Code lacks persistent session/work history across instances | Najamkh | OPEN | 0 | 0 | 2026-08-15 | 2026-08-15 | area:core, enhancement, platform:windows |
| [#72945](https://github.com/anthropics/claude-code/issues/72945) | \[DOCS\] Sub-agents quickstart still walks through the \`/agents\` wizard that v2.1.198 removed | coygeek | OPEN | 0 | 4 | 2026-08-15 | 2026-07-01 | area:agents, area:docs, bug, documentation |
| [#70811](https://github.com/anthropics/claude-code/issues/70811) | \[Bug\]\[cyber\] Refused to improve PII scrubber for redacting tenant/client IDs and domains in cloud IAM output (req\_011CcPKyX1EgzbWgarVyTH5d) | sworrl | CLOSED / NOT\_PLANNED | 0 | 2 | 2026-08-15 | 2026-06-25 | area:model, area:security, duplicate, platform:linux, stale |
| [#70817](https://github.com/anthropics/claude-code/issues/70817) | \[Bug\]\[aup\] Refused to generate least-privilege IAM policy scoping down over-permissioned service account roles (req\_011CcPetvCKoATwPmRssxwht) | sworrl | CLOSED / NOT\_PLANNED | 0 | 2 | 2026-08-15 | 2026-06-25 | api:anthropic, area:model, bug, duplicate, platform:linux, stale |
| [#70830](https://github.com/anthropics/claude-code/issues/70830) | \[Bug\]\[aup\] Incident-response investigation of a business email compromise and securing the affected mailbox wr (req\_011CcPJ7kxsNsSfA5EEojodo) | sworrl | CLOSED / NOT\_PLANNED | 0 | 2 | 2026-08-15 | 2026-06-25 | api:anthropic, area:model, bug, duplicate, platform:linux, stale |
| [#70844](https://github.com/anthropics/claude-code/issues/70844) | \[Bug\]\[cyber\] False positive blocks routine network admin scripting and TLS certificate automation work (req\_011CcCJ547coZQf8eHXmFmJF) | sworrl | CLOSED / NOT\_PLANNED | 0 | 3 | 2026-08-15 | 2026-06-25 | area:model, duplicate, platform:linux, stale |

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
