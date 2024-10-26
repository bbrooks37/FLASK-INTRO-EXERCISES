import unittest
from app import app

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        result = self.app.get('/add?a=10&b=20')
        self.assertEqual(result.data, b'30')

    def test_sub(self):
        result = self.app.get('/sub?a=20&b=10')
        self.assertEqual(result.data, b'10')

    def test_mult(self):
        result = self.app.get('/mult?a=10&b=20')
        self.assertEqual(result.data, b'200')

    def test_div(self):
        result = self.app.get('/div?a=20&b=10')
        self.assertEqual(result.data, b'2.0')

    def test_all_in_one(self):
        response = self.app.get('/add?a=10&b=20')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'30')

        response = self.app.get('/sub?a=20&b=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'10')

        response = self.app.get('/mult?a=10&b=20')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'200')

        response = self.app.get('/div?a=20&b=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'2.0')

if __name__ == '__main__':
    unittest.main()
