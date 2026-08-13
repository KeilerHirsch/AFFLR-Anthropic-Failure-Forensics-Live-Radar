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
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5884 (👍 4549 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
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
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 816 (👍 721 · ❤️ 47 · 🚀 34 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 796 (👍 585 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#65697](https://github.com/anthropics/claude-code/issues/65697) | \[FEATURE\] Official Claude Desktop build for Linux (Ubuntu LTS / Debian) | powell-clark | CLOSED / COMPLETED | 655 (👍 498 · 👎 4 · 🎉 28 · ❤️ 65 · 🚀 35 · 👀 25) | 53 | 2026-08-13 | 2026-06-05 | area:desktop, enhancement, platform:linux |
| [#17432](https://github.com/anthropics/claude-code/issues/17432) | Feature Request: India-Specific Pricing Plans (INR) for Claude &amp; Claude Code | saidev-pbi-fabric | OPEN | 620 (👍 485 · ❤️ 39 · 🚀 81 · 👀 15) | 212 | 2026-08-07 | 2026-01-11 | area:cost, enhancement, external |
| [#2511](https://github.com/anthropics/claude-code/issues/2511) | Feature request: Connect Claude code to Claude projects  | salimmallick | OPEN | 595 (👍 384 · ❤️ 116 · 🚀 59 · 👀 36) | 49 | 2026-07-29 | 2025-06-24 | area:core, enhancement |
| [#6686](https://github.com/anthropics/claude-code/issues/6686) | Feature Request: Add support for Agent Client Protocol (ACP) | coygeek | CLOSED / NOT\_PLANNED | 551 (👍 437 · ❤️ 114) | 37 | 2026-02-19 | 2025-08-27 | area:ide, enhancement, external |
| [#38335](https://github.com/anthropics/claude-code/issues/38335) | \[BUG\] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) | karenrebecag | OPEN | 543 (👍 474 · 😕 42 · 👀 27) | 831 | 2026-07-31 | 2026-03-24 | invalid |
| [#53262](https://github.com/anthropics/claude-code/issues/53262) | HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota | sasha-id | CLOSED / COMPLETED | 532 (👍 213 · 👎 3 · 😄 66 · 😕 230 · 🚀 6 · 👀 14) | 93 | 2026-07-11 | 2026-04-25 | area:cost, bug, has repro, platform:macos |
| [#15942](https://github.com/anthropics/claude-code/issues/15942) | Add support for Visual Studio 2026 Integration | ovftank | OPEN | 516 (👍 414 · 🎉 25 · ❤️ 27 · 🚀 29 · 👀 21) | 149 | 2026-08-11 | 2026-01-01 | area:ide, enhancement, platform:windows |
| [#27302](https://github.com/anthropics/claude-code/issues/27302) | \[FEATURE\] Support multiple Connector accounts (same connector, different accounts) in Claude and Claude Code on the web (claude.ai/code) | nathanmargaglio | OPEN | 480 (👍 344 · ❤️ 109 · 🚀 15 · 👀 12) | 227 | 2026-08-12 | 2026-02-21 | enhancement |
| [#1455](https://github.com/anthropics/claude-code/issues/1455) | Claude Code does not respect the XDG Base Directory specification | jennifgcrl | OPEN | 435 (👍 418 · 👎 1 · 😄 3 · 🎉 4 · ❤️ 6 · 👀 3) | 65 | 2026-08-12 | 2025-05-31 | bug, enhancement, platform:linux |
| [#73125](https://github.com/anthropics/claude-code/issues/73125) | \[BUG\] AskUserQuestion: "No response after 60s — continued without an answer" | ANogin | CLOSED / COMPLETED | 414 (👍 388 · 😄 1 · 😕 16 · 🚀 9) | 143 | 2026-07-09 | 2026-07-02 | api:bedrock, area:tools, area:tui, bug, platform:linux, platform:vscode |
| [#31005](https://github.com/anthropics/claude-code/issues/31005) | Support for AGENTS.md and .agents/skills/, the community has been asking since August 2025 | kvnwolf | OPEN | 412 (👍 309 · 🎉 2 · ❤️ 70 · 👀 31) | 19 | 2026-08-10 | 2026-03-05 | area:core, duplicate, enhancement, memory |
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
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5884 (👍 4549 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
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
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 816 (👍 721 · ❤️ 47 · 🚀 34 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#24964](https://github.com/anthropics/claude-code/issues/24964) | \[BUG\] Cowork: Folder picker rejects folders outside home directory, symlinks/junctions also blocked | aviy009 | CLOSED / COMPLETED | 190 (👍 189 · 😕 1) | 157 | 2026-04-19 | 2026-02-11 | area:ide, bug, has repro, oncall, platform:macos, platform:windows |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 796 (👍 585 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#29579](https://github.com/anthropics/claude-code/issues/29579) | \[BUG\] API Error: Rate limit reached despite Claude Max subscription and only 16% usage | CaptainDaredevil | OPEN | 94 (👍 94) | 153 | 2026-07-27 | 2026-02-28 | area:api, area:auth, bug, has repro, platform:vscode, platform:windows |
| [#33238](https://github.com/anthropics/claude-code/issues/33238) | Claude Code OAuth login fails with a timeout error. \`auth.anthropic.com\` does not resolve via DNS, making it impossible to authenticate. | lokasquad1 | OPEN | 47 (👍 45 · 👀 2) | 153 | 2026-07-20 | 2026-03-11 | area:auth, bug, platform:windows |

</details>

### 🆕 Recently active

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#86448](https://github.com/anthropics/claude-code/issues/86448) | MCP channel notifications with list- or int-valued params.meta fields are silently dropped (no error, connection stays healthy) | bobloy | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | — |
| [#40495](https://github.com/anthropics/claude-code/issues/40495) | \[BUG\] Cowork sessions ignore user hooks and managed settings — sandbox platform mismatch breaks all settings resolution | gmnbs | OPEN | 19 (👍 19) | 21 | 2026-08-13 | 2026-03-29 | area:cowork, area:hooks, bug, has repro, platform:macos |
| [#86446](https://github.com/anthropics/claude-code/issues/86446) | Remote control of a Claude Code session requires being physically at the host machine to enable | jordansloane-coder | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | enhancement |
| [#86447](https://github.com/anthropics/claude-code/issues/86447) | \[BUG\] Print mode (-p --output-format stream-json): session ends with result: success while background tasks are running and a ScheduleWakeup is pending — scheduled wakeup can never fire, background tasks are killed | hhorton-onebrief | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:cli, bug, has repro, platform:linux |
| [#86445](https://github.com/anthropics/claude-code/issues/86445) | \[Bug\] Security vulnerability: Private repository data exposed to production without filtering | NucleuxCO | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:security, bug, needs-repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#81698](https://github.com/anthropics/claude-code/issues/81698) | \[Windows\] Desktop app: GPU process crash (exit code 101457950) kills entire app and all running sessions | J-dev2 | OPEN | 0 | 27 | 2026-08-13 | 2026-07-27 | — |
| [#86430](https://github.com/anthropics/claude-code/issues/86430) | HTTP MCP: valid token treated as expired — "OAuth session expired and could not be refreshed" when provider issues no refresh token (mcp.facebook.com/ads) | farmaconapratica | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:auth, area:mcp, bug, has repro, platform:macos |
| [#86444](https://github.com/anthropics/claude-code/issues/86444) | Desktop app hangs previewing localhost dev server; uninstall/reinstall silently wipes all session transcripts | viswateja-bgf | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, bug, platform:windows |
| [#86443](https://github.com/anthropics/claude-code/issues/86443) | \[BUG\] Desktop app (macOS): scheduled sessions with background tasks leak harness processes indefinitely (task-notification race, follow-up to #39632) | antonelloreho-dot | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:core, area:desktop, bug, has repro, platform:macos |
| [#85471](https://github.com/anthropics/claude-code/issues/85471) | \[BUG\] Suspicious injected instructions repeatedly appended to my own outgoing messages (Code tab) | singtan4 | OPEN | 0 | 1 | 2026-08-13 | 2026-08-10 | bug |
| [#86435](https://github.com/anthropics/claude-code/issues/86435) | Prohibited block forbids all deletion, unscoped — blocks rm, log scrubbing, and cleanup in coding/ops agents | Bitblade | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:agents, area:permissions, enhancement, platform:linux |
| [#86442](https://github.com/anthropics/claude-code/issues/86442) | \[Bug\] Classifiers not working during XDR evaluation despite document submission | sentinel-hydra | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:tui, bug, platform:windows |
| [#86434](https://github.com/anthropics/claude-code/issues/86434) | \[BUG\] \`/goal\`: the Stop-hook condition is frozen at creation time and the verifier cannot see later cancellation | CaptainException | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:hooks, bug, platform:vscode, platform:windows |
| [#86438](https://github.com/anthropics/claude-code/issues/86438) | \[BUG\] \`/goal clear\` typed while the agent is working is treated as chat text and never executed | CaptainException | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:tui, bug, platform:vscode, platform:windows |
| [#86439](https://github.com/anthropics/claude-code/issues/86439) | \[BUG\] \`/goal\` and \`/goal clear\` report "No goal set" after a met/failed verdict while the Stop hook stays armed | CaptainException | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:core, area:hooks, bug, has repro, platform:vscode, platform:windows |
| [#86441](https://github.com/anthropics/claude-code/issues/86441) | Claude generates AL/Business Central code that misuses \[TryFunction\] assuming it rolls back transactions | AlfredoArroyoClikalia | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | bug, model |
| [#86440](https://github.com/anthropics/claude-code/issues/86440) | Agent should stop and report, not work around, a failed Docker context connection | tilusnet | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:model, enhancement |
| [#86437](https://github.com/anthropics/claude-code/issues/86437) | \[MODEL\] Template not replicating | marcheimlich-collab | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | api:anthropic, area:model, bug, model |
| [#86436](https://github.com/anthropics/claude-code/issues/86436) | \[Bug\] Unexpected language switching to Portuguese regardless of configuration | Floeig | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:model, bug, platform:linux |
| [#61889](https://github.com/anthropics/claude-code/issues/61889) | CVP approved user being blocked on completely benign, non-security queries in fresh sessions on claude.ai (not Claude Code). | 7H35C4r3Cr0W | OPEN | 4 (👍 4) | 43 | 2026-08-13 | 2026-05-23 | invalid |
| [#86142](https://github.com/anthropics/claude-code/issues/86142) | MCP servers declaring draft-07 outputSchema are entirely unusable: "unsupported dialect" rejected client-side before dispatch | amitfin | OPEN | 1 (👍 1) | 4 | 2026-08-13 | 2026-08-12 | area:mcp, bug, has repro, platform:macos |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | federicolopeza | OPEN | 12 (👍 12) | 92 | 2026-08-13 | 2026-08-06 | — |
| [#86433](https://github.com/anthropics/claude-code/issues/86433) | Windows desktop 1.28929.0 (MSIX): whole app exits on GPU process crash, triggered by session preview/Browser pane | vopikyou-ui | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, duplicate, platform:windows |
| [#76727](https://github.com/anthropics/claude-code/issues/76727) | Cross-session coordination for independently-launched Claude Code sessions | wshallwshall | OPEN | 0 | 15 | 2026-08-13 | 2026-07-11 | area:agents, area:hooks, enhancement |
| [#24798](https://github.com/anthropics/claude-code/issues/24798) | Inter-session communication for multi-Claude workflows | hmcg001 | OPEN | 21 (👍 21) | 65 | 2026-08-13 | 2026-02-10 | area:core, area:tui, enhancement |

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
