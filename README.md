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
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5879 (👍 4544 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
| [#42796](https://github.com/anthropics/claude-code/issues/42796) | \[MODEL\] Claude Code is unusable for complex engineering tasks with the Feb updates | stellaraccident | CLOSED / COMPLETED | 3286 (👍 2072 · 👎 8 · 😄 149 · 🎉 114 · 😕 59 · ❤️ 436 · 🚀 231 · 👀 217) | 583 | 2026-04-24 | 2026-04-02 | area:model, bug, model |
| [#45596](https://github.com/anthropics/claude-code/issues/45596) | Bring Back Buddy — A Consolidated Plea from the Community | Hujoepandiselvan | OPEN | 2068 (👍 1167 · 👎 5 · 😄 36 · 🎉 1 · ❤️ 639 · 🚀 68 · 👀 152) | 266 | 2026-08-12 | 2026-04-09 | area:skills, area:tui, duplicate, enhancement |
| [#17118](https://github.com/anthropics/claude-code/issues/17118) | \[Feature Request\] Support for OpenCode and Max plan | shawnyeager | CLOSED / COMPLETED | 1416 (👍 797 · 👎 8 · 😄 12 · 😕 4 · ❤️ 514 · 🚀 81) | 410 | 2026-02-09 | 2026-01-09 | area:auth, bug, has repro, oncall, platform:linux |
| [#3382](https://github.com/anthropics/claude-code/issues/3382) | \[BUG\] Claude says "You're absolutely right!" about everything | scottleibrand | CLOSED / COMPLETED | 1375 (👍 873 · 😄 337 · ❤️ 126 · 👀 39) | 179 | 2025-09-20 | 2025-07-12 | area:core, area:model, bug, duplicate |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#34229](https://github.com/anthropics/claude-code/issues/34229) | \[BUG\] Phone verification | jpiabrantes | OPEN | 892 (👍 821 · 🎉 15 · ❤️ 21 · 🚀 19 · 👀 16) | 742 | 2026-07-19 | 2026-03-14 | invalid |
| [#3648](https://github.com/anthropics/claude-code/issues/3648) | Terminal Scrolling Uncontrollably During Claude Code Interaction | JacobGoldenArt | CLOSED / COMPLETED | 837 (👍 694 · 👎 3 · 😄 2 · 🎉 4 · 😕 45 · ❤️ 31 · 🚀 16 · 👀 42) | 337 | 2026-02-06 | 2025-07-16 | area:auth, area:ide, area:tui, bug, oncall, platform:macos |
| [#826](https://github.com/anthropics/claude-code/issues/826) | \[BUG\] Console scrolling top of history when claude add text to the console | ocontant | OPEN / REOPENED | 823 (👍 691 · 😄 15 · 🎉 2 · 😕 15 · ❤️ 7 · 🚀 15 · 👀 78) | 354 | 2026-07-29 | 2025-04-19 | bug, duplicate, oncall, platform:macos |
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 810 (👍 717 · ❤️ 46 · 🚀 33 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 794 (👍 583 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#65697](https://github.com/anthropics/claude-code/issues/65697) | \[FEATURE\] Official Claude Desktop build for Linux (Ubuntu LTS / Debian) | powell-clark | CLOSED / COMPLETED | 655 (👍 498 · 👎 4 · 🎉 28 · ❤️ 65 · 🚀 35 · 👀 25) | 52 | 2026-08-12 | 2026-06-05 | area:desktop, enhancement, platform:linux |
| [#17432](https://github.com/anthropics/claude-code/issues/17432) | Feature Request: India-Specific Pricing Plans (INR) for Claude &amp; Claude Code | saidev-pbi-fabric | OPEN | 620 (👍 485 · ❤️ 39 · 🚀 81 · 👀 15) | 212 | 2026-08-07 | 2026-01-11 | area:cost, enhancement, external |
| [#2511](https://github.com/anthropics/claude-code/issues/2511) | Feature request: Connect Claude code to Claude projects  | salimmallick | OPEN | 595 (👍 384 · ❤️ 116 · 🚀 59 · 👀 36) | 49 | 2026-07-29 | 2025-06-24 | area:core, enhancement |
| [#6686](https://github.com/anthropics/claude-code/issues/6686) | Feature Request: Add support for Agent Client Protocol (ACP) | coygeek | CLOSED / NOT\_PLANNED | 551 (👍 437 · ❤️ 114) | 37 | 2026-02-19 | 2025-08-27 | area:ide, enhancement, external |
| [#38335](https://github.com/anthropics/claude-code/issues/38335) | \[BUG\] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) | karenrebecag | OPEN | 543 (👍 474 · 😕 42 · 👀 27) | 831 | 2026-07-31 | 2026-03-24 | invalid |
| [#53262](https://github.com/anthropics/claude-code/issues/53262) | HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota | sasha-id | CLOSED / COMPLETED | 532 (👍 213 · 👎 3 · 😄 66 · 😕 230 · 🚀 6 · 👀 14) | 93 | 2026-07-11 | 2026-04-25 | area:cost, bug, has repro, platform:macos |
| [#15942](https://github.com/anthropics/claude-code/issues/15942) | Add support for Visual Studio 2026 Integration | ovftank | OPEN | 515 (👍 413 · 🎉 25 · ❤️ 27 · 🚀 29 · 👀 21) | 149 | 2026-08-11 | 2026-01-01 | area:ide, enhancement, platform:windows |
| [#27302](https://github.com/anthropics/claude-code/issues/27302) | \[FEATURE\] Support multiple Connector accounts (same connector, different accounts) in Claude and Claude Code on the web (claude.ai/code) | nathanmargaglio | OPEN | 480 (👍 344 · ❤️ 109 · 🚀 15 · 👀 12) | 227 | 2026-08-12 | 2026-02-21 | enhancement |
| [#1455](https://github.com/anthropics/claude-code/issues/1455) | Claude Code does not respect the XDG Base Directory specification | jennifgcrl | OPEN | 434 (👍 417 · 👎 1 · 😄 3 · 🎉 4 · ❤️ 6 · 👀 3) | 65 | 2026-08-12 | 2025-05-31 | bug, enhancement, platform:linux |
| [#73125](https://github.com/anthropics/claude-code/issues/73125) | \[BUG\] AskUserQuestion: "No response after 60s — continued without an answer" | ANogin | CLOSED / COMPLETED | 414 (👍 388 · 😄 1 · 😕 16 · 🚀 9) | 143 | 2026-07-09 | 2026-07-02 | api:bedrock, area:tools, area:tui, bug, platform:linux, platform:vscode |
| [#31005](https://github.com/anthropics/claude-code/issues/31005) | Support for AGENTS.md and .agents/skills/, the community has been asking since August 2025 | kvnwolf | OPEN | 411 (👍 308 · 🎉 2 · ❤️ 70 · 👀 31) | 19 | 2026-08-10 | 2026-03-05 | area:core, duplicate, enhancement, memory |
| [#6915](https://github.com/anthropics/claude-code/issues/6915) | Allow MCP tools to be available only to subagent | eli0shin | CLOSED / COMPLETED | 378 (👍 271 · ❤️ 57 · 🚀 40 · 👀 10) | 89 | 2026-03-23 | 2025-08-31 | area:mcp, duplicate, enhancement |
| [#8477](https://github.com/anthropics/claude-code/issues/8477) | \[FEATURE\] Add Option to Always Show Claude's Thinking | janbam | OPEN | 356 (👍 329 · 👎 1 · 👀 26) | 92 | 2026-07-26 | 2025-09-30 | area:tui, enhancement |
| [#46829](https://github.com/anthropics/claude-code/issues/46829) | Cache TTL silently regressed from 1h to 5m around early March 2026, causing quota and cost inflation | seanGSISG | CLOSED / NOT\_PLANNED | 342 (👍 245 · 😕 24 · ❤️ 24 · 👀 49) | 56 | 2026-06-28 | 2026-04-12 | api:anthropic, area:cost, bug, has repro |

</details>

### 💬 Most discussed

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#38335](https://github.com/anthropics/claude-code/issues/38335) | \[BUG\] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) | karenrebecag | OPEN | 543 (👍 474 · 😕 42 · 👀 27) | 831 | 2026-07-31 | 2026-03-24 | invalid |
| [#34229](https://github.com/anthropics/claude-code/issues/34229) | \[BUG\] Phone verification | jpiabrantes | OPEN | 892 (👍 821 · 🎉 15 · ❤️ 21 · 🚀 19 · 👀 16) | 742 | 2026-07-19 | 2026-03-14 | invalid |
| [#42796](https://github.com/anthropics/claude-code/issues/42796) | \[MODEL\] Claude Code is unusable for complex engineering tasks with the Feb updates | stellaraccident | CLOSED / COMPLETED | 3286 (👍 2072 · 👎 8 · 😄 149 · 🎉 114 · 😕 59 · ❤️ 436 · 🚀 231 · 👀 217) | 583 | 2026-04-24 | 2026-04-02 | area:model, bug, model |
| [#17118](https://github.com/anthropics/claude-code/issues/17118) | \[Feature Request\] Support for OpenCode and Max plan | shawnyeager | CLOSED / COMPLETED | 1416 (👍 797 · 👎 8 · 😄 12 · 😕 4 · ❤️ 514 · 🚀 81) | 410 | 2026-02-09 | 2026-01-09 | area:auth, bug, has repro, oncall, platform:linux |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#826](https://github.com/anthropics/claude-code/issues/826) | \[BUG\] Console scrolling top of history when claude add text to the console | ocontant | OPEN / REOPENED | 823 (👍 691 · 😄 15 · 🎉 2 · 😕 15 · ❤️ 7 · 🚀 15 · 👀 78) | 354 | 2026-07-29 | 2025-04-19 | bug, duplicate, oncall, platform:macos |
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5879 (👍 4544 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
| [#3648](https://github.com/anthropics/claude-code/issues/3648) | Terminal Scrolling Uncontrollably During Claude Code Interaction | JacobGoldenArt | CLOSED / COMPLETED | 837 (👍 694 · 👎 3 · 😄 2 · 🎉 4 · 😕 45 · ❤️ 31 · 🚀 16 · 👀 42) | 337 | 2026-02-06 | 2025-07-16 | area:auth, area:ide, area:tui, bug, oncall, platform:macos |
| [#769](https://github.com/anthropics/claude-code/issues/769) | \[BUG\]  In-progress Call causes Screen Flickering | Cheffromspace | OPEN / REOPENED | 335 (👍 300 · 😄 3 · 😕 13 · 👀 19) | 307 | 2026-07-16 | 2025-04-12 | area:tools, area:tui, bug, oncall |
| [#3572](https://github.com/anthropics/claude-code/issues/3572) | Anthropic API Overloaded Error with Repeated 529 Status Codes | wepajoli | CLOSED / COMPLETED | 142 (👍 124 · 😕 10 · 👀 8) | 274 | 2025-08-02 | 2025-07-15 | area:api, area:auth, area:packaging, bug, has repro, platform:macos |
| [#8763](https://github.com/anthropics/claude-code/issues/8763) | API Error: 400 due to tool use concurrency issues. Run /rewind to recover the conversation. - \[Bug\] Anthropic API Error: Unexpected 400 Bad Request Response | ariccio | CLOSED / COMPLETED | 277 (👍 238 · 😕 36 · 👀 3) | 270 | 2025-11-27 | 2025-10-02 | area:api, area:core, area:tools, bug, has repro, oncall, platform:macos |
| [#45596](https://github.com/anthropics/claude-code/issues/45596) | Bring Back Buddy — A Consolidated Plea from the Community | Hujoepandiselvan | OPEN | 2068 (👍 1167 · 👎 5 · 😄 36 · 🎉 1 · ❤️ 639 · 🚀 68 · 👀 152) | 266 | 2026-08-12 | 2026-04-09 | area:skills, area:tui, duplicate, enhancement |
| [#27302](https://github.com/anthropics/claude-code/issues/27302) | \[FEATURE\] Support multiple Connector accounts (same connector, different accounts) in Claude and Claude Code on the web (claude.ai/code) | nathanmargaglio | OPEN | 480 (👍 344 · ❤️ 109 · 🚀 15 · 👀 12) | 227 | 2026-08-12 | 2026-02-21 | enhancement |
| [#17432](https://github.com/anthropics/claude-code/issues/17432) | Feature Request: India-Specific Pricing Plans (INR) for Claude &amp; Claude Code | saidev-pbi-fabric | OPEN | 620 (👍 485 · ❤️ 39 · 🚀 81 · 👀 15) | 212 | 2026-08-07 | 2026-01-11 | area:cost, enhancement, external |
| [#1913](https://github.com/anthropics/claude-code/issues/1913) | Terminal Flickering | PierrunoYT | OPEN | 321 (👍 321) | 187 | 2026-07-09 | 2025-06-10 | area:tui, bug, duplicate, oncall |
| [#4928](https://github.com/anthropics/claude-code/issues/4928) | \[BUG\] file named nul created on windows | rweijnen | CLOSED / COMPLETED | 235 (👍 235) | 184 | 2026-03-23 | 2025-08-01 | area:tools, bug, has repro, oncall, platform:windows |
| [#46987](https://github.com/anthropics/claude-code/issues/46987) | \[BUG\]  API Error: Stream idle timeout - partial response received - multiple time today | ac-monty | OPEN | 197 (👍 168 · 😕 20 · 👀 9) | 184 | 2026-07-09 | 2026-04-12 | api:anthropic, duplicate, platform:macos |
| [#5088](https://github.com/anthropics/claude-code/issues/5088) | Claude Account Disabled After Payment for Claude Code Max 5x Plan | thinhbuzz | OPEN | 66 (👍 60 · 👀 6) | 181 | 2026-07-20 | 2025-08-04 | area:auth, area:cost, bug, oncall |
| [#3382](https://github.com/anthropics/claude-code/issues/3382) | \[BUG\] Claude says "You're absolutely right!" about everything | scottleibrand | CLOSED / COMPLETED | 1375 (👍 873 · 😄 337 · ❤️ 126 · 👀 39) | 179 | 2025-09-20 | 2025-07-12 | area:core, area:model, bug, duplicate |
| [#18866](https://github.com/anthropics/claude-code/issues/18866) | \[BUG\] Auto-compact not triggering on Claude.ai (web &amp; desktop) despite being marked as fixed | solangerainha | CLOSED / COMPLETED | 65 (👍 65) | 176 | 2026-02-28 | 2026-01-17 | bug, invalid |
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 810 (👍 717 · ❤️ 46 · 🚀 33 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#24964](https://github.com/anthropics/claude-code/issues/24964) | \[BUG\] Cowork: Folder picker rejects folders outside home directory, symlinks/junctions also blocked | aviy009 | CLOSED / COMPLETED | 190 (👍 189 · 😕 1) | 157 | 2026-04-19 | 2026-02-11 | area:ide, bug, has repro, oncall, platform:macos, platform:windows |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 794 (👍 583 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#29579](https://github.com/anthropics/claude-code/issues/29579) | \[BUG\] API Error: Rate limit reached despite Claude Max subscription and only 16% usage | CaptainDaredevil | OPEN | 94 (👍 94) | 153 | 2026-07-27 | 2026-02-28 | area:api, area:auth, bug, has repro, platform:vscode, platform:windows |
| [#33238](https://github.com/anthropics/claude-code/issues/33238) | Claude Code OAuth login fails with a timeout error. \`auth.anthropic.com\` does not resolve via DNS, making it impossible to authenticate. | lokasquad1 | OPEN | 47 (👍 45 · 👀 2) | 153 | 2026-07-20 | 2026-03-11 | area:auth, bug, platform:windows |

</details>

### 🆕 Recently active

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#79793](https://github.com/anthropics/claude-code/issues/79793) | \[Bug\] Auto-Compact consumes excessive session usage quota | fab-c14 | OPEN | 0 | 1 | 2026-08-13 | 2026-07-21 | — |
| [#86260](https://github.com/anthropics/claude-code/issues/86260) | \[Bug\] Agent ignoring explicit user instructions and executing unauthorized actions | MetaEnzo | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | — |
| [#86233](https://github.com/anthropics/claude-code/issues/86233) | MCP OAuth loopback redirect uses 127.0.0.1 instead of localhost — breaks providers (e.g. Salesforce) that only allow localhost callback URLs | alex-magill | OPEN | 0 | 1 | 2026-08-13 | 2026-08-12 | area:auth, area:mcp, bug, has repro |
| [#84040](https://github.com/anthropics/claude-code/issues/84040) | Sidebar project grouping is inconsistent; add a way to disable directory-based grouping | twilightit-dev | OPEN | 2 (👍 2) | 1 | 2026-08-13 | 2026-08-05 | — |
| [#86259](https://github.com/anthropics/claude-code/issues/86259) | \[FEATURE\] Show each session's working directory in the desktop sidebar | sg650 | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, area:ui, enhancement |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#71539](https://github.com/anthropics/claude-code/issues/71539) | \[BUG\] Mouse click to refocus terminal triggers permission prompt unintentionally | quenti77 | OPEN | 23 (👍 23) | 11 | 2026-08-13 | 2026-06-26 | area:permissions, area:tui, bug, platform:linux |
| [#86111](https://github.com/anthropics/claude-code/issues/86111) | Repeated hard-stop "API Error: Sonnet 5 can't help with this. Start a new session to continue" errors | craigaspmdinc-droid | OPEN | 0 | 1 | 2026-08-13 | 2026-08-12 | area:model, bug, platform:vscode, platform:windows |
| [#77819](https://github.com/anthropics/claude-code/issues/77819) | \[BUG\] Fable 5 on Max: "You've hit your monthly spend limit" despite Unlimited spend limit and meters at 5% session / 41% weekly | ciaran-finnegan | OPEN | 0 | 2 | 2026-08-13 | 2026-07-15 | area:cost, bug, platform:macos |
| [#86258](https://github.com/anthropics/claude-code/issues/86258) | \[Bug\] Agent hallucinates and over-interprets instructions, causing uncontrolled execution and token wastage | Leo-TakumaSugashi | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:model, bug, platform:macos |
| [#86257](https://github.com/anthropics/claude-code/issues/86257) | Feature request: Korean (한글) bilingual display for CLI chrome text (spinner verbs, "Tip:" lines) | enjoyinglife989 | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:tui, enhancement |
| [#80876](https://github.com/anthropics/claude-code/issues/80876) | \[BUG\] Interrupted auto-update leaves MSIX in Servicing/Staged state (AddPackage times out after 5 min); orphaned CoworkVMService undeletable via SCM even as SYSTEM | eduleitner | OPEN | 2 (👍 2) | 2 | 2026-08-13 | 2026-07-24 | bug |
| [#81301](https://github.com/anthropics/claude-code/issues/81301) | Assistant authored a fabricated user turn, acted on its instructions, and the text re-entered as user input | hrmtz | OPEN | 0 | 4 | 2026-08-13 | 2026-07-26 | — |
| [#84667](https://github.com/anthropics/claude-code/issues/84667) | \[Bug\] Subagents inherit session model without cost confirmation, causing unintended quota drain on limited-quota models | Founder-NeutronTech | OPEN | 0 | 1 | 2026-08-13 | 2026-08-06 | — |
| [#86256](https://github.com/anthropics/claude-code/issues/86256) | Agent states unverifiable claims about external/client-side system state as confirmed fact, then repeats the same failure mode immediately after correction | bm-agent-ops | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:agent, area:model, bug, platform:wsl |
| [#86112](https://github.com/anthropics/claude-code/issues/86112) | \[Bug\] Claude Code ignores conciseness instructions and over-elaborates responses | FysicsTeachr | OPEN | 0 | 2 | 2026-08-13 | 2026-08-12 | area:model, bug, needs-repro, platform:windows |
| [#72692](https://github.com/anthropics/claude-code/issues/72692) | CLI /model picker doesn't list Sonnet 5 as a preset; shows custom model instead | palminha | OPEN | 1 (👍 1) | 8 | 2026-08-13 | 2026-07-01 | area:tui, bug, platform:macos |
| [#53516](https://github.com/anthropics/claude-code/issues/53516) | \[FEATURE\] Stable, documented schema for ~/.claude/projects/&lt;encoded-cwd&gt;/&lt;uuid&gt;.jsonl line types | Mike-AugmentisLabs | OPEN | 5 (👍 5) | 8 | 2026-08-13 | 2026-04-26 | area:docs, area:ide, enhancement |
| [#86255](https://github.com/anthropics/claude-code/issues/86255) | Subagent-attributed "Ready to code?" approval dialog shows the AO's own plan-mode content, not the subagent's, and isn't gated on the subagent actually requesting approval | aldelbal | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:agents, bug, has repro, platform:macos |
| [#84192](https://github.com/anthropics/claude-code/issues/84192) | \[Feature Request\] Reimplement Claude Code in pure Rust to eliminate CPU spikes and terminal flickering | Aditya-Nagariya | OPEN | 1 (👍 1) | 1 | 2026-08-13 | 2026-08-05 | — |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | federicolopeza | OPEN | 12 (👍 12) | 83 | 2026-08-13 | 2026-08-06 | — |
| [#85904](https://github.com/anthropics/claude-code/issues/85904) | \[BUG\] PreToolUse hooks are registered and listed by /hooks, but never execute (v2.1.219, Windows) | mukaihiroyuki | OPEN | 0 | 1 | 2026-08-13 | 2026-08-11 | area:hooks, bug, duplicate, has repro, platform:windows |
| [#86197](https://github.com/anthropics/claude-code/issues/86197) | \[Bug\] Anthropic API Error: Content Flagged by Safety Filters on Legitimate Code Tasks | creativeheadz | OPEN | 1 (👍 1) | 1 | 2026-08-13 | 2026-08-12 | area:model, bug, platform:linux |
| [#86252](https://github.com/anthropics/claude-code/issues/86252) | Claude in Chrome extension won't connect to any Cowork session (cloud or local) — "Sign-in unavailable, must be opened from claude.com" | wilkinsonjames1991-gif | OPEN | 0 | 1 | 2026-08-13 | 2026-08-13 | area:chrome, area:cowork, bug, platform:windows |
| [#86245](https://github.com/anthropics/claude-code/issues/86245) | \[BUG\] ScheduleWakeup has no fallback when tengu\_kairos\_loop\_dynamic is off — self-pacing unreachable for all non-first-party deployments, and non-/loop callers fail opaquely | spencer-carver | OPEN | 0 | 2 | 2026-08-13 | 2026-08-13 | area:core, area:providers, area:skills, bug, has repro |
| [#86254](https://github.com/anthropics/claude-code/issues/86254) | Plugin-namespaced slash commands (plugin:skill) feel cluttered in the picker/autocomplete | michaelspears | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:plugins, area:skills, enhancement, user-experience |

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
