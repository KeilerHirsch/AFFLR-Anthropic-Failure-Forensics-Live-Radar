import unittest
from urllib.parse import parse_qs, urlparse

from scripts import afflr


def sample_issue(number, *, title="ordinary issue", body="ordinary body", labels=None, created=None, updated=None):
    return {
        "number": number,
        "title": title,
        "body": body,
        "html_url": f"https://github.com/anthropics/claude-code/issues/{number}",
        "user": {"login": "tester"},
        "state": "open",
        "state_reason": None,
        "comments": 0,
        "created_at": created or "2026-08-01T00:00:00Z",
        "updated_at": updated or "2026-08-01T00:00:00Z",
        "labels": [{"name": name} for name in (labels or ["bug"])],
        "reactions": {
            "total_count": 0,
            "+1": 0,
            "-1": 0,
            "laugh": 0,
            "hooray": 0,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0,
        },
    }


class TargetedPoolTests(unittest.TestCase):
    def test_targeted_queries_keep_repo_issue_scope(self):
        for query in afflr.TARGETED_SEARCH_QUERIES:
            url = afflr.build_search_url(per_page=100, query=query)
            params = parse_qs(urlparse(url).query)
            q = params["q"][0]
            self.assertIn("repo:anthropics/claude-code", q)
            self.assertIn("is:issue", q)
            self.assertIn(query, q)
            self.assertEqual(params["per_page"], ["100"])

    def test_targeted_pool_deduplicates_overlap(self):
        hit = sample_issue(
            87519,
            title="Monitor notifications deliver fabricated events",
            body="permission boundary and provenance mismatch",
            labels=["bug", "area:tools"],
        )
        calls = 0

        def fake_fetch(url):
            nonlocal calls
            calls += 1
            return {"incomplete_results": False, "items": [hit]}

        pool = afflr.collect_targeted_pool(fake_fetch)
        self.assertEqual(calls, len(afflr.TARGETED_SEARCH_QUERIES))
        self.assertEqual([issue.number for issue in pool], [87519])

    def test_targeted_hit_survives_outside_generic_recent_window(self):
        recent_payload = {
            "incomplete_results": False,
            "items": [sample_issue(99999, title="new cosmetic issue", body="theme request")],
        }
        deep_hit = sample_issue(
            87519,
            title="Monitor task notification fabricated event",
            body="subprocess never emitted the observation",
            labels=["bug", "area:tools"],
            created="2026-08-18T04:17:54Z",
            updated="2026-08-18T04:19:04Z",
        )
        targeted_payload = {"incomplete_results": False, "items": [deep_hit]}
        pinned = {
            number: sample_issue(
                number,
                title=f"related {number} routing provenance",
                body="benchmark provenance context",
                labels=["model"],
            )
            for number in afflr.RELATED_CONTEXT_NUMBERS
        }

        def fake_fetch(url):
            if url.startswith(afflr.ISSUE_ENDPOINT):
                return pinned[int(url.rsplit("/", 1)[1])]
            q = parse_qs(urlparse(url).query)["q"][0]
            if q == afflr.SEARCH_SCOPE:
                return recent_payload
            return targeted_payload

        views = afflr.collect_primary_views(fake_fetch)
        integrity = {issue.number for issue in views["evidence-integrity"]}
        fresh = {issue.number for issue in views["fresh-critical"]}
        self.assertIn(87519, integrity)
        self.assertIn(87519, fresh)
        self.assertNotIn(99999, fresh)

    def test_invalid_search_page_size_fails_closed(self):
        with self.assertRaises(afflr.RadarError):
            afflr.build_search_url(per_page=101)


if __name__ == "__main__":
    unittest.main()
