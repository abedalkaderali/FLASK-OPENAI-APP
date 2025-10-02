import unittest
from flask import json
from src.app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

class ChatEndpointTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.api_key = os.getenv("X_API_KEY")

    def test_chat_endpoint_success(self):
        response = self.app.post('/chat',
                                 headers={'x-api-key': self.api_key},
                                 data=json.dumps({'content': 'what is the capital of Lebanon'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('response', data)
        self.assertIn('version', data)

    def test_chat_endpoint_missing_content(self):
        response = self.app.post('/chat',
                                 headers={'x-api-key': self.api_key},
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_chat_endpoint_invalid_api_key(self):
        response = self.app.post('/chat',
                                 headers={'x-api-key': 'invalid_key'},
                                 data=json.dumps({'content': 'what is the capital of Lebanon'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
