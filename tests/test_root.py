import unittest
from src.app import create_app
from flask import json
import os
from dotenv import load_dotenv

load_dotenv()

class TestRootEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.api_key = os.getenv("X_API_KEY")

    def test_root_endpoint(self):
        resp = self.app.get('/', headers={'x-api-key': self.api_key})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, {"response": "Hello, World!"})

    def test_root_endpoint_missing_content(self):
        resp = self.app.post('/',
            headers={'x-api-key': self.api_key},
            data=json.dumps({}),
            content_type='application/json')
        self.assertEqual(resp.status_code, 405)

    def test_root_endpoint_missing_api_key(self):
        resp = self.app.get('/', headers={'x-api-key': 'invalid_key'})
        self.assertEqual(resp.status_code, 401)

if __name__ == '__main__':
    unittest.main()
