import unittest
from unittest.mock import patch
from evance_api.client import EvanceClient
from evance_api.auth import EvanceAuth


class TestEvanceClient(unittest.TestCase):
    @patch("requests.post")
    def test_authentication(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"access_token": "test_token"}

        auth = EvanceAuth.from_json("akiba.json")
        auth.authenticate()

        self.assertEqual(auth.token, "test_token")

    @patch("requests.request")
    def test_get_products(self, mock_request):
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"products": []}

        auth = EvanceAuth.from_json("akiba.json")
        auth.token = "test_token"

        client = EvanceClient(auth)
        response = client.get("products")

        self.assertIn("products", response)
