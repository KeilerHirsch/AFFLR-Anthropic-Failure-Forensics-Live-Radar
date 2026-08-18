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
            "body": "Observed model routing fallback with reproducible evidence.",
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
            raw["html_url"] = (
                f"https://github.com/anthropics/claude-code/issues/{raw['number']}"
            )
        return raw


class NormalizationTests(IssueFixtureMixin, unittest.TestCase):
    def test_normalize_issue_preserves_metadata(self):
        issue = afflr.normalize_issue(self.sample_issue())
        self.assertEqual(issue.number, 83510)
        self.assertEqual(issue.author, "KeilerHirsch")
        self.assertEqual(issue.reactions_total, 12)
        self.assertEqual(issue.comments, 34)
        self.assertEqual(issue.labels, ("bug", "model"))
        self.assertIn("routing fallback", issue.body)

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

    def test_unexpected_issue_url_is_rejected(self):
        with self.assertRaises(afflr.RadarError):
            afflr.normalize_issue(
                self.sample_issue(html_url="https://evil.example/issues/83510")
            )


class DiscoveryTests(IssueFixtureMixin, unittest.TestCase):
    def test_fabricated_monitor_event_is_integrity_signal(self):
        issue = afflr.normalize_issue(
            self.sample_issue(
                number=87519,
                title="Monitor tool: task notifications deliver fabricated events",
                body="The subprocess never emitted the notification.",
                labels=[{"name": "bug"}, {"name": "area:tools"}],
                updated_at="2026-08-18T04:19:04Z",
                created_at="2026-08-18T04:17:54Z",
            )
        )
        self.assertIn("observation / provenance integrity", afflr.classify_signals(issue))

    def test_credential_permission_issue_is_security_signal(self):
        issue = afflr.normalize_issue(
            self.sample_issue(
                number=90001,
                title="Permission boundary leaks session token",
                body="Credential handling crosses an authorization boundary.",
                labels=[{"name": "security"}, {"name": "area:auth"}],
            )
        )
        self.assertIn("security / trust boundary", afflr.classify_signals(issue))

    def test_related_context_is_explicit_not_evidence_level(self):
        issue = afflr.normalize_issue(self.sample_issue(number=87086))
        self.assertIn("related context", afflr.classify_signals(issue))

    def test_primary_collection_keeps_related_context_and_fresh_critical(self):
        recent_payload = {
            "incomplete_results": False,
            "items": [
                self.sample_issue(
                    number=87519,
                    title="Monitor notifications deliver fabricated events",
                    body="Observation event mismatch.",
                    labels=[{"name": "bug"}, {"name": "area:tools"}],
                    created_at="2026-08-18T04:17:54Z",
                    updated_at="2026-08-18T04:19:04Z",
                ),
                self.sample_issue(
                    number=77777,
                    title="Feature request: themes",
                    body="Cosmetic only.",
                    labels=[{"name": "enhancement"}],
                    created_at="2026-08-18T03:00:00Z",
                    updated_at="2026-08-18T03:00:00Z",
                ),
            ],
        }

        pinned = {
            number: self.sample_issue(
                number=number,
                title=f"related {number} provenance routing",
                body="benchmark provenance and model routing context",
                labels=[{"name": "model"}],
                created_at="2026-08-16T00:00:00Z",
                updated_at="2026-08-16T01:00:00Z",
            )
            for number in afflr.RELATED_CONTEXT_NUMBERS
        }

        def fake_fetch(url):
            if url.startswith(afflr.SEARCH_ENDPOINT):
                return recent_payload
            number = int(url.rsplit("/", 1)[1])
            return pinned[number]

        views = afflr.collect_primary_views(fake_fetch)
        integrity_numbers = {issue.number for issue in views["evidence-integrity"]}
        fresh_numbers = {issue.number for issue in views["fresh-critical"]}
        self.assertIn(87086, integrity_numbers)
        self.assertIn(87519, integrity_numbers)
        self.assertIn(87519, fresh_numbers)
        self.assertNotIn(77777, fresh_numbers)

    def test_secondary_views_keep_old_discovery_metadata(self):
        calls = []

        def fake_fetch(url):
            calls.append(url)
            return {
                "incomplete_results": False,
                "items": [self.sample_issue(number=len(calls))],
            }

        views = afflr.collect_secondary_views(fake_fetch)
        self.assertEqual(len(calls), 3)
        self.assertEqual(set(views), set(afflr.SECONDARY_VIEW_ORDER))
        self.assertIn("sort=reactions", calls[0])
        self.assertIn("sort=comments", calls[1])
        self.assertIn("sort=updated", calls[2])


class RenderingTests(IssueFixtureMixin, unittest.TestCase):
    def primary_views(self, issue):
        return {name: [issue] for name in afflr.PRIMARY_VIEW_ORDER}

    def secondary_views(self, issue):
        return {name: [issue] for name in afflr.SECONDARY_VIEW_ORDER}

    def test_watchlist_renders_primary_then_secondary(self):
        issue = afflr.normalize_issue(self.sample_issue())
        text = afflr.render_markdown(
            self.primary_views(issue),
            self.secondary_views(issue),
        )
        self.assertIn("# Primary forensic discovery", text)
        self.assertIn("🛡️ Security & trust-boundary signals", text)
        self.assertIn("# Secondary discovery metadata", text)
        self.assertIn("## Most reacted", text)
        self.assertIn("not an AFF evidence level", text)

    def test_readme_fragment_omits_popularity_views(self):
        issue = afflr.normalize_issue(self.sample_issue())
        text = afflr.render_readme_fragment(self.primary_views(issue))
        self.assertIn("Security & trust-boundary signals", text)
        self.assertIn("Evidence / provenance / integrity signals", text)
        self.assertIn("Fresh critical signals", text)
        self.assertNotIn("Most reacted", text)
        self.assertIn("watchlist/candidates.md", text)

    def test_primary_rows_explain_signal(self):
        issue = afflr.normalize_issue(
            self.sample_issue(
                number=87519,
                title="Monitor fabricated notification event",
                body="subprocess never emitted it",
                labels=[{"name": "area:tools"}, {"name": "bug"}],
            )
        )
        text = "\n".join(afflr.render_primary_table_rows([issue]))
        self.assertIn("observation / provenance integrity", text)
        self.assertIn("high-signal label", text)

    def test_render_escapes_untrusted_text(self):
        issue = afflr.normalize_issue(
            self.sample_issue(title="[click](https://evil.example) | <script>")
        )
        text = afflr.render_markdown(
            self.primary_views(issue),
            self.secondary_views(issue),
        )
        self.assertIn(r"\[click\](https://evil.example) \| &lt;script&gt;", text)
        self.assertNotIn("<script>", text)

    def test_readme_top_five_and_collapses_rest(self):
        issues = [
            afflr.normalize_issue(self.sample_issue(number=number))
            for number in range(1, 26)
        ]
        primary = {name: issues for name in afflr.PRIMARY_VIEW_ORDER}
        text = afflr.render_readme_fragment(primary)
        self.assertEqual(text.count("<details>"), 3)
        self.assertEqual(text.count("<summary>Show remaining 20</summary>"), 3)

    def test_inject_readme_fragment_preserves_outside_content(self):
        original = (
            "before\n"
            "<!-- AFFLR-RADAR:START -->\n"
            "old\n"
            "<!-- AFFLR-RADAR:END -->\n"
            "after\n"
        )
        updated = afflr.inject_readme_fragment(original, "new\n")
        self.assertEqual(
            updated,
            "before\n"
            "<!-- AFFLR-RADAR:START -->\n"
            "new\n"
            "<!-- AFFLR-RADAR:END -->\n"
            "after\n",
        )


class HttpAndCliTests(IssueFixtureMixin, unittest.TestCase):
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
            seen["headers"] = {
                key.lower(): value for key, value in request.header_items()
            }
            return self.DummyResponse(
                b'{"incomplete_results": false, "items": []}'
            )

        payload = afflr.fetch_json(
            "https://api.github.com/search/issues?q=x", opener=opener
        )
        self.assertFalse(payload["incomplete_results"])
        self.assertNotIn("authorization", seen["headers"])

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


class RepositoryContractTests(unittest.TestCase):
    def test_readme_has_single_generated_region(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("<!-- AFFLR-RADAR:START -->"), 1)
        self.assertEqual(text.count("<!-- AFFLR-RADAR:END -->"), 1)
        self.assertIn("Evidence before attribution.", text)

    def test_workflow_contract(self):
        text = Path(".github/workflows/afflr.yml").read_text(encoding="utf-8")
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn("contents: write", text)
        self.assertIn("README.md", text)
        self.assertIn("watchlist/candidates.md", text)
        self.assertIn("git diff --quiet", text)
        self.assertIn("git push origin HEAD:main", text)
        self.assertIn("remote main moved during AFFLR run", text)
        self.assertNotIn("secrets.PAT", text)


if __name__ == "__main__":
    unittest.main()
