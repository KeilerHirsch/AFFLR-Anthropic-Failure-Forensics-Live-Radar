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
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88425](https://github.com/anthropics/claude-code/issues/88425) | \[BUG\] False positive: \[bio\] safeguard fires on base64 file-comparison work, then hard-blocks the conversation (request IDs included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:desktop, area:model, bug, platform:windows |
| [#75607](https://github.com/anthropics/claude-code/issues/75607) | \[BUG\] Server-side experiment (\`x-cc-atis\`) silently removed Opus 4.8 thinking summaries, and the CLI silently self-updated even with \`autoUpdates: false\`. No notice, no opt-in, settings silently overridden. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-08 | api:anthropic, area:core, area:model, bug, has repro, platform:linux, platform:vscode |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#68316](https://github.com/anthropics/claude-code/issues/68316) | \[BUG\] macOS version of Claude Desktop becomes corrupted, freezes, requiring full Reset App before it will work again | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-13 | area:desktop, bug, has repro, platform:macos, stale |
| [#78658](https://github.com/anthropics/claude-code/issues/78658) | Model behavior: Sonnet 5 recommended a security control with no enforcement value, despite explicit safety-critical project context (session evidence + transcript line included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#79528](https://github.com/anthropics/claude-code/issues/79528) | \[Bug\] Safety classifier false-positives on legitimate SRE/DevOps operations, forcing model downgrade | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:model, bug, duplicate, platform:macos, stale |
| [#79265](https://github.com/anthropics/claude-code/issues/79265) | Opus 4.8 fabricated attached-PDF content, embedding an unlabeled prompt-injection payload (fake exfil URL + concealment instruction) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:mcp, area:model, area:security, bug, platform:windows, stale |
| [#79182](https://github.com/anthropics/claude-code/issues/79182) | \[Bug\] Fable 5 safeguards falsely triggering on authorized defensive security work, causing mid-session model downgrades | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-19 | area:model, bug, platform:windows, stale |
| [#78530](https://github.com/anthropics/claude-code/issues/78530) | Model executes a destructive persistent state change (deletes OS-level saved settings) inferred from a goal-level instruction — no confirmation, no backup, Nth same-session recurrence | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:permissions, bug, platform:windows, stale |
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88425](https://github.com/anthropics/claude-code/issues/88425) | \[BUG\] False positive: \[bio\] safeguard fires on base64 file-comparison work, then hard-blocks the conversation (request IDs included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:desktop, area:model, bug, platform:windows |
| [#75607](https://github.com/anthropics/claude-code/issues/75607) | \[BUG\] Server-side experiment (\`x-cc-atis\`) silently removed Opus 4.8 thinking summaries, and the CLI silently self-updated even with \`autoUpdates: false\`. No notice, no opt-in, settings silently overridden. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-08 | api:anthropic, area:core, area:model, bug, has repro, platform:linux, platform:vscode |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#68316](https://github.com/anthropics/claude-code/issues/68316) | \[BUG\] macOS version of Claude Desktop becomes corrupted, freezes, requiring full Reset App before it will work again | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-13 | area:desktop, bug, has repro, platform:macos, stale |
| [#78658](https://github.com/anthropics/claude-code/issues/78658) | Model behavior: Sonnet 5 recommended a security control with no enforcement value, despite explicit safety-critical project context (session evidence + transcript line included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#79528](https://github.com/anthropics/claude-code/issues/79528) | \[Bug\] Safety classifier false-positives on legitimate SRE/DevOps operations, forcing model downgrade | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:model, bug, duplicate, platform:macos, stale |
| [#79265](https://github.com/anthropics/claude-code/issues/79265) | Opus 4.8 fabricated attached-PDF content, embedding an unlabeled prompt-injection payload (fake exfil URL + concealment instruction) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:mcp, area:model, area:security, bug, platform:windows, stale |
| [#79182](https://github.com/anthropics/claude-code/issues/79182) | \[Bug\] Fable 5 safeguards falsely triggering on authorized defensive security work, causing mid-session model downgrades | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-19 | area:model, bug, platform:windows, stale |
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88459](https://github.com/anthropics/claude-code/issues/88459) | \[BUG\] Background subagent narrates fabricated "live progress" from stale build artifacts instead of a real running process | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:model, bug, platform:windows |
| [#88458](https://github.com/anthropics/claude-code/issues/88458) | \[Bug\] Anthropic API Error: Fable 5 safeguards incorrectly flagged legitimate design documentation | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, duplicate, platform:macos |
| [#88456](https://github.com/anthropics/claude-code/issues/88456) | \[Bug\] Anthropic API Error: Content Policy Violation on Safe Inputs with Claude 3.5 Sonnet | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, duplicate, platform:windows |
| [#88455](https://github.com/anthropics/claude-code/issues/88455) | \[Feature Request\] Add learning plan generation capability | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, needs-repro, platform:windows |
| [#88454](https://github.com/anthropics/claude-code/issues/88454) | \[Bug\] Increased false positive flagging in MCP Server development workflows | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:mcp, area:model, bug, platform:vscode, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88453](https://github.com/anthropics/claude-code/issues/88453) | \[BUG\] A \`context: fork\` skill silently loses the Agent tool when backgrounded, with no generic signal that it happened | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:skills, bug |
| [#88451](https://github.com/anthropics/claude-code/issues/88451) | \[Bug\] Non-streaming retry receives event-stream response instead of JSON (HTTP 200) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:api, area:networking, duplicate, platform:windows |
| [#88450](https://github.com/anthropics/claude-code/issues/88450) | /auto-mode-setup fails: removeFromPermissionsAllow\[0\] is not a rule string the removal offer could have produced | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cli, area:permissions, bug, duplicate, platform:linux |
| [#88449](https://github.com/anthropics/claude-code/issues/88449) | \[FEATURE\] Make “N shells, N monitors still running” a Clickable Dropdown with Summaries | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:tui, enhancement |
| [#88448](https://github.com/anthropics/claude-code/issues/88448) | \[Bug\] API Error: Safeguards falsely flag normal message with \`reasoning\_extraction\` | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, duplicate, platform:windows |
| [#88447](https://github.com/anthropics/claude-code/issues/88447) | Archive folder in FleetView shows empty/unclickable session list despite archived sessions existing | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:agent-view, area:ui, bug, has repro |
| [#88446](https://github.com/anthropics/claude-code/issues/88446) | \[BUG\] \`/compact\` not working in the  newly updated Visual Studio Code extension (v2.1.238) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:ide, bug, platform:linux, platform:vscode, regression |
| [#88445](https://github.com/anthropics/claude-code/issues/88445) | \[BUG\] Auto interaction between 2 Claude Code Desktop sessions | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, platform:windows |
| [#88444](https://github.com/anthropics/claude-code/issues/88444) | \[BUG\] Resuming a fork forfeits its prompt cache: deterministic miss after any tool loop, fork 5m vs parent 1h TTL, full-context rewrites while the prefix is live | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:agents, area:core, area:cost, bug, has repro, platform:linux |
| [#88443](https://github.com/anthropics/claude-code/issues/88443) | \[BUG\] Claude Desktop main app process never launches — CreateProcess ERROR\_INVALID\_PARAMETER (87), same packaged-activation defect as #86140 but hitting the primary exe, not just Cowork | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | invalid |
| [#88441](https://github.com/anthropics/claude-code/issues/88441) | \[BUG\] User settings.json PreToolUse hooks never fire for Bash calls inside Task-spawned subagents | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:agents, area:hooks, bug, duplicate |
| [#88440](https://github.com/anthropics/claude-code/issues/88440) | \[Bug\] Fork command uses parent session's cwd instead of current working directory | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:cli, bug, has repro, platform:macos |
| [#88439](https://github.com/anthropics/claude-code/issues/88439) | \[MODEL\] Claude speaks broken Japanese | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, model, platform:aws-bedrock |
| [#88437](https://github.com/anthropics/claude-code/issues/88437) | Built-in skills: 3 content defects (security-review, keybindings-help, update-config) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:skills, bug |
| [#88436](https://github.com/anthropics/claude-code/issues/88436) | \[BUG\] Plan Mode Side Panel Won't Open | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug, platform:macos |
| [#88435](https://github.com/anthropics/claude-code/issues/88435) | ToolSearch: the \`+term\` prefix matches descriptions too, so it does not "require the term in the name" | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:tools, bug, has repro |
| [#88434](https://github.com/anthropics/claude-code/issues/88434) | --print returns "Not logged in" when $USER is absent/wrong: keychain OAuth lookup keys on $USER with no uid fallback (macOS) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:macos |
| [#88433](https://github.com/anthropics/claude-code/issues/88433) | \[Bug\] Anthropic API Error: False Positive Detection | OPEN | observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, needs-info, platform:macos, platform:vscode |
| [#88432](https://github.com/anthropics/claude-code/issues/88432) | \[BUG\] Desktop (Windows/WSL): detached window's slash menu lists only bundled skills | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:bedrock, area:desktop, area:skills, bug, has repro, platform:windows, platform:wsl |
| [#88431](https://github.com/anthropics/claude-code/issues/88431) | \[BUG\] Cowork Dispatch entry never renders in macOS sidebar (Max) — setup unreachable, mobile pairing fails | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:cowork, area:desktop, bug, platform:macos |

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
