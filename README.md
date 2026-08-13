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
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5883 (👍 4548 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
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
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 815 (👍 720 · ❤️ 47 · 🚀 34 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 796 (👍 585 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#16157](https://github.com/anthropics/claude-code/issues/16157) | \[BUG\] Instantly hitting usage limits with Max subscription | deqrocks | OPEN | 724 (👍 693 · 👎 2 · 🎉 1 · 😕 3 · 🚀 17 · 👀 8) | 1486 | 2026-08-06 | 2026-01-03 | area:api, area:cost, bug, oncall, platform:macos |
| [#65697](https://github.com/anthropics/claude-code/issues/65697) | \[FEATURE\] Official Claude Desktop build for Linux (Ubuntu LTS / Debian) | powell-clark | CLOSED / COMPLETED | 655 (👍 498 · 👎 4 · 🎉 28 · ❤️ 65 · 🚀 35 · 👀 25) | 52 | 2026-08-12 | 2026-06-05 | area:desktop, enhancement, platform:linux |
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
| [#6235](https://github.com/anthropics/claude-code/issues/6235) | Feature Request: Support AGENTS.md. | DylanLIiii | OPEN | 5883 (👍 4548 · 👎 10 · 😄 33 · 🎉 293 · 😕 5 · ❤️ 397 · 🚀 330 · 👀 267) | 347 | 2026-08-08 | 2025-08-21 | area:core, enhancement, memory |
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
| [#18435](https://github.com/anthropics/claude-code/issues/18435) | \[FEATURE\] Add the ability to manage multiple Claude accounts within the Claude Desktop app with easy switching between profiles. | Agentic-Marketer | OPEN | 815 (👍 720 · ❤️ 47 · 🚀 34 · 👀 14) | 164 | 2026-08-10 | 2026-01-15 | area:auth, area:ide, enhancement |
| [#24964](https://github.com/anthropics/claude-code/issues/24964) | \[BUG\] Cowork: Folder picker rejects folders outside home directory, symlinks/junctions also blocked | aviy009 | CLOSED / COMPLETED | 190 (👍 189 · 😕 1) | 157 | 2026-04-19 | 2026-02-11 | area:ide, bug, has repro, oncall, platform:macos, platform:windows |
| [#36151](https://github.com/anthropics/claude-code/issues/36151) | \[FEATURE\] Multi-account switching in Claude Mobile app without shared email | CorneAussems | OPEN | 796 (👍 585 · ❤️ 171 · 🚀 40) | 153 | 2026-08-12 | 2026-03-19 | invalid |
| [#29579](https://github.com/anthropics/claude-code/issues/29579) | \[BUG\] API Error: Rate limit reached despite Claude Max subscription and only 16% usage | CaptainDaredevil | OPEN | 94 (👍 94) | 153 | 2026-07-27 | 2026-02-28 | area:api, area:auth, bug, has repro, platform:vscode, platform:windows |
| [#33238](https://github.com/anthropics/claude-code/issues/33238) | Claude Code OAuth login fails with a timeout error. \`auth.anthropic.com\` does not resolve via DNS, making it impossible to authenticate. | lokasquad1 | OPEN | 47 (👍 45 · 👀 2) | 153 | 2026-07-20 | 2026-03-11 | area:auth, bug, platform:windows |

</details>

### 🆕 Recently active

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#86386](https://github.com/anthropics/claude-code/issues/86386) | \[BUG\] Desktop app: turns triggered by cross-session messages hang at 0 tokens (manual prompts work) | BaltaKid | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:agents, area:desktop, bug, platform:windows, regression |
| [#74715](https://github.com/anthropics/claude-code/issues/74715) | "Always allow" for Claude-in-Chrome site permissions is always persisted as duration:"once" — approved sites list stays empty, prompt repeats for every browser action | kir-kopylov | OPEN | 2 (👍 2) | 8 | 2026-08-13 | 2026-07-06 | area:browser-extension, area:chrome, bug, has repro, platform:windows |
| [#86385](https://github.com/anthropics/claude-code/issues/86385) | Cross-session send\_message delivers to the target session's queue but never triggers a responding turn (regression in desktop 1.28929.0 / CC runtime 2.1.227, still broken in 2.1.231) | RNPS | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:agents, area:desktop, bug, has repro, platform:windows, regression |
| [#86384](https://github.com/anthropics/claude-code/issues/86384) | \[BUG\] Desktop Browser pane: a site on the "Allowed sites" list still raises a permission card on every tool call in Auto mode, claiming site permissions are disabled | level420 | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, area:permissions, bug, has repro, platform:windows |
| [#86383](https://github.com/anthropics/claude-code/issues/86383) | \[BUG\] Desktop: "Disable automatic verification" does not persist, and a hand-written autoVerify: false in .claude/launch.json is overwritten with true shortly after app start | level420 | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, bug, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |
|---:|---|---|---|---:|---:|---|---|---|
| [#86379](https://github.com/anthropics/claude-code/issues/86379) | \[BUG\] Stop hook blocks on dirty/untracked working tree and is reprovisioned every Claude Code web session | kleinarik | OPEN | 0 | 2 | 2026-08-13 | 2026-08-13 | area:claude-code-web, area:hooks, bug, has repro, platform:web |
| [#70062](https://github.com/anthropics/claude-code/issues/70062) | \[BUG\] 'claude-api' is consuming entire context | SenojLuap | OPEN | 5 (👍 5) | 10 | 2026-08-13 | 2026-06-22 | area:skills, bug, has repro, platform:linux |
| [#70881](https://github.com/anthropics/claude-code/issues/70881) | \[BUG\] Claude Desktop falls back to Safari for SSO login when default browser is Arc | omnomwillyum | OPEN | 5 (👍 5) | 6 | 2026-08-13 | 2026-06-25 | area:auth, area:desktop, bug, platform:macos |
| [#86234](https://github.com/anthropics/claude-code/issues/86234) | Claude Desktop (Windows): heavy ad-stack page in in-app Claude Browser pane crashes entire app, no crash dump, kills all hosted sessions | kai-sorensen | OPEN | 0 | 1 | 2026-08-13 | 2026-08-12 | area:desktop, bug, has repro, platform:windows |
| [#74733](https://github.com/anthropics/claude-code/issues/74733) | claude update on Windows reports success but never replaces the launcher (stays on old version) | ronnieshipman | OPEN | 1 (👍 1) | 2 | 2026-08-13 | 2026-07-06 | area:installation, bug, platform:windows |
| [#16128](https://github.com/anthropics/claude-code/issues/16128) | \[FEATURE\] AWS Bedrock authentication support for Chrome extension | joaopixar | OPEN | 113 (👍 113) | 27 | 2026-08-13 | 2026-01-03 | api:bedrock, area:auth, area:ide, enhancement |
| [#86339](https://github.com/anthropics/claude-code/issues/86339) | Auto-mode classifier: ~310s permission decisions that resolve to "Allowed" — the 30s classifier timeout never fires | domagojmedo | CLOSED / COMPLETED | 1 (👍 1) | 1 | 2026-08-13 | 2026-08-13 | area:permissions, bug, platform:windows |
| [#29017](https://github.com/anthropics/claude-code/issues/29017) | \[BUG\] Conversation history is lost in VSCode extension | I571664 | OPEN | 23 (👍 20 · 👀 3) | 29 | 2026-08-13 | 2026-02-26 | area:ide, bug, platform:macos, platform:vscode |
| [#86227](https://github.com/anthropics/claude-code/issues/86227) | \[BUG\] HTTP MCP: OAuth succeeds, then initialize hangs until CONNECT\_TIMEOUT (raising MCP\_TIMEOUT doesn't help) | samirazambujadev | OPEN | 0 | 2 | 2026-08-13 | 2026-08-12 | area:mcp, bug, has repro, platform:macos |
| [#86382](https://github.com/anthropics/claude-code/issues/86382) | Desktop app: prompt suggestions stopped appearing (~12-13 Aug), gated off remotely with no local override | phuazz | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:desktop, bug, platform:windows |
| [#86381](https://github.com/anthropics/claude-code/issues/86381) | \[Bug\] Fullscreen TUI redraw scrolls terminal under GNU screen on WSL2 (regression in 2.1.228) | kstephens-outside | OPEN | 0 | 0 | 2026-08-13 | 2026-08-13 | area:tui, bug, has repro, platform:wsl |
| [#86154](https://github.com/anthropics/claude-code/issues/86154) | --plugin-dir loads plugin skills but never starts the plugin's MCP servers (desktop app sessions lose all plugin MCP tools) | nicolaswarlop-jpg | OPEN | 0 | 1 | 2026-08-13 | 2026-08-12 | area:desktop, area:mcp, area:plugins, bug, has repro, platform:windows |
| [#86375](https://github.com/anthropics/claude-code/issues/86375) | \[BUG\] Auto mode appears to make billed requests that emit no telemetry | pilo-tribe-ai | OPEN | 0 | 1 | 2026-08-13 | 2026-08-13 | api:anthropic, area:cost, area:permissions, bug, has repro, platform:macos |
| [#86377](https://github.com/anthropics/claude-code/issues/86377) | \[Bug\] Keyboard composition characters trigger unintended clipboard paste on macOS | lucashara | OPEN | 0 | 1 | 2026-08-13 | 2026-08-13 | area:tui, bug, platform:macos |
| [#86373](https://github.com/anthropics/claude-code/issues/86373) | Hanja/foreign character substitution recurs in normal chat responses, not just suggestion box | MRJHP | OPEN | 0 | 2 | 2026-08-13 | 2026-08-13 | area:model, bug, platform:vscode, platform:windows |
| [#79759](https://github.com/anthropics/claude-code/issues/79759) | \[BUG\] Permission model: let a specific allow override a broad deny (specificity-aware precedence) | saleem-mirza | OPEN | 1 (👍 1) | 3 | 2026-08-13 | 2026-07-21 | — |
| [#50884](https://github.com/anthropics/claude-code/issues/50884) | \[FEATURE\] Let users remove stale/dead Remote Control environments from the claude.ai/code environment list | wolfomania | OPEN | 28 (👍 28) | 8 | 2026-08-13 | 2026-04-19 | area:claude-code-web, area:cli, enhancement |
| [#75064](https://github.com/anthropics/claude-code/issues/75064) | \[BUG\] re-opening #63590 on behalf of OP: Context/compact button triggers compact on single click with no confirmation or undo | williamrobotma | OPEN | 2 (👍 2) | 1 | 2026-08-13 | 2026-07-07 | area:ide, duplicate, platform:vscode, user-experience |
| [#65961](https://github.com/anthropics/claude-code/issues/65961) | \[MODEL\] Claude verbose code comments by default — ignores instructions to stop. | bhuvarloka | OPEN | 105 (👍 105) | 10 | 2026-08-13 | 2026-06-07 | area:model, bug, model |
| [#86378](https://github.com/anthropics/claude-code/issues/86378) | HTTP MCP client works in long-running sessions but fails at connect in brand-new sessions on the identical CLI version | caprar-mms | CLOSED / DUPLICATE | 0 | 1 | 2026-08-13 | 2026-08-13 | area:mcp, bug, has repro, platform:macos |

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
