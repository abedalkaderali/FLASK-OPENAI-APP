import unittest
from flask import json
from src.app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

class TestGenerateImageEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.api_key = os.getenv("X_API_KEY")

    def test_generate_image_base64(self):
        response = self.app.post('/generateImage',
                                 headers={'x-api-key': self.api_key, 'response-type': 'base64'},
                                 data=json.dumps({"content": "A red elephant"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("b64_json", data["response"])
        self.assertIn("version", data)

    def test_generate_image_missing_content(self):
        response = self.app.post('/generateImage',
                                 headers={'x-api-key': self.api_key, 'response-type': 'base64'},
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_generate_image_invalid_api_key(self):
        response = self.app.post('/generateImage',
                                 headers={'x-api-key': 'invalid_key', 'response-type': 'base64'},
                                 data=json.dumps({"content": "A red elephant"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
