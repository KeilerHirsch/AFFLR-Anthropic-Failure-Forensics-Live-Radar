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
| [#78671](https://github.com/anthropics/claude-code/issues/78671) | \[BUG\] Cloud Cowork sessions provisioned without remote-devices MCP despite authenticated device bridge — signCreateSessionBind not\_registered, silent unbound fallback | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:cowork, bug, has repro, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
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
| [#78530](https://github.com/anthropics/claude-code/issues/78530) | Model executes a destructive persistent state change (deletes OS-level saved settings) inferred from a goal-level instruction — no confirmation, no backup, Nth same-session recurrence | OPEN | security / trust boundary · high-signal label | 2026-08-20 | 2026-07-17 | area:model, area:permissions, bug, platform:windows, stale |
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |

</details>

### 🔬 Evidence / provenance / integrity signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#78671](https://github.com/anthropics/claude-code/issues/78671) | \[BUG\] Cloud Cowork sessions provisioned without remote-devices MCP despite authenticated device bridge — signCreateSessionBind not\_registered, silent unbound fallback | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-07-17 | area:cowork, bug, has repro, platform:linux |
| [#44778](https://github.com/anthropics/claude-code/issues/44778) | \[Bug\] System events delivered as user-role messages cause model to fabricate user consent and act on it | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-04-07 | area:agents, area:core, area:security, bug, has repro |
| [#87591](https://github.com/anthropics/claude-code/issues/87591) | Model fabricates user approval in its own turn, then executes a send tool in the same turn | CLOSED / DUPLICATE | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-18 | area:model, area:permissions, area:security, bug, has repro, platform:macos |
| [#87833](https://github.com/anthropics/claude-code/issues/87833) | Starting a session in Claude Desktop revokes filesystem access from already-running CLI sessions (macOS TCC identity collision) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-19 | area:desktop, area:security, bug, has repro, platform:macos |
| [#67246](https://github.com/anthropics/claude-code/issues/67246) | Safety-classifier model switch (Fable 5 → Opus 4.8) fires on benign content and can't be overridden with /model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-06-10 | area:model, bug, platform:macos |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#86012](https://github.com/anthropics/claude-code/issues/86012) | Cross-session messages leave the recipient's query completely unresponsive (hadFirstResponse=false, reason=no\_response) until Desktop's own idle-timeout force-kills it 15-20 min later | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-12 | area:agent-view, area:desktop, area:mcp, bug, has repro, platform:macos, platform:windows, regression |
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
| [#78140](https://github.com/anthropics/claude-code/issues/78140) | Claude Code: fabricates constraints requiring human action, unloads automatable work onto the user, and builds unauthorized governance — recurring after correction | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-16 | area:model, bug, platform:windows, stale |
| [#67730](https://github.com/anthropics/claude-code/issues/67730) | Subagents return fully hallucinated results with zero tool calls; leaked tool-call XML in text; two fabricated 'prompt injection detected' reports | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-06-12 | area:agents, area:model, bug, platform:macos, stale |
| [#76861](https://github.com/anthropics/claude-code/issues/76861) | \[Bug\] Input safeguard over-flags authorized red-teaming work, forcing fallback to Opus model | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-12 | area:model, bug, platform:linux, stale |
| [#76248](https://github.com/anthropics/claude-code/issues/76248) | \[BUG\] Cloud/Cowork sessions: git proxy now blocks all pushes — "not in this session's authorized repository set"; PAT pass-through no longer works (CCR\_TEST\_GITPROXY rollout?) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-20 | 2026-07-10 | area:cowork, bug, has repro, reproduced |
| [#83795](https://github.com/anthropics/claude-code/issues/83795) | \[SECURITY/ARCHITECTURE\] Model pinning via settings.json is silently overridden — 4 measured bypass vectors + documented fallback substitution, Gen-4 models removed from the model menu | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-04 | model |
| [#83510](https://github.com/anthropics/claude-code/issues/83510) | \[MODEL\] Measurable quality regression in Claude generation 5 (Fable 5 / Opus 5 / Sonnet 5): worse nonsense detection, ~2x verbosity, under-disclosed model fallback (Fable 5 → Opus 4.8) — reproducible measurements | OPEN | security / trust boundary · observation / provenance integrity · related context | 2026-08-16 | 2026-08-03 | — |
| [#85937](https://github.com/anthropics/claude-code/issues/85937) | \[Billing\]\[Bug\] Two Individual-plan auto-recharges completed (USD 99.08); Auto-reload off at post-charge capture | OPEN | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-11 | area:cost, bug, platform:macos |

</details>

### 🚨 Fresh critical signals

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88487](https://github.com/anthropics/claude-code/issues/88487) | Desktop app update wipes \`claudeAiOauth\` from .credentials.json, silently logging out Claude Code and killing Remote Control sessions (Windows) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, has repro, platform:windows |
| [#88485](https://github.com/anthropics/claude-code/issues/88485) | Auto-mode safety classifier blocks user's own credentials for their own accounts (local menu bar app setup) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |
| [#88484](https://github.com/anthropics/claude-code/issues/88484) | claude.ai connectors and local stdio servers yield zero tools at session start (desktop); only a manual connector re-toggle — which uses a different registration path (UUID vs display-name) — makes them appear | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, bug, has repro, platform:windows |
| [#88483](https://github.com/anthropics/claude-code/issues/88483) | \[BUG\] Desktop app never rebuilds its deferred-tool pool: tools/list\_changed and RefreshMcpTools are both no-ops (CLI 2.1.237 works with the identical server — carve-out from #66084) | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:desktop, area:mcp, bug, has repro, platform:windows |
| [#88482](https://github.com/anthropics/claude-code/issues/88482) | I'd be happy to help, but I need more information to generate a proper GitHub issue title. Could you please provide:  1. \*\*What error or unexpected behavior are you experiencing?\*\* (e.g., crash, wrong output, API error message) 2. \*\*What is the exact error | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | bug, needs-info, platform:windows |

<details>
<summary>Show remaining 20</summary>

| Issue | Title | State | Signal | Updated | Created | Labels |
|---:|---|---|---|---|---|---|
| [#88481](https://github.com/anthropics/claude-code/issues/88481) | \[BUG\] Claude Code launched via wsl.exe-relayed WSL terminal triggers Windows kernel BSOD (0x1A/0x4477) — safe via SSH-remote WSL session | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | bug, external, has repro, platform:windows, platform:wsl |
| [#88479](https://github.com/anthropics/claude-code/issues/88479) | \[FEATURE\] Viewer analytics for Artifacts: views, unique viewers, last-viewed (and expose to the agent) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | invalid |
| [#88478](https://github.com/anthropics/claude-code/issues/88478) | iOS Simulator panel crash-loops on attach: SIGABRT in CoreImage/Metal on the FBSimulatorControl BitmapStream thread | CLOSED / NOT\_PLANNED | security / trust boundary · observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:desktop, duplicate, platform:macos |
| [#88477](https://github.com/anthropics/claude-code/issues/88477) | \[BUG\] Login verification emails never delivered (ESP suppression list?) — fully locked out of Claude Code on Max plan, recurring issue | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:auth, bug, external, platform:windows |
| [#88476](https://github.com/anthropics/claude-code/issues/88476) | Archive/delete of Claude Code sessions is per-client — desktop's archive flag is invisible to the VS Code extension | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:cli, area:desktop, area:vscode, enhancement, platform:windows |
| [#88475](https://github.com/anthropics/claude-code/issues/88475) | bypass permissions mode steers agents off Read/Edit/Grep onto composed shell strings, reintroducing quoting and exit-code failures that the structured tools cannot have | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:bash, area:core, area:permissions, bug, has repro, platform:linux |
| [#88474](https://github.com/anthropics/claude-code/issues/88474) | \[MODEL\] Typos in Korean audio text during video generation caused wasted Higgsfield credits | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:mcp, area:model, bug, model |
| [#88473](https://github.com/anthropics/claude-code/issues/88473) | VS Code extension: AskUserQuestion picker steals keyboard focus on mount even when its chat tab is hidden (mount-focus lacks the document.hasFocus gate the 500ms step has) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:permissions, bug, platform:vscode, platform:windows |
| [#88472](https://github.com/anthropics/claude-code/issues/88472) | \[MODEL\] Quite hard when you are working with a pentester because safeguards are always thrown while you just want to give him information or this kind of things when you want to make a plan | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | api:anthropic, area:model, bug, model, needs-repro |
| [#88471](https://github.com/anthropics/claude-code/issues/88471) | \[FEATURE\] Allow \`preview\` on \`multiSelect\` AskUserQuestion questions | OPEN | observation / provenance integrity | 2026-08-21 | 2026-08-21 | area:tui, enhancement |
| [#88470](https://github.com/anthropics/claude-code/issues/88470) | Claude Code reads files matching a user CLAUDE.md 'never read' instruction | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, area:security, bug, platform:vscode |
| [#88469](https://github.com/anthropics/claude-code/issues/88469) | Claude Code repeatedly fails to apply its own persisted rules, and allocates effort away from the user's stated goal | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:agents, bug, memory, platform:linux |
| [#88468](https://github.com/anthropics/claude-code/issues/88468) | \[BUG\] JetBrains plugin: diff approval doesn't register when the diff is empty (Write/Edit falsely reported as rejected) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:ide, bug, platform:intellij, platform:macos |
| [#88467](https://github.com/anthropics/claude-code/issues/88467) | very undependable; unpredictable; losing confidence; new models are deteriorating | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, model, platform:vscode |
| [#88466](https://github.com/anthropics/claude-code/issues/88466) | Auto-resume-at-reset checkbox is checked but session doesn't actually resume - requires manually selecting the session | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:tui, bug |
| [#88465](https://github.com/anthropics/claude-code/issues/88465) | VS Code extension: agent file-read preview tabs (✻ \[Claude Code\]) steal keyboard focus from the tab the user is typing in | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:ide, bug, platform:vscode, platform:windows |
| [#88464](https://github.com/anthropics/claude-code/issues/88464) | \[BUG\]Unexpected text generation regarding prompt injection / jailbreaking | OPEN | security / trust boundary · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug |
| [#88463](https://github.com/anthropics/claude-code/issues/88463) | Artifact publish auto-arms a background "live updates" monitor with no opt-out | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:tools, enhancement |
| [#88462](https://github.com/anthropics/claude-code/issues/88462) | \[Data Loss\] Claude Code ran rm -rf on $HOME in auto mode — destructive code hidden inside a script the assistant wrote itself (5th report of this class) | OPEN | security / trust boundary | 2026-08-21 | 2026-08-21 | area:permissions, area:sandbox, bug, data-loss, high-priority, platform:wsl |
| [#88461](https://github.com/anthropics/claude-code/issues/88461) | \[Bug\] Anthropic API Error: False Positive Security Filter on Legitimate Encryption Operations | OPEN | security / trust boundary · observation / provenance integrity · high-signal label | 2026-08-21 | 2026-08-21 | area:model, bug, platform:macos |

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
