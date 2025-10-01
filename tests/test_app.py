import unittest
from flask import json
from src.app import create_app 
from dotenv import load_dotenv
import os

load_dotenv()
class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.api_key = os.getenv("API_KEY")

    def test_root_endpoint(self):
        response = self.app.get('/', headers={'x-api-key': self.api_key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"response": "Hello, World!"})

    def test_chat_endpoint(self):
        response = self.app.post('/chat', 
                                 headers={'x-api-key': self.api_key}, 
                                 data=json.dumps({"content": "what is the capital of Lebanon"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json)
        self.assertIn("version", response.json)

    def test_generate_image_endpoint(self):
        response = self.app.post('/generateImage', 
                                 headers={'x-api-key': self.api_key, 'response-type': 'base64'}, 
                                 data=json.dumps({"content": "A red elephant"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("base64", response.json)
        self.assertIn("version", response.json)

if __name__ == '__main__':
    unittest.main()
