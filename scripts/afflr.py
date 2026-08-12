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
    """Raised when AFFLR cannot produce a complete, trustworthy snapshot."""


REACTION_KEYS = (
    "+1",
    "-1",
    "laugh",
    "hooray",
    "confused",
    "heart",
    "rocket",
    "eyes",
)
REACTION_EMOJI = {
    "+1": "👍",
    "-1": "👎",
    "laugh": "😄",
    "hooray": "🎉",
    "confused": "😕",
    "heart": "❤️",
    "rocket": "🚀",
    "eyes": "👀",
}
VIEW_SORT = {
    "most-reacted": "reactions",
    "most-discussed": "comments",
    "recently-active": "updated",
}
VIEW_TITLES = {
    "most-reacted": "Most reacted",
    "most-discussed": "Most discussed",
    "recently-active": "Recently active",
}
README_VIEW_TITLES = {
    "most-reacted": "🔥 Most reacted",
    "most-discussed": "💬 Most discussed",
    "recently-active": "🆕 Recently active",
}
VIEW_ORDER = ("most-reacted", "most-discussed", "recently-active")
SEARCH_ENDPOINT = "https://api.github.com/search/issues"
SEARCH_SCOPE = "repo:anthropics/claude-code is:issue"
EXPECTED_ISSUE_PREFIX = "https://github.com/anthropics/claude-code/issues/"
TABLE_HEADER = (
    "| Issue | Title | Author | State | Reactions | Comments | Updated | Created | Labels |"
)
TABLE_RULE = "|---:|---|---|---|---:|---:|---|---|---|"
README_START = "<!-- AFFLR-RADAR:START -->"
README_END = "<!-- AFFLR-RADAR:END -->"


@dataclass(frozen=True)
class IssueRecord:
    number: int
    title: str
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
    if not isinstance(reactions, dict) or not isinstance(
        reactions.get("total_count"), int
    ):
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

    if not isinstance(number, int) or not isinstance(comments, int):
        raise RadarError("invalid numeric issue metadata")
    if number <= 0 or comments < 0:
        raise RadarError("out-of-range numeric issue metadata")
    if not isinstance(title, str) or not isinstance(url, str) or not isinstance(state, str):
        raise RadarError("invalid string issue metadata")
    if state not in {"open", "closed"}:
        raise RadarError(f"invalid issue state: {state!r}")

    expected_url = f"{EXPECTED_ISSUE_PREFIX}{number}"
    if url != expected_url:
        raise RadarError(f"unexpected issue URL: {url!r}")

    reactions_total = reactions["total_count"]
    if reactions_total < 0 or any(count < 0 for _, count in reaction_pairs):
        raise RadarError("negative reaction count")

    return IssueRecord(
        number=number,
        title=title,
        url=url,
        author=user["login"],
        state=state,
        state_reason=state_reason,
        reactions_total=reactions_total,
        reactions=tuple(reaction_pairs),
        comments=comments,
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


def sort_view(view_name: str, issues: list[IssueRecord]) -> list[IssueRecord]:
    if view_name == "most-reacted":
        return sorted(
            issues,
            key=lambda issue: (
                issue.reactions_total,
                issue.comments,
                _ts(issue.updated_at),
                issue.number,
            ),
            reverse=True,
        )
    if view_name == "most-discussed":
        return sorted(
            issues,
            key=lambda issue: (
                issue.comments,
                issue.reactions_total,
                _ts(issue.updated_at),
                issue.number,
            ),
            reverse=True,
        )
    if view_name == "recently-active":
        return sorted(
            issues,
            key=lambda issue: (
                _ts(issue.updated_at),
                issue.reactions_total,
                issue.comments,
                issue.number,
            ),
            reverse=True,
        )
    raise RadarError(f"unknown view: {view_name}")


def build_search_url(view_name: str) -> str:
    try:
        sort_name = VIEW_SORT[view_name]
    except KeyError as exc:
        raise RadarError(f"unknown view: {view_name}") from exc

    params = {
        "q": SEARCH_SCOPE,
        "sort": sort_name,
        "order": "desc",
        "per_page": 25,
    }
    return f"{SEARCH_ENDPOINT}?{urlencode(params)}"


def collect_views(
    fetcher: Callable[[str], dict[str, Any]],
) -> dict[str, list[IssueRecord]]:
    result: dict[str, list[IssueRecord]] = {}
    for name in VIEW_ORDER:
        issues = normalize_search_response(fetcher(build_search_url(name)))
        if len(issues) > 25:
            raise RadarError(f"too many rows returned for {name}")
        result[name] = sort_view(name, issues)
    return result


def escape_cell(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = escaped.replace("\\", "\\\\")
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
        f"{REACTION_EMOJI[key]} {count}"
        for key, count in issue.reactions
        if count
    )
    if not detail:
        return str(issue.reactions_total)
    return f"{issue.reactions_total} ({detail})"


def render_table_rows(issues: list[IssueRecord]) -> list[str]:
    rows: list[str] = []
    for issue in issues:
        labels = ", ".join(issue.labels) if issue.labels else "—"
        rows.append(
            "| [#{number}]({url}) | {title} | {author} | {state} | {reactions} | "
            "{comments} | {updated} | {created} | {labels} |".format(
                number=issue.number,
                url=issue.url,
                title=escape_cell(issue.title),
                author=escape_cell(issue.author),
                state=escape_cell(state_label(issue)),
                reactions=escape_cell(reaction_label(issue)),
                comments=issue.comments,
                updated=issue.updated_at[:10],
                created=issue.created_at[:10],
                labels=escape_cell(labels),
            )
        )
    return rows


def render_markdown(views: dict[str, list[IssueRecord]]) -> str:
    if set(views) != set(VIEW_ORDER):
        raise RadarError("missing or unexpected radar view")

    lines = [
        "# AFFLR — Anthropic Failure Forensics Live Radar",
        "",
        "> Automated discovery metadata from public `anthropics/claude-code` issues. "
        "Inclusion here is **not** AFF acceptance, an evidence level, or causal attribution.",
        "",
        "Reactions, comments, labels, and activity are discovery signals only. "
        "The case archive remains manually reviewed under **Evidence before attribution**.",
        "",
    ]

    for name in VIEW_ORDER:
        lines.extend(
            [
                f"## {VIEW_TITLES[name]}",
                "",
                TABLE_HEADER,
                TABLE_RULE,
                *render_table_rows(views[name][:25]),
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_readme_fragment(views: dict[str, list[IssueRecord]]) -> str:
    if set(views) != set(VIEW_ORDER):
        raise RadarError("missing or unexpected radar view")

    lines = [
        "> Automated discovery metadata from public `anthropics/claude-code` issues. "
        "Popularity is a discovery signal, not evidence.",
        "",
    ]

    for name in VIEW_ORDER:
        issues = views[name][:25]
        visible = issues[:5]
        hidden = issues[5:25]
        lines.extend(
            [
                f"### {README_VIEW_TITLES[name]}",
                "",
                TABLE_HEADER,
                TABLE_RULE,
                *render_table_rows(visible),
                "",
            ]
        )
        if hidden:
            lines.extend(
                [
                    "<details>",
                    f"<summary>Show remaining {len(hidden)}</summary>",
                    "",
                    TABLE_HEADER,
                    TABLE_RULE,
                    *render_table_rows(hidden),
                    "",
                    "</details>",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def inject_readme_fragment(readme: str, fragment: str) -> str:
    if readme.count(README_START) != 1 or readme.count(README_END) != 1:
        raise RadarError("README must contain exactly one AFFLR radar marker pair")

    start = readme.index(README_START)
    end = readme.index(README_END)
    if start >= end:
        raise RadarError("AFFLR README markers are inverted")

    before = readme[: start + len(README_START)]
    after = readme[end:]
    return before + "\n" + fragment.rstrip() + "\n" + after


def fetch_json(url: str, opener=urlopen) -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "KeilerHirsch-AFFLR",
        },
    )
    # Deliberately unauthenticated: upstream search is public.
    try:
        with opener(request, timeout=30) as response:
            raw = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RadarError("GitHub search request failed") from exc

    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise RadarError("GitHub search returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise RadarError("GitHub search returned non-object JSON")
    return payload


def collect_live_views() -> dict[str, list[IssueRecord]]:
    return collect_views(fetch_json)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="AFFLR — Anthropic Failure Forensics Live Radar"
    )
    parser.add_argument("--output", required=True)
    parser.add_argument("--readme")
    args = parser.parse_args(argv)

    # Collect and render everything before touching either destination.
    views = collect_live_views()
    rendered_watchlist = render_markdown(views)

    readme_path = Path(args.readme) if args.readme else None
    rendered_readme: str | None = None
    if readme_path is not None:
        existing_readme = readme_path.read_text(encoding="utf-8")
        rendered_readme = inject_readme_fragment(
            existing_readme, render_readme_fragment(views)
        )

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
