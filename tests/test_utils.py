import unittest
from flask import Flask
from app.utils import get_request_metadata

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/test', methods=['GET'])
        def test_route():
            return get_request_metadata()

    def test_get_request_metadata(self):
        with self.app.test_client() as client:
            response = client.get('/test', headers={"User-Agent": "Test-Agent"})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['url'], 'http://localhost/test')
            self.assertEqual(data['user_agent'], 'Test-Agent')