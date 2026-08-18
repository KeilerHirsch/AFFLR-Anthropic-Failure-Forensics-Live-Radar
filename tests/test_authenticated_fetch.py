import os
import unittest
from unittest.mock import patch

from scripts import afflr


class DummyResponse:
    def __init__(self, body):
        self._body = body

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class AuthenticatedFetchTests(unittest.TestCase):
    def test_fetch_json_uses_github_token_when_available(self):
        seen = {}

        def opener(request, timeout=0):
            seen["headers"] = {
                key.lower(): value for key, value in request.header_items()
            }
            return DummyResponse(b'{"incomplete_results": false, "items": []}')

        with patch.dict(os.environ, {"GITHUB_TOKEN": "test-token"}, clear=False):
            afflr.fetch_json(
                "https://api.github.com/search/issues?q=x",
                opener=opener,
            )

        self.assertEqual(seen["headers"].get("authorization"), "Bearer test-token")


if __name__ == "__main__":
    unittest.main()
