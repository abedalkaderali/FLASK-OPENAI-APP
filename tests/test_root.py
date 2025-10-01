import unittest
from src.app import create_app

class TestRootEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_root_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"response": "Hello, World!"})

if __name__ == '__main__':
    unittest.main()

