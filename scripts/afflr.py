# The Man, The Myth, The Legend : Keilerhirsch
from __future__ import annotations

import argparse
import html
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class RadarError(RuntimeError):
    """Raised when AFFLR cannot produce a complete, structurally validated snapshot."""


REACTION_KEYS = ("+1", "-1", "laugh", "hooray", "confused", "heart", "rocket", "eyes")
REACTION_EMOJI = {
    "+1": "👍", "-1": "👎", "laugh": "😄", "hooray": "🎉",
    "confused": "😕", "heart": "❤️", "rocket": "🚀", "eyes": "👀",
}

SECONDARY_VIEW_SORT = {
    "most-reacted": "reactions",
    "most-discussed": "comments",
    "recently-active": "updated",
}
SECONDARY_VIEW_TITLES = {
    "most-reacted": "Most reacted",
    "most-discussed": "Most discussed",
    "recently-active": "Recently active",
}
SECONDARY_VIEW_ORDER = ("most-reacted", "most-discussed", "recently-active")

PRIMARY_VIEW_TITLES = {
    "security-trust": "🛡️ Security & trust-boundary signals",
    "evidence-integrity": "🔬 Evidence / provenance / integrity signals",
    "fresh-critical": "🚨 Fresh critical signals",
}
PRIMARY_VIEW_ORDER = ("security-trust", "evidence-integrity", "fresh-critical")

# Stable context anchors for the current investigation. Inclusion is discovery
# metadata only; it is not an AFF evidence level or causal attribution.
RELATED_CONTEXT_NUMBERS = (83510, 83795, 86979, 87086)

# Targeted pools prevent high-value issues from disappearing merely because the
# repository produced >100 newer updates. Queries are deliberately broad and
# overlapping; results are normalized and deduplicated by issue number before
# ranking. These are discovery queries, not vulnerability classifications.
TARGETED_SEARCH_QUERIES = (
    "security OR credential OR permission OR sandbox OR injection OR unauthorized",
    '"data loss" OR deletion OR destructive OR rewind OR overwrite',
    "fabricated OR phantom OR monitor OR notification OR provenance OR integrity",
    "routing OR fallback OR pinning OR safeguard OR classifier OR benchmark OR eval",
    "token OR secret OR auth OR session OR privacy OR exfiltration",
)
TARGETED_POOL_LIMIT = 100
RECENT_POOL_LIMIT = 100

SEARCH_ENDPOINT = "https://api.github.com/search/issues"
ISSUE_ENDPOINT = "https://api.github.com/repos/anthropics/claude-code/issues"
SEARCH_SCOPE = "repo:anthropics/claude-code is:issue"
EXPECTED_ISSUE_PREFIX = "https://github.com/anthropics/claude-code/issues/"
TABLE_HEADER = "| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |"
TABLE_RULE = "|---:|---|---|---|---:|---:|---|---|---|"
PRIMARY_TABLE_HEADER = "| Issue | Title | State | Signal | Updated | Created | Labels |"
PRIMARY_TABLE_RULE = "|---:|---|---|---|---|---|---|"
README_START = "<!-- AFFLR-RADAR:START -->"
README_END = "<!-- AFFLR-RADAR:END -->"

SECURITY_TERMS = (
    "security", "credential", "credentials", "token", "secret", "permission",
    "permissions", "sandbox", "injection", "exfil", "unauthor", "authentication",
    "authorization", "auth", "session", "data loss", "delete", "deletion",
    "destructive", "rce", "path traversal", "privacy", "rewind", "overwrite",
)
INTEGRITY_TERMS = (
    "fabricat", "phantom", "hallucin", "monitor", "notification", "event",
    "provenance", "integrity", "routing", "rerout", "fallback", "pinning",
    "model switch", "model selector", "sticky model", "eval", "benchmark",
    "telemetry", "classifier", "safeguard", "false positive",
    "reasoning extraction", "observation",
)
HIGH_SIGNAL_LABELS = {
    "has repro", "security", "area:auth", "area:tools", "area:model", "area:api", "oncall",
}


@dataclass(frozen=True)
class IssueRecord:
    number: int
    title: str
    body: str
    url: str
    author: str
    state: str
    state_reason: str | None
    reactions_total: int
    reactions: tuple[tuple[str, int], ...]
    comments: int
    created_at: str
    updated_at: str
    labels: tuple[str, ...]


def _need(mapping: dict[str, Any], key: str) -> Any:
    if key not in mapping:
        raise RadarError(f"missing required field: {key}")
    return mapping[key]


def _iso(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise RadarError(f"invalid {field}")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise RadarError(f"invalid {field}: {value!r}") from exc
    return value


def normalize_issue(raw: dict[str, Any]) -> IssueRecord:
    user = _need(raw, "user")
    if not isinstance(user, dict) or not isinstance(user.get("login"), str):
        raise RadarError("invalid user.login")

    reactions = _need(raw, "reactions")
    if not isinstance(reactions, dict) or not isinstance(reactions.get("total_count"), int):
        raise RadarError("invalid reactions")

    labels_raw = _need(raw, "labels")
    if not isinstance(labels_raw, list):
        raise RadarError("invalid labels")
    labels: list[str] = []
    for label in labels_raw:
        if not isinstance(label, dict) or not isinstance(label.get("name"), str):
            raise RadarError("invalid label")
        labels.append(label["name"])

    reaction_pairs: list[tuple[str, int]] = []
    for key in REACTION_KEYS:
        value = reactions.get(key, 0)
        if not isinstance(value, int):
            raise RadarError(f"invalid reaction count: {key}")
        reaction_pairs.append((key, value))

    state_reason = raw.get("state_reason")
    if state_reason is not None and not isinstance(state_reason, str):
        raise RadarError("invalid state_reason")

    number = _need(raw, "number")
    comments = _need(raw, "comments")
    title = _need(raw, "title")
    url = _need(raw, "html_url")
    state = _need(raw, "state")
    body = raw.get("body") or ""

    if not isinstance(number, int) or not isinstance(comments, int):
        raise RadarError("invalid numeric issue metadata")
    if number <= 0 or comments < 0:
        raise RadarError("out-of-range numeric issue metadata")
    if not isinstance(title, str) or not isinstance(url, str) or not isinstance(state, str):
        raise RadarError("invalid string issue metadata")
    if not isinstance(body, str):
        raise RadarError("invalid issue body")
    if state not in {"open", "closed"}:
        raise RadarError(f"invalid issue state: {state!r}")

    expected_url = f"{EXPECTED_ISSUE_PREFIX}{number}"
    if url != expected_url:
        raise RadarError(f"unexpected issue URL: {url!r}")

    reactions_total = reactions["total_count"]
    if reactions_total < 0 or any(count < 0 for _, count in reaction_pairs):
        raise RadarError("negative reaction count")

    return IssueRecord(
        number=number, title=title, body=body, url=url, author=user["login"], state=state,
        state_reason=state_reason, reactions_total=reactions_total,
        reactions=tuple(reaction_pairs), comments=comments,
        created_at=_iso(_need(raw, "created_at"), "created_at"),
        updated_at=_iso(_need(raw, "updated_at"), "updated_at"),
        labels=tuple(sorted(labels, key=str.casefold)),
    )


def normalize_search_response(payload: dict[str, Any]) -> list[IssueRecord]:
    if payload.get("incomplete_results") is not False:
        raise RadarError("GitHub search returned incomplete results")
    items = payload.get("items")
    if not isinstance(items, list):
        raise RadarError("GitHub search response has no items list")
    return [normalize_issue(item) for item in items]


def _ts(value: str) -> float:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def _issue_text(issue: IssueRecord) -> str:
    return " ".join((issue.title, issue.body, *issue.labels)).casefold()


def _matches_any(issue: IssueRecord, terms: tuple[str, ...]) -> int:
    text = _issue_text(issue)
    return sum(1 for term in terms if term in text)


def classify_signals(issue: IssueRecord) -> tuple[str, ...]:
    signals: list[str] = []
    if _matches_any(issue, SECURITY_TERMS):
        signals.append("security / trust boundary")
    if _matches_any(issue, INTEGRITY_TERMS):
        signals.append("observation / provenance integrity")
    labels = {label.casefold() for label in issue.labels}
    if labels & HIGH_SIGNAL_LABELS:
        signals.append("high-signal label")
    if issue.number in RELATED_CONTEXT_NUMBERS:
        signals.append("related context")
    return tuple(signals)


def discovery_priority(issue: IssueRecord) -> tuple[int, int, int, float, int]:
    """Transparent discovery ordering; not a vulnerability or evidence score."""
    security_hits = _matches_any(issue, SECURITY_TERMS)
    integrity_hits = _matches_any(issue, INTEGRITY_TERMS)
    labels = {label.casefold() for label in issue.labels}
    return (
        min(security_hits + integrity_hits, 8),
        int(bool(labels & HIGH_SIGNAL_LABELS)),
        int(issue.number in RELATED_CONTEXT_NUMBERS),
        _ts(issue.updated_at),
        issue.number,
    )


def sort_secondary_view(view_name: str, issues: list[IssueRecord]) -> list[IssueRecord]:
    if view_name == "most-reacted":
        key = lambda issue: (issue.reactions_total, issue.comments, _ts(issue.updated_at), issue.number)
    elif view_name == "most-discussed":
        key = lambda issue: (issue.comments, issue.reactions_total, _ts(issue.updated_at), issue.number)
    elif view_name == "recently-active":
        key = lambda issue: (_ts(issue.updated_at), issue.reactions_total, issue.comments, issue.number)
    else:
        raise RadarError(f"unknown view: {view_name}")
    return sorted(issues, key=key, reverse=True)


def build_search_url(*, sort_name: str = "updated", per_page: int = 25, query: str | None = None) -> str:
    if per_page <= 0 or per_page > 100:
        raise RadarError("invalid GitHub search page size")
    q = SEARCH_SCOPE if not query else f"{SEARCH_SCOPE} {query}"
    params = {"q": q, "sort": sort_name, "order": "desc", "per_page": per_page}
    return f"{SEARCH_ENDPOINT}?{urlencode(params)}"


def build_issue_url(number: int) -> str:
    if number <= 0:
        raise RadarError("invalid issue number")
    return f"{ISSUE_ENDPOINT}/{number}"


def _merge_issues(*groups: list[IssueRecord]) -> list[IssueRecord]:
    by_number: dict[int, IssueRecord] = {}
    for group in groups:
        for issue in group:
            by_number[issue.number] = issue
    return list(by_number.values())


def collect_secondary_views(fetcher: Callable[[str], dict[str, Any]]) -> dict[str, list[IssueRecord]]:
    result: dict[str, list[IssueRecord]] = {}
    for name in SECONDARY_VIEW_ORDER:
        issues = normalize_search_response(
            fetcher(build_search_url(sort_name=SECONDARY_VIEW_SORT[name]))
        )
        if len(issues) > 25:
            raise RadarError(f"too many rows returned for {name}")
        result[name] = sort_secondary_view(name, issues)
    return result


def collect_targeted_pool(fetcher: Callable[[str], dict[str, Any]]) -> list[IssueRecord]:
    groups: list[list[IssueRecord]] = []
    for query in TARGETED_SEARCH_QUERIES:
        issues = normalize_search_response(
            fetcher(build_search_url(sort_name="updated", per_page=TARGETED_POOL_LIMIT, query=query))
        )
        if len(issues) > TARGETED_POOL_LIMIT:
            raise RadarError("too many rows returned for targeted discovery pool")
        groups.append(issues)
    return _merge_issues(*groups)


def collect_primary_views(fetcher: Callable[[str], dict[str, Any]]) -> dict[str, list[IssueRecord]]:
    recent = normalize_search_response(
        fetcher(build_search_url(sort_name="updated", per_page=RECENT_POOL_LIMIT))
    )
    if len(recent) > RECENT_POOL_LIMIT:
        raise RadarError("too many rows returned for primary discovery pool")

    targeted = collect_targeted_pool(fetcher)

    pinned: list[IssueRecord] = []
    for number in RELATED_CONTEXT_NUMBERS:
        pinned.append(normalize_issue(fetcher(build_issue_url(number))))

    pool = _merge_issues(recent, targeted, pinned)
    security = [issue for issue in pool if _matches_any(issue, SECURITY_TERMS)]
    integrity = [issue for issue in pool if _matches_any(issue, INTEGRITY_TERMS)]

    critical_numbers = {issue.number for issue in security + integrity}
    # Freshness is based on creation time, not membership in the generic recent
    # window, so a high-volume hour cannot hide a newly created targeted hit.
    fresh = [issue for issue in pool if issue.number in critical_numbers]

    security.sort(key=discovery_priority, reverse=True)
    integrity.sort(key=discovery_priority, reverse=True)
    fresh.sort(key=lambda issue: (_ts(issue.created_at), discovery_priority(issue)), reverse=True)
    return {
        "security-trust": security[:25],
        "evidence-integrity": integrity[:25],
        "fresh-critical": fresh[:25],
    }


def escape_cell(value: str) -> str:
    escaped = html.escape(value, quote=False).replace("\\", "\\\\")
    for char in ("|", "[", "]", "*", "_", "`"):
        escaped = escaped.replace(char, "\\" + char)
    return " ".join(escaped.splitlines())


def state_label(issue: IssueRecord) -> str:
    label = issue.state.upper()
    if issue.state_reason:
        label += " / " + issue.state_reason.upper()
    return label


def reaction_label(issue: IssueRecord) -> str:
    detail = " · ".join(
        f"{REACTION_EMOJI[key]} {count}" for key, count in issue.reactions if count
    )
    return str(issue.reactions_total) if not detail else f"{issue.reactions_total} ({detail})"


def signal_label(issue: IssueRecord) -> str:
    signals = classify_signals(issue)
    return " · ".join(signals) if signals else "discovery candidate"


def render_secondary_table_rows(issues: list[IssueRecord]) -> list[str]:
    rows: list[str] = []
    for issue in issues:
        labels = ", ".join(issue.labels) if issue.labels else "—"
        rows.append(
            "| [#{number}]({url}) | {title} | {author} | {state} | {reactions} | {comments} | "
            "{updated} | {created} | {labels} |".format(
                number=issue.number, url=issue.url, title=escape_cell(issue.title),
                author=escape_cell(issue.author), state=escape_cell(state_label(issue)),
                reactions=escape_cell(reaction_label(issue)), comments=issue.comments,
                updated=issue.updated_at[:10], created=issue.created_at[:10], labels=escape_cell(labels),
            )
        )
    return rows


def render_primary_table_rows(issues: list[IssueRecord]) -> list[str]:
    rows: list[str] = []
    for issue in issues:
        labels = ", ".join(issue.labels) if issue.labels else "—"
        rows.append(
            "| [#{number}]({url}) | {title} | {state} | {signal} | {updated} | {created} | {labels} |".format(
                number=issue.number, url=issue.url, title=escape_cell(issue.title),
                state=escape_cell(state_label(issue)), signal=escape_cell(signal_label(issue)),
                updated=issue.updated_at[:10], created=issue.created_at[:10], labels=escape_cell(labels),
            )
        )
    return rows


def render_markdown(primary: dict[str, list[IssueRecord]], secondary: dict[str, list[IssueRecord]]) -> str:
    if set(primary) != set(PRIMARY_VIEW_ORDER):
        raise RadarError("missing or unexpected primary radar view")
    if set(secondary) != set(SECONDARY_VIEW_ORDER):
        raise RadarError("missing or unexpected secondary radar view")

    lines = [
        "# AFFLR — Anthropic Failure Forensics Live Radar", "",
        "> Automated discovery metadata from public `anthropics/claude-code` issues. Inclusion here is **not** AFF acceptance, **not an AFF evidence level**, a vulnerability rating, or causal attribution.", "",
        "Primary ordering is a transparent discovery heuristic over the generic recent pool, targeted security/integrity search pools, known related context, issue text/labels, and recency. Reactions and comments remain secondary metadata only.", "",
        "The case archive remains manually reviewed under **Evidence before attribution**.", "",
        "# Primary forensic discovery", "",
    ]
    for name in PRIMARY_VIEW_ORDER:
        lines.extend([f"## {PRIMARY_VIEW_TITLES[name]}", "", PRIMARY_TABLE_HEADER, PRIMARY_TABLE_RULE, *render_primary_table_rows(primary[name][:25]), ""])

    lines.extend([
        "# Secondary discovery metadata", "",
        "Popularity and discussion volume can help find clusters, but they do not raise an issue's evidence level or forensic priority.", "",
    ])
    for name in SECONDARY_VIEW_ORDER:
        lines.extend([f"## {SECONDARY_VIEW_TITLES[name]}", "", TABLE_HEADER, TABLE_RULE, *render_secondary_table_rows(secondary[name][:25]), ""])
    return "\n".join(lines).rstrip() + "\n"


def render_readme_fragment(primary: dict[str, list[IssueRecord]]) -> str:
    if set(primary) != set(PRIMARY_VIEW_ORDER):
        raise RadarError("missing or unexpected primary radar view")
    lines = [
        "> Automated discovery metadata from public `anthropics/claude-code` issues. Primary ranking is **discovery-only** — not an AFF evidence level, vulnerability rating, or causal attribution.", "",
        "The live README prioritizes security/trust-boundary and provenance/integrity signals from both recent activity and targeted search pools. Popularity views remain in [`watchlist/candidates.md`](watchlist/candidates.md) as secondary discovery metadata.", "",
    ]
    for name in PRIMARY_VIEW_ORDER:
        issues = primary[name][:25]
        visible, hidden = issues[:5], issues[5:25]
        lines.extend([f"### {PRIMARY_VIEW_TITLES[name]}", "", PRIMARY_TABLE_HEADER, PRIMARY_TABLE_RULE, *render_primary_table_rows(visible), ""])
        if hidden:
            lines.extend(["<details>", f"<summary>Show remaining {len(hidden)}</summary>", "", PRIMARY_TABLE_HEADER, PRIMARY_TABLE_RULE, *render_primary_table_rows(hidden), "", "</details>", ""])
    return "\n".join(lines).rstrip() + "\n"


def inject_readme_fragment(readme: str, fragment: str) -> str:
    if readme.count(README_START) != 1 or readme.count(README_END) != 1:
        raise RadarError("README must contain exactly one AFFLR radar marker pair")
    start, end = readme.index(README_START), readme.index(README_END)
    if start >= end:
        raise RadarError("AFFLR README markers are inverted")
    return readme[: start + len(README_START)] + "\n" + fragment.rstrip() + "\n" + readme[end:]


def fetch_json(url: str, opener=urlopen) -> dict[str, Any]:
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "KeilerHirsch-AFFLR"})
    try:
        with opener(request, timeout=30) as response:
            raw = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RadarError("GitHub request failed") from exc
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise RadarError("GitHub returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise RadarError("GitHub returned non-object JSON")
    return payload


def collect_live_views() -> tuple[dict[str, list[IssueRecord]], dict[str, list[IssueRecord]]]:
    return collect_primary_views(fetch_json), collect_secondary_views(fetch_json)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AFFLR — Anthropic Failure Forensics Live Radar")
    parser.add_argument("--output", required=True)
    parser.add_argument("--readme")
    args = parser.parse_args(argv)

    primary, secondary = collect_live_views()
    rendered_watchlist = render_markdown(primary, secondary)

    readme_path = Path(args.readme) if args.readme else None
    rendered_readme: str | None = None
    if readme_path is not None:
        existing_readme = readme_path.read_text(encoding="utf-8")
        rendered_readme = inject_readme_fragment(existing_readme, render_readme_fragment(primary))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output_temp = output.with_suffix(output.suffix + ".tmp")
    with output_temp.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(rendered_watchlist)

    readme_temp: Path | None = None
    if readme_path is not None and rendered_readme is not None:
        readme_temp = readme_path.with_suffix(readme_path.suffix + ".tmp")
        with readme_temp.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(rendered_readme)

    output_temp.replace(output)
    if readme_temp is not None and readme_path is not None:
        readme_temp.replace(readme_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
