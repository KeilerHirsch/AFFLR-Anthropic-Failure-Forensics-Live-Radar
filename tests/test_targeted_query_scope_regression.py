import unittest
from urllib.parse import parse_qs, urlparse

from scripts import afflr


class TargetedQueryScopeRegressionTests(unittest.TestCase):
    def test_targeted_or_query_is_grouped_inside_repo_scope(self):
        for query in afflr.TARGETED_SEARCH_QUERIES:
            url = afflr.build_search_url(per_page=100, query=query)
            q = parse_qs(urlparse(url).query)["q"][0]
            self.assertEqual(q.count(afflr.SEARCH_SCOPE), 1)
            self.assertTrue(
                q.startswith(f"{afflr.SEARCH_SCOPE} ("),
                msg=f"targeted query is not grouped under repo scope: {q}",
            )
            self.assertTrue(q.endswith(")"), msg=f"targeted query is not closed: {q}")

    def test_targeted_queries_stay_within_github_boolean_operator_limit(self):
        for query in afflr.TARGETED_SEARCH_QUERIES:
            self.assertLessEqual(
                query.count(" OR "),
                5,
                msg=f"GitHub rejects targeted query with >5 boolean operators: {query}",
            )


if __name__ == "__main__":
    unittest.main()
