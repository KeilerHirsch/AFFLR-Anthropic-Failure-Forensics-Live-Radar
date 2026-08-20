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
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
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
| [#77168](https://github.com/anthropics/claude-code/issues/77168) | \[BUG\] auth\_denied event with reason invalid\_token when client posts to App Gateway /v1/metrics endpoint | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | api:bedrock, area:auth, bug, regression, stale |
| [#73861](https://github.com/anthropics/claude-code/issues/73861) | \[BUG\] /login reports "Login successful" but credentials are never written to macOS Keychain (v2.1.199) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-03 | area:auth, bug, platform:macos, stale |
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
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#73083](https://github.com/anthropics/claude-code/issues/73083) | \[Bug\]\[cyber\] Safety filter blocked a legitimate request to audit and harden own website security (req\_011CccNmQvSEeR2z4FsxBTyp) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73058](https://github.com/anthropics/claude-code/issues/73058) | \[Bug\]\[cyber\] Safety filter blocked capturing undocumented flight-control opcodes over device link (req\_011CccKQww4Ww9U6zj1HkA22) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73060](https://github.com/anthropics/claude-code/issues/73060) | \[Bug\]\[cyber\] ClAudit false-positive in GlassFalcon — req\_011CccKSJbYtX1BPrLwEhucM | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |
| [#73057](https://github.com/anthropics/claude-code/issues/73057) | \[Bug\]\[cyber\] Safeguard blocked authorized adversarial security review of own web app (req\_011CccKEuYAYEFLEtJo1Vn4L) | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-02 | area:model, area:security, bug, duplicate, platform:linux, stale |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
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
| [#77168](https://github.com/anthropics/claude-code/issues/77168) | \[BUG\] auth\_denied event with reason invalid\_token when client posts to App Gateway /v1/metrics endpoint | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-13 | api:bedrock, area:auth, bug, regression, stale |
| [#73861](https://github.com/anthropics/claude-code/issues/73861) | \[BUG\] /login reports "Login successful" but credentials are never written to macOS Keychain (v2.1.199) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-03 | area:auth, bug, platform:macos, stale |
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
| [#88396](https://github.com/anthropics/claude-code/issues/88396) | \[Bug\] Safety guardrails incorrectly triggered during API testing workflow | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, needs-repro, platform:macos |
| [#88395](https://github.com/anthropics/claude-code/issues/88395) | Claude in Chrome never connects when Claude Desktop is installed (extension keeps the first native host that pongs; Desktop helper pongs while the app is closed) | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:browser-extension, area:chrome, bug, has repro, platform:macos |
| [#88393](https://github.com/anthropics/claude-code/issues/88393) | \[Bug\] \`claude --continue\` silently resumes existing conversation without indication or live session detection | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:cli, area:core, bug, has repro, platform:macos |
| [#88392](https://github.com/anthropics/claude-code/issues/88392) | \[BUG\] MCP server reports hasTools: true on connect and a reference client confirms tools exist, but Claude Code's session gets zero — intermittently | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:mcp, bug, has repro, platform:linux |
| [#88391](https://github.com/anthropics/claude-code/issues/88391) | \[BUG\] Prompt suggestions silently stopped appearing in Claude Code Desktop (regression in 2.1.229) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos, regression |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88390](https://github.com/anthropics/claude-code/issues/88390) | \[Bug\] Session terminates on model rate limit instead of falling back to available model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:windows |
| [#88389](https://github.com/anthropics/claude-code/issues/88389) | \[Feature Request\] Add security audit capabilities for user applications | OPEN | security / trust boundary | 2026-08-20 | 2026-08-20 | area:security, duplicate, platform:linux |
| [#88388](https://github.com/anthropics/claude-code/issues/88388) | \[Bug\] Anthropic API Error: Content Flagged by Safeguards (Fable 5) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, duplicate, platform:macos |
| [#88384](https://github.com/anthropics/claude-code/issues/88384) | \[MODEL\]  Claude overwrote 5+ site pages without backup during an authorized emergency action, causing permanent data loss | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:tools, bug, data-loss, model |
| [#88381](https://github.com/anthropics/claude-code/issues/88381) | \[Bug\] Artifact version history shows stale cached versions and prevents deletion | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | bug, platform:macos |
| [#88379](https://github.com/anthropics/claude-code/issues/88379) | \[BUG\] Worktree isolation classifies \`git -C\` paths by leading character: refuses \`.\` and \`~\` inside the worktree, allows \`$VAR\` that escapes it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:sandbox, bug, has repro, platform:wsl |
| [#88378](https://github.com/anthropics/claude-code/issues/88378) | Background task notifications stay queued until the next user message in SDK streaming mode | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agent-sdk, bug, platform:linux |
| [#88377](https://github.com/anthropics/claude-code/issues/88377) | \[BUG\] Vim mode: after a paste, Shift+Enter intermittently submits instead of inserting a newline (Ghostty/macOS, stock keytab) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tui, bug, has repro, platform:macos |
| [#88358](https://github.com/anthropics/claude-code/issues/88358) | Windows: telegram plugin's stale-poller eviction never fires — \`ps -p &lt;pid&gt; -o args=\` is unsupported by Cygwin ps, failure swallowed, bot.pid overwritten anyway | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-08-20 | area:plugins, bug, has repro, platform:windows |
| [#88357](https://github.com/anthropics/claude-code/issues/88357) | SendMessage (cross-session/teammate) silently discards queued messages to a busy session: \`queue-operation: remove\` instead of \`dequeue\` | CLOSED / COMPLETED | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:agents, area:mcp, bug, platform:linux |
| [#88346](https://github.com/anthropics/claude-code/issues/88346) | \[BUG\] Task store files deleted without any Task tool call, ~5s after a teammate completes the highest-numbered task (2.1.234–2.1.237) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:tools, bug, data-loss, has repro, platform:linux |
| [#88340](https://github.com/anthropics/claude-code/issues/88340) | Efficiency friction: noisy nudge reminders, safety-hook false positives, no file:// support in browser tool | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:mcp, enhancement, platform:macos |
| [#88338](https://github.com/anthropics/claude-code/issues/88338) | PostToolUse rewrite collisions are last-registered-wins, not "last-write-wins" — and a clobbered redaction is silent | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, area:security, bug, has repro |
| [#88337](https://github.com/anthropics/claude-code/issues/88337) | \[FEATURE\] Desktop sidebar: indicate which projects have work running | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, area:ui, enhancement, platform:macos |
| [#88330](https://github.com/anthropics/claude-code/issues/88330) | Auto-mode classifier blocks its own fix: opaque, coarse-grained, and inconsistent across channels | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, enhancement |
| [#88328](https://github.com/anthropics/claude-code/issues/88328) | PermissionRequest hooks never fire in --print mode on 2.1.237, while a PreToolUse control in the same settings file does | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:hooks, area:permissions, bug, has repro, platform:windows |
| [#88323](https://github.com/anthropics/claude-code/issues/88323) | Claude Desktop (Windows MSIX) bricks itself — package flagged "Modified" after Code Integrity blocks vk\_swiftshader.dll | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-20 | 2026-08-20 | area:desktop, bug, platform:windows |
| [#88320](https://github.com/anthropics/claude-code/issues/88320) | Desktop app's GhRestClient burns the user's GitHub GraphQL rate limit: ~640 points per session focus, ~2,000 per turn start | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:desktop, bug, has repro, platform:macos |
| [#88318](https://github.com/anthropics/claude-code/issues/88318) | Severe instruction-following degradation: unrequested git commit/PR, ignored instructions, fabricated links — 6 weeks of dated transcript evidence | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:model, bug, platform:windows |
| [#88307](https://github.com/anthropics/claude-code/issues/88307) | \[BUG\] Daemon-hosted background worker deletes \`~/.claude/settings.json\` when it is a symlink into a read-only directory (nix/home-manager) — all user settings silently lost | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-08-20 | area:agent-view, area:core, bug, data-loss, has repro, platform:linux |

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
