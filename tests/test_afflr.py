import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import afflr


class IssueFixtureMixin:
    def sample_issue(self, **overrides):
        raw = {
            "number": 83510,
            "title": "[MODEL] quality regression | measured",
            "html_url": "https://github.com/anthropics/claude-code/issues/83510",
            "user": {"login": "KeilerHirsch"},
            "state": "open",
            "state_reason": None,
            "comments": 34,
            "created_at": "2026-08-04T10:00:00Z",
            "updated_at": "2026-08-12T10:00:00Z",
            "labels": [{"name": "model"}, {"name": "bug"}],
            "reactions": {
                "total_count": 12,
                "+1": 9,
                "-1": 0,
                "laugh": 0,
                "hooray": 0,
                "confused": 0,
                "heart": 1,
                "rocket": 2,
                "eyes": 0,
            },
        }
        raw.update(overrides)
        if "number" in overrides and "html_url" not in overrides:
            raw["html_url"] = f"https://github.com/anthropics/claude-code/issues/{raw['number']}"
        return raw


class NormalizationTests(IssueFixtureMixin, unittest.TestCase):
    def test_normalize_issue_preserves_metadata(self):
        issue = afflr.normalize_issue(self.sample_issue())
        self.assertEqual(issue.number, 83510)
        self.assertEqual(issue.author, "KeilerHirsch")
        self.assertEqual(issue.reactions_total, 12)
        self.assertEqual(issue.comments, 34)
        self.assertEqual(issue.labels, ("bug", "model"))

    def test_closed_state_reason_is_preserved(self):
        issue = afflr.normalize_issue(
            self.sample_issue(state="closed", state_reason="not_planned")
        )
        self.assertEqual(issue.state, "closed")
        self.assertEqual(issue.state_reason, "not_planned")

    def test_incomplete_results_fail_closed(self):
        with self.assertRaises(afflr.RadarError):
            afflr.normalize_search_response(
                {"incomplete_results": True, "items": [self.sample_issue()]}
            )

    def test_missing_required_field_fails_closed(self):
        raw = self.sample_issue()
        del raw["user"]
        with self.assertRaises(afflr.RadarError):
            afflr.normalize_search_response(
                {"incomplete_results": False, "items": [raw]}
            )

    def test_non_string_title_is_rejected(self):
        with self.assertRaises(afflr.RadarError):
            afflr.normalize_issue(self.sample_issue(title={"oops": True}))

    def test_unexpected_issue_url_is_rejected(self):
        with self.assertRaises(afflr.RadarError):
            afflr.normalize_issue(
                self.sample_issue(html_url="https://evil.example/issues/83510")
            )


class OrderingAndQueryTests(IssueFixtureMixin, unittest.TestCase):
    def test_most_reacted_tie_breaks_deterministically(self):
        raws = (
            self.sample_issue(number=1, comments=2, updated_at="2026-08-12T09:00:00Z"),
            self.sample_issue(number=2, comments=3, updated_at="2026-08-12T08:00:00Z"),
            self.sample_issue(number=3, comments=3, updated_at="2026-08-12T10:00:00Z"),
        )
        issues = [afflr.normalize_issue(raw) for raw in raws]
        self.assertEqual(
            [issue.number for issue in afflr.sort_view("most-reacted", issues)],
            [3, 2, 1],
        )

    def test_search_urls_use_full_issue_scope_and_top_25(self):
        urls = {
            name: afflr.build_search_url(name)
            for name in ("most-reacted", "most-discussed", "recently-active")
        }
        for url in urls.values():
            self.assertIn("repo%3Aanthropics%2Fclaude-code", url)
            self.assertIn("is%3Aissue", url)
            self.assertIn("per_page=25", url)
            self.assertIn("order=desc", url)
        self.assertIn("sort=reactions", urls["most-reacted"])
        self.assertIn("sort=comments", urls["most-discussed"])
        self.assertIn("sort=updated", urls["recently-active"])

    def test_collect_views_makes_exactly_three_requests(self):
        calls = []

        def fake_fetch(url):
            calls.append(url)
            return {
                "incomplete_results": False,
                "items": [self.sample_issue(number=len(calls))],
            }

        views = afflr.collect_views(fake_fetch)
        self.assertEqual(len(calls), 3)
        self.assertEqual(
            set(views), {"most-reacted", "most-discussed", "recently-active"}
        )


class RenderingTests(IssueFixtureMixin, unittest.TestCase):
    def test_render_contains_required_metadata_and_escapes_table_text(self):
        issue = afflr.normalize_issue(
            self.sample_issue(title="bad | title <script>")
        )
        views = {
            name: [issue]
            for name in ("most-reacted", "most-discussed", "recently-active")
        }
        text = afflr.render_markdown(views)
        self.assertIn("# AFFLR — Anthropic Failure Forensics Live Radar", text)
        self.assertIn("[#83510]", text)
        self.assertIn("KeilerHirsch", text)
        self.assertIn("12 (", text)
        self.assertIn("34", text)
        self.assertIn(r"bad \| title &lt;script&gt;", text)
        self.assertNotIn("<script>", text)

    def test_markdown_link_syntax_in_title_is_neutralized(self):
        issue = afflr.normalize_issue(
            self.sample_issue(title="[click](https://evil.example) | test")
        )
        views = {
            name: [issue]
            for name in ("most-reacted", "most-discussed", "recently-active")
        }
        text = afflr.render_markdown(views)
        self.assertIn(r"\[click\](https://evil.example) \| test", text)
        self.assertNotIn("[click](https://evil.example)", text)

    def test_render_has_no_scores_or_new_marker(self):
        issue = afflr.normalize_issue(self.sample_issue())
        views = {
            name: [issue]
            for name in ("most-reacted", "most-discussed", "recently-active")
        }
        text = afflr.render_markdown(views)
        self.assertNotIn("Forensic score", text)
        self.assertNotIn("AFF score", text)
        self.assertNotIn("**NEW**", text)

    def test_render_is_byte_stable(self):
        issue = afflr.normalize_issue(self.sample_issue())
        views = {
            name: [issue]
            for name in ("most-reacted", "most-discussed", "recently-active")
        }
        self.assertEqual(afflr.render_markdown(views), afflr.render_markdown(views))


class HttpAndCliTests(unittest.TestCase):
    class DummyResponse:
        def __init__(self, body):
            self._body = body

        def read(self):
            return self._body

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def test_fetch_json_sends_no_authentication_header(self):
        seen = {}

        def opener(request, timeout=0):
            seen["headers"] = {key.lower(): value for key, value in request.header_items()}
            return self.DummyResponse(
                b'{"incomplete_results": false, "items": []}'
            )

        payload = afflr.fetch_json(
            "https://api.github.com/search/issues?q=x", opener=opener
        )
        self.assertFalse(payload["incomplete_results"])
        self.assertNotIn("authorization", seen["headers"])

    def test_invalid_json_fails_closed(self):
        def opener(request, timeout=0):
            return self.DummyResponse(b"not-json")

        with self.assertRaises(afflr.RadarError):
            afflr.fetch_json(
                "https://api.github.com/search/issues?q=x", opener=opener
            )

    def test_cli_failure_does_not_replace_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "radar.md"
            output.write_text("last known good\n", encoding="utf-8")
            with patch.object(
                afflr, "collect_live_views", side_effect=afflr.RadarError("boom")
            ):
                with self.assertRaises(afflr.RadarError):
                    afflr.main(["--output", str(output)])
            self.assertEqual(
                output.read_text(encoding="utf-8"), "last known good\n"
            )


class WorkflowContractTests(unittest.TestCase):
    def test_workflow_contract(self):
        text = Path(".github/workflows/afflr.yml").read_text(encoding="utf-8")
        self.assertIn("name: AFFLR", text)
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("contents: write", text)
        self.assertIn("pull-requests: write", text)
        self.assertIn("automation/afflr", text)
        self.assertIn("3d3c42e5aac5ba805825da76410c181273ba90b1", text)
        self.assertNotIn("secrets.PAT", text)
        self.assertNotIn("cases/AFF-", text)
        self.assertIn("gh pr close", text)
        self.assertIn("--force-with-lease", text)


if __name__ == "__main__":
    unittest.main()
