import unittest
from urllib.parse import parse_qs, urlparse

from scripts import afflr


class TargetedQueryScopeRegressionTests(unittest.TestCase):
    def test_each_or_arm_repeats_repo_and_issue_scope(self):
        for query in afflr.TARGETED_SEARCH_QUERIES:
            url = afflr.build_search_url(per_page=100, query=query)
            q = parse_qs(urlparse(url).query)["q"][0]
            expected_arms = query.count(" OR ") + 1
            self.assertEqual(
                q.count(afflr.SEARCH_SCOPE),
                expected_arms,
                msg=f"targeted OR query leaked search scope: {q}",
            )


if __name__ == "__main__":
    unittest.main()
