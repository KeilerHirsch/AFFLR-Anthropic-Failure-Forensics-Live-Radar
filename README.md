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
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#75607](https://github.com/anthropics/claude-code/issues/75607) | \[BUG\] Server-side experiment (\`x-cc-atis\`) silently removed Opus 4.8 thinking summaries, and the CLI silently self-updated even with \`autoUpdates: false\`. No notice, no opt-in, settings silently overridden. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-08 | api:anthropic, area:core, area:model, bug, has repro, platform:linux, platform:vscode |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#68316](https://github.com/anthropics/claude-code/issues/68316) | \[BUG\] macOS version of Claude Desktop becomes corrupted, freezes, requiring full Reset App before it will work again | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-13 | area:desktop, bug, has repro, platform:macos, stale |
| [#79535](https://github.com/anthropics/claude-code/issues/79535) | \[BUG\] Repeated OAuth 401 "revoked" storms in Desktop app — regression 2.1.209 → 2.1.215 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:auth, area:desktop, bug, platform:macos, regression, stale |
| [#79505](https://github.com/anthropics/claude-code/issues/79505) | MCP OAuth: no per-server "clear authentication", and no re-registration when a cached DCR client is rejected | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:auth, area:mcp, bug, platform:macos, stale |
| [#78658](https://github.com/anthropics/claude-code/issues/78658) | Model behavior: Sonnet 5 recommended a security control with no enforcement value, despite explicit safety-critical project context (session evidence + transcript line included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#79528](https://github.com/anthropics/claude-code/issues/79528) | \[Bug\] Safety classifier false-positives on legitimate SRE/DevOps operations, forcing model downgrade | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:model, bug, duplicate, platform:macos, stale |
| [#79265](https://github.com/anthropics/claude-code/issues/79265) | Opus 4.8 fabricated attached-PDF content, embedding an unlabeled prompt-injection payload (fake exfil URL + concealment instruction) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:mcp, area:model, area:security, bug, platform:windows, stale |
| [#79182](https://github.com/anthropics/claude-code/issues/79182) | \[Bug\] Fable 5 safeguards falsely triggering on authorized defensive security work, causing mid-session model downgrades | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-19 | area:model, bug, platform:windows, stale |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, stale |
| [#78530](https://github.com/anthropics/claude-code/issues/78530) | Model executes a destructive persistent state change (deletes OS-level saved settings) inferred from a goal-level instruction — no confirmation, no backup, Nth same-session recurrence | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:permissions, bug, platform:windows, stale |
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#88262](https://github.com/anthropics/claude-code/issues/88262) | \[MODEL\] Opus suggested that shell mode in claude-code was not in chat context | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, bug, model |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
| [#75607](https://github.com/anthropics/claude-code/issues/75607) | \[BUG\] Server-side experiment (\`x-cc-atis\`) silently removed Opus 4.8 thinking summaries, and the CLI silently self-updated even with \`autoUpdates: false\`. No notice, no opt-in, settings silently overridden. | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-08 | api:anthropic, area:core, area:model, bug, has repro, platform:linux, platform:vscode |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#68316](https://github.com/anthropics/claude-code/issues/68316) | \[BUG\] macOS version of Claude Desktop becomes corrupted, freezes, requiring full Reset App before it will work again | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-13 | area:desktop, bug, has repro, platform:macos, stale |
| [#79535](https://github.com/anthropics/claude-code/issues/79535) | \[BUG\] Repeated OAuth 401 "revoked" storms in Desktop app — regression 2.1.209 → 2.1.215 | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:auth, area:desktop, bug, platform:macos, regression, stale |
| [#79505](https://github.com/anthropics/claude-code/issues/79505) | MCP OAuth: no per-server "clear authentication", and no re-registration when a cached DCR client is rejected | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:auth, area:mcp, bug, platform:macos, stale |
| [#78658](https://github.com/anthropics/claude-code/issues/78658) | Model behavior: Sonnet 5 recommended a security control with no enforcement value, despite explicit safety-critical project context (session evidence + transcript line included) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:model, bug, stale |
| [#69381](https://github.com/anthropics/claude-code/issues/69381) | Bug Report: Claude Code Agent Fabricates Code, Ignores APIs, Wastes Tokens | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-18 | area:tools, bug, model, platform:windows, stale |
| [#79528](https://github.com/anthropics/claude-code/issues/79528) | \[Bug\] Safety classifier false-positives on legitimate SRE/DevOps operations, forcing model downgrade | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:model, bug, duplicate, platform:macos, stale |
| [#79265](https://github.com/anthropics/claude-code/issues/79265) | Opus 4.8 fabricated attached-PDF content, embedding an unlabeled prompt-injection payload (fake exfil URL + concealment instruction) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-20 | area:mcp, area:model, area:security, bug, platform:windows, stale |
| [#79182](https://github.com/anthropics/claude-code/issues/79182) | \[Bug\] Fable 5 safeguards falsely triggering on authorized defensive security work, causing mid-session model downgrades | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-19 | area:model, bug, platform:windows, stale |
| [#78534](https://github.com/anthropics/claude-code/issues/78534) | \[BUG\] headersHelper on http transport still falls into "Incompatible auth server: does not support dynamic client registration" on 2.1.211 (regression from #53267 persists) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:auth, area:mcp, bug, has repro, platform:windows, regression, stale |
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |
| [#78527](https://github.com/anthropics/claude-code/issues/78527) | \[BUG\] v2.1.210 regression: PreToolUse prompt-hook deny stops the entire turn (hook\_stopped\_continuation) instead of returning a tool error | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-17 | area:hooks, bug, has repro, platform:macos, regression, reproduced |
| [#69044](https://github.com/anthropics/claude-code/issues/69044) | User feedback: Recurring errors documented over months of daily Claude Code use | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-17 | area:model, bug |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88423](https://github.com/anthropics/claude-code/issues/88423) | In-process subagents are never re-invoked when their own run\_in\_background Bash / Monitor task completes | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, bug, has repro, platform:linux |
| [#88422](https://github.com/anthropics/claude-code/issues/88422) | \[Bug\] API Error: Fable 5's safeguards flagged this message | OPEN | observation / provenance integrity | 2026-08-21 | 2026-08-21 | bug, needs-info, platform:macos |
| [#88421](https://github.com/anthropics/claude-code/issues/88421) | \[Bug\] Anthropic API Error: Invalid tool\_use\_id in advisor\_tool\_result after session compaction | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:core, bug, duplicate, platform:windows |
| [#88420](https://github.com/anthropics/claude-code/issues/88420) | \[Bug\] Memory/Context not persisting user profile updates across sessions | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | bug, memory, platform:macos |
| [#88418](https://github.com/anthropics/claude-code/issues/88418) | \`.claude.json\` stores one project directory under up to three different path spellings, splitting trust, MCP servers, and worktree state across them | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:core, area:mcp, area:security, bug, has repro, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88417](https://github.com/anthropics/claude-code/issues/88417) | \[BUG\] \`protocol mismatch\` error when trying to install Claude CLI | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:installation, bug, platform:linux |
| [#88416](https://github.com/anthropics/claude-code/issues/88416) | Benign coding work was stopped by reasoning\_extraction; drafting a follow-up comment to report that event was then refused as cyber | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:vscode |
| [#88415](https://github.com/anthropics/claude-code/issues/88415) | Desktop app dies silently after GPU process crash (exitCode 101457950) when a Browser-pane page requests a WebGPU adapter - Windows 11 / AMD APU | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, bug, platform:windows |
| [#88414](https://github.com/anthropics/claude-code/issues/88414) | Remote Control session goes permanently unresponsive (process alive, no crash) after a Bash tool call times out; mobile app shows it as unrecoverable 'Disconnected' | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:core, bug, has repro, platform:ios, platform:macos |
| [#88413](https://github.com/anthropics/claude-code/issues/88413) | \[BUG\] \[BUG\] Claude in Chrome 1.0.85 + Chrome 151 (Windows): all clicks/keystrokes silently dropped — "Debugger is not attached to the tab with id" on every input dispatch | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:browser-extension, area:chrome, bug, has repro, platform:windows |
| [#88412](https://github.com/anthropics/claude-code/issues/88412) | \[BUG\] Waking an idle agent fork (\`subagent\_type: "fork"\`) forfeits its inherited prompt cache on every wake — \`messages\_changed\`, \`cache\_read\` pinned to a fixed boundary, not TTL | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:agents, area:cost, bug, has repro, platform:linux |
| [#88410](https://github.com/anthropics/claude-code/issues/88410) | \[BUG\] 사용자 동의/명령 없이 초반 대화 구간이 유실됨 | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | bug, data-loss, needs-info, platform:macos |
| [#88409](https://github.com/anthropics/claude-code/issues/88409) | Desktop: session group names sync across devices via account, sessions don't — no opt-out (privacy concern for isolated work/personal machines) | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:desktop, enhancement, platform:windows |
| [#88408](https://github.com/anthropics/claude-code/issues/88408) | \[BUG\] Native scheduled tasks fire immediately on resume after external restart (catch-up fires), ignoring the configured cadence | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:core, bug, has repro, platform:windows |
| [#88407](https://github.com/anthropics/claude-code/issues/88407) | \[Bug\] Anthropic API Error: Reasoning extraction access restriction | OPEN | observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, duplicate, platform:vscode, platform:windows |
| [#88406](https://github.com/anthropics/claude-code/issues/88406) | \[Bug\] Cache eviction triggered during active nested subagent execution | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:core, area:tui, bug, platform:windows |
| [#88405](https://github.com/anthropics/claude-code/issues/88405) | Symlinked files in .claude/rules/ are not auto-loaded (contradicts docs) | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-20 | area:core, bug, has repro |
| [#88404](https://github.com/anthropics/claude-code/issues/88404) | Remote Control: expose the ~/.claude.json project registry as a picker in the session list | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | enhancement, platform:windows |
| [#88403](https://github.com/anthropics/claude-code/issues/88403) | \[FEATURE\] Slack MCP: implement the claude/channel capability so Slack activity can drive turns | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:mcp, area:plugins, enhancement |
| [#88402](https://github.com/anthropics/claude-code/issues/88402) | find shell wrapper doesn't skip hidden/gitignored paths like grep/rg do — traverses Claude's own .claude/worktrees/ | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:bash, bug, has repro |
| [#88401](https://github.com/anthropics/claude-code/issues/88401) | \[Feature Request\] Add built-in security vulnerability scanning tool for local product validation | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, area:security, enhancement, platform:windows |
| [#88400](https://github.com/anthropics/claude-code/issues/88400) | Skill auto-discovery is exactly one level deep, but the docs say "all SKILL.md files in skill subdirectories" — and a nested SKILL.md is ignored silently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:docs, area:plugins, area:skills, bug, has repro |
| [#88399](https://github.com/anthropics/claude-code/issues/88399) | \[Feature Request\] Display token count permanently in UI | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:statusline, enhancement, platform:macos |
| [#88398](https://github.com/anthropics/claude-code/issues/88398) | \[BUG\] design-sync truncation marker points to unshipped component docs | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:skills, bug, has repro |
| [#88397](https://github.com/anthropics/claude-code/issues/88397) | Subagent results never returned to the main conversation (Agent tool); result unrecoverable | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, bug, platform:wsl |

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
