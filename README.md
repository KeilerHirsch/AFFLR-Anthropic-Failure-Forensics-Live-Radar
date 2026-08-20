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
| [#87006](https://github.com/anthropics/claude-code/issues/87006) | \[BUG\] Windows Desktop: Remote Control sessions repeatedly disconnect after clean reinstall; resumed and forked sessions cannot stay attached | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-15 | area:desktop, bug, has repro, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88169](https://github.com/anthropics/claude-code/issues/88169) | \[BUG\] list\_sessions\_request hangs on SMB-mounted workspaces (VS Code extension, v2.1.237) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:ide, duplicate, platform:vscode, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88145](https://github.com/anthropics/claude-code/issues/88145) | \[MODEL\] Claude autonomously launches costly subagents without explicit consent | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:cost, area:permissions, enhancement |
| [#87190](https://github.com/anthropics/claude-code/issues/87190) | \[FEATURE\] Attach a terminal to a Remote Control session running on another machine | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-16 | area:cli, enhancement |
| [#88134](https://github.com/anthropics/claude-code/issues/88134) | Subagent (Agent tool) result flagged by harness as instruction poisoning: fabricated docs example steering toward .env exfiltration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:security, bug, platform:linux |
| [#79883](https://github.com/anthropics/claude-code/issues/79883) | Memory feature's own directory (~/.claude/projects/&lt;id&gt;/memory/) is blocked by the .claude sensitive-file guardrail — no way to pre-authorize | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80170](https://github.com/anthropics/claude-code/issues/80170) | \[Bug\] Permission classifier blocks safe command phrasings during production incidents, ignoring settings.json allowlists | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:permissions |
| [#80045](https://github.com/anthropics/claude-code/issues/80045) | Security: MCP server \`env\` secrets exposed in plaintext via \`--mcp-config\` argv (visible in \`ps\`/\`/proc\`/EDR logs) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:ide |
| [#79750](https://github.com/anthropics/claude-code/issues/79750) | \[Bug\] Auto-mode classifier inherits \[1m\] suffix, causing repeated permission check failures and session lockout | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80552](https://github.com/anthropics/claude-code/issues/80552) | Auto-mode classifier denies a destructive MCP tool call after it already succeeded (mismatched tool\_use\_id) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:permissions |
| [#81100](https://github.com/anthropics/claude-code/issues/81100) | \[BUG\] Desktop app: 30-day retention sweep deletes the only copy of Desktop transcripts, leaving unopenable ghost entries in the session list | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:desktop |
| [#81142](https://github.com/anthropics/claude-code/issues/81142) | Auto mode classifier sends \[1m\]-suffixed model without the 1M beta header; HTTP 400 is reported as "temporarily unavailable" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81378](https://github.com/anthropics/claude-code/issues/81378) | PowerShell command blocked citing a path unrelated to the command; here-string text content is scanned as code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-26 | area:permissions |
| [#80426](https://github.com/anthropics/claude-code/issues/80426) | Desktop app (Windows/MSIX) intermittently fails to start after self-inflicted race condition on native-host install; recovery wipes local session index | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:desktop |
| [#80999](https://github.com/anthropics/claude-code/issues/80999) | Windows: hidden Browser-pane preview kills the app via Code Integrity block on packaged vk\_swiftshader.dll, then "Repair" dialog | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:desktop |
| [#81041](https://github.com/anthropics/claude-code/issues/81041) | permissions.ask rules are loaded and displayed in /permissions but never enforced (2.1.219, macOS) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81526](https://github.com/anthropics/claude-code/issues/81526) | \[BUG\] Sandbox silently deletes project-root \`refs/\`, \`objects/\`, \`HEAD\` created mid-session — recursive, no prompt (macOS, 2.1.220) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:core |
| [#82167](https://github.com/anthropics/claude-code/issues/82167) | \[Bug\] Settings file corrupted to \`{}\` by stale in-memory config persisting over concurrent writes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-29 | area:core |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82748](https://github.com/anthropics/claude-code/issues/82748) | \[Bug\] \`claude-opus-5\` absent from client model table on 2.1.212 — /context uses a 200K denominator while auto-compact and the API both use 1M | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-30 | area:core |
| [#87348](https://github.com/anthropics/claude-code/issues/87348) | Endless SecurityAgent prompt stack for "Claude Code-credentials": credential rewrite creates keychain partition mismatch, "Always Allow" can never persist (behavior persists after #41026 was closed as resolved) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-17 | area:auth, area:security, bug, has repro, platform:macos, platform:vscode |
| [#88131](https://github.com/anthropics/claude-code/issues/88131) | \[Bug\] Fable 5 persistent premature-closure pressure overrides explicit anti-closure instructions and degrades investigation, implementation, and verification during benign coding work | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#87006](https://github.com/anthropics/claude-code/issues/87006) | \[BUG\] Windows Desktop: Remote Control sessions repeatedly disconnect after clean reinstall; resumed and forked sessions cannot stay attached | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-15 | area:desktop, bug, has repro, platform:windows |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#88169](https://github.com/anthropics/claude-code/issues/88169) | \[BUG\] list\_sessions\_request hangs on SMB-mounted workspaces (VS Code extension, v2.1.237) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:ide, duplicate, platform:vscode, platform:windows |
| [#84352](https://github.com/anthropics/claude-code/issues/84352) | \[BUG\] CVP-approved Claude.ai organization still receives cyber safeguard blocks in Claude Code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-06 | — |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88145](https://github.com/anthropics/claude-code/issues/88145) | \[MODEL\] Claude autonomously launches costly subagents without explicit consent | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:cost, area:permissions, enhancement |
| [#87190](https://github.com/anthropics/claude-code/issues/87190) | \[FEATURE\] Attach a terminal to a Remote Control session running on another machine | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-16 | area:cli, enhancement |
| [#88134](https://github.com/anthropics/claude-code/issues/88134) | Subagent (Agent tool) result flagged by harness as instruction poisoning: fabricated docs example steering toward .env exfiltration | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:security, bug, platform:linux |
| [#79883](https://github.com/anthropics/claude-code/issues/79883) | Memory feature's own directory (~/.claude/projects/&lt;id&gt;/memory/) is blocked by the .claude sensitive-file guardrail — no way to pre-authorize | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80170](https://github.com/anthropics/claude-code/issues/80170) | \[Bug\] Permission classifier blocks safe command phrasings during production incidents, ignoring settings.json allowlists | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:permissions |
| [#80045](https://github.com/anthropics/claude-code/issues/80045) | Security: MCP server \`env\` secrets exposed in plaintext via \`--mcp-config\` argv (visible in \`ps\`/\`/proc\`/EDR logs) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-22 | area:ide |
| [#79750](https://github.com/anthropics/claude-code/issues/79750) | \[Bug\] Auto-mode classifier inherits \[1m\] suffix, causing repeated permission check failures and session lockout | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-21 | area:permissions |
| [#80552](https://github.com/anthropics/claude-code/issues/80552) | Auto-mode classifier denies a destructive MCP tool call after it already succeeded (mismatched tool\_use\_id) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:permissions |
| [#81100](https://github.com/anthropics/claude-code/issues/81100) | \[BUG\] Desktop app: 30-day retention sweep deletes the only copy of Desktop transcripts, leaving unopenable ghost entries in the session list | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:desktop |
| [#81142](https://github.com/anthropics/claude-code/issues/81142) | Auto mode classifier sends \[1m\]-suffixed model without the 1M beta header; HTTP 400 is reported as "temporarily unavailable" | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81378](https://github.com/anthropics/claude-code/issues/81378) | PowerShell command blocked citing a path unrelated to the command; here-string text content is scanned as code | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-26 | area:permissions |
| [#80426](https://github.com/anthropics/claude-code/issues/80426) | Desktop app (Windows/MSIX) intermittently fails to start after self-inflicted race condition on native-host install; recovery wipes local session index | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-23 | area:desktop |
| [#80999](https://github.com/anthropics/claude-code/issues/80999) | Windows: hidden Browser-pane preview kills the app via Code Integrity block on packaged vk\_swiftshader.dll, then "Repair" dialog | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-24 | area:desktop |
| [#81041](https://github.com/anthropics/claude-code/issues/81041) | permissions.ask rules are loaded and displayed in /permissions but never enforced (2.1.219, macOS) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-25 | area:permissions |
| [#81526](https://github.com/anthropics/claude-code/issues/81526) | \[BUG\] Sandbox silently deletes project-root \`refs/\`, \`objects/\`, \`HEAD\` created mid-session — recursive, no prompt (macOS, 2.1.220) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:core |
| [#82167](https://github.com/anthropics/claude-code/issues/82167) | \[Bug\] Settings file corrupted to \`{}\` by stale in-memory config persisting over concurrent writes | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-29 | area:core |
| [#81727](https://github.com/anthropics/claude-code/issues/81727) | Skills have no enforceable phase gating: invoked skill's mandatory procedure silently skipped, and MCP writes bypass the hook layer entirely | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-27 | area:hooks, area:skills |
| [#82748](https://github.com/anthropics/claude-code/issues/82748) | \[Bug\] \`claude-opus-5\` absent from client model table on 2.1.212 — /context uses a 200K denominator while auto-compact and the API both use 1M | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-30 | area:core |
| [#88131](https://github.com/anthropics/claude-code/issues/88131) | \[Bug\] Fable 5 persistent premature-closure pressure overrides explicit anti-closure instructions and degrades investigation, implementation, and verification during benign coding work | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug |
| [#74913](https://github.com/anthropics/claude-code/issues/74913) | \[BUG\] Claude Desktop (macOS): chat MCP tool calls time out with zero network activity when a system PAC is configured; configured MCP server stays connected and never receives tools/call | OPEN / REOPENED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-07-06 | area:desktop, area:mcp, invalid, stale |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88175](https://github.com/anthropics/claude-code/issues/88175) | \[Bug\] Anthropic API Error: Reasoning extraction safeguard false positive on consecutive tool calls | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:windows |
| [#88174](https://github.com/anthropics/claude-code/issues/88174) | \[cyber\] Security vulnerability report: Unauthorized premium license escalation via payment bypass | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:tui, bug, platform:windows |
| [#88172](https://github.com/anthropics/claude-code/issues/88172) | MCP connector serves a stale tools/list after a server adds tools — only an app relaunch refreshes it (a new conversation and re-issued server/discover do not) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:mcp, bug, platform:macos |
| [#88171](https://github.com/anthropics/claude-code/issues/88171) | \[BUG\] /context in Claude Code for VS Code causes request spikes and may trigger rate limits or DoS protection | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | bug |
| [#88170](https://github.com/anthropics/claude-code/issues/88170) | \[BUG\] Marketplace-entry dependencies: version constraints silently ignored, prune deletes live dependencies | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:plugins, bug, has repro, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88169](https://github.com/anthropics/claude-code/issues/88169) | \[BUG\] list\_sessions\_request hangs on SMB-mounted workspaces (VS Code extension, v2.1.237) | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:ide, duplicate, platform:vscode, platform:windows |
| [#88168](https://github.com/anthropics/claude-code/issues/88168) | Desktop app: chat scrollback permanently truncated at a fixed mid-conversation point after app restart (session JSONL intact) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos |
| [#88167](https://github.com/anthropics/claude-code/issues/88167) | \[Feature Request\] Add security context mode for local vulnerability testing | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, enhancement, platform:macos |
| [#88166](https://github.com/anthropics/claude-code/issues/88166) | \[FEATURE\] remote-control: a supported way to run it as a persistent service (survive reboot, crash, and auto-update) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:core, enhancement, platform:macos |
| [#88165](https://github.com/anthropics/claude-code/issues/88165) | Feature request: secrets locker / credential broker - password manager fills fields, model never sees values (accessibility) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:a11y, area:security, enhancement |
| [#88164](https://github.com/anthropics/claude-code/issues/88164) | /skills prints "No changes" instead of the skill list, and misses skills added mid-session | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:cli, area:skills, bug, has repro, platform:macos |
| [#88163](https://github.com/anthropics/claude-code/issues/88163) | Completely incorrect about "you are doing security" | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:macos |
| [#88162](https://github.com/anthropics/claude-code/issues/88162) | \[Bug\] Anthropic API: Claude 3.5 Opus high hallucination rate in code generation | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:macos |
| [#88161](https://github.com/anthropics/claude-code/issues/88161) | You've hit your session limit · resets 4:20pm (Asia/Calcutta) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:cost, bug, platform:macos |
| [#88160](https://github.com/anthropics/claude-code/issues/88160) | \[FEATURE\] Peer-requested context reset: let one session hand a collaborator a clean context and a continuation prompt | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:agents, area:core, enhancement |
| [#88159](https://github.com/anthropics/claude-code/issues/88159) | \[Bug\] False positive crash detection during debugging session | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, bug, needs-repro, platform:macos |
| [#88158](https://github.com/anthropics/claude-code/issues/88158) | \[Bug\] MCP update\_document patch mode silently drops content after checkbox lists | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, data-loss, has repro, platform:windows |
| [#88157](https://github.com/anthropics/claude-code/issues/88157) | Add one-click/keyboard-shortcut archive for chat sessions | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:ui, enhancement |
| [#88156](https://github.com/anthropics/claude-code/issues/88156) | \[Bug\] False positive reasoning\_extraction error detection | CLOSED / COMPLETED | observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:core, bug, needs-repro, platform:windows |
| [#88154](https://github.com/anthropics/claude-code/issues/88154) | \[BUG\] Microsoft Dataverse MCP connector fails with "missing required resultType" on every call in Claude Code (works fine in claude.ai chat) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:mcp, bug, platform:vscode, platform:windows |
| [#88153](https://github.com/anthropics/claude-code/issues/88153) | \[Bug\] Fable 5 false positive on OSS decompilation analysis in code review context | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:macos |
| [#88152](https://github.com/anthropics/claude-code/issues/88152) | \[Bug\] Anthropic API Error: Request flagged incorrectly with "cyber" keyword | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:linux |
| [#88151](https://github.com/anthropics/claude-code/issues/88151) | \[Bug\] Claude Security Plugin Scan Results Not Processed Correctly | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:plugins, bug, needs-info, platform:macos, platform:vscode |
| [#88150](https://github.com/anthropics/claude-code/issues/88150) | Windows desktop app: repeated crash mid-session + Windows 'Repair' fails to fix it | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:windows |
| [#88149](https://github.com/anthropics/claude-code/issues/88149) | \[BUG\] @-mention file picker cannot descend into directory whose name contains a space — child files never suggested | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |

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
