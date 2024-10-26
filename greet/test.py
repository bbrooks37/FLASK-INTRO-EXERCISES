import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertEqual(result.data, b'welcome')

    def test_welcome_home(self):
        result = self.app.get('/welcome/home')
        self.assertEqual(result.data, b'welcome home')

    def test_welcome_back(self):
        result = self.app.get('/welcome/back')
        self.assertEqual(result.data, b'welcome back')

if __name__ == '__main__':
    unittest.main()
