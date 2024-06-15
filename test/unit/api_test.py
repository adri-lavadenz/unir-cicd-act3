import unittest
import pytest
from app.api import api_application

@pytest.mark.unit
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = api_application.test_client()
        self.app.testing = True

    def test_add_endpoint(self):
        response = self.app.get('/calc/add/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '5')

    def test_subtract_endpoint(self):
        response = self.app.get('/calc/substract/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '-1')

    def test_multiply_endpoint(self):
        response = self.app.get('/calc/multiply/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '6')

    def test_divide_endpoint(self):
        response = self.app.get('/calc/divide/6/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '2.0')

    def test_divide_by_zero(self):
        response = self.app.get('/calc/divide/1/0')
        self.assertEqual(response.status_code, 400)

    def test_power_endpoint(self):
        response = self.app.get('/calc/power/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '8')

    def test_sqrt_endpoint(self):
        response = self.app.get('/calc/sqrt/9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '3.0')

    def test_sqrt_negative_number(self):
        response = self.app.get('/calc/sqrt/-1')
        self.assertEqual(response.status_code, 400)

    def test_log10_endpoint(self):
        response = self.app.get('/calc/log10/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '2.0')

    def test_log10_non_positive_number(self):
        response = self.app.get('/calc/log10/0')
        self.assertEqual(response.status_code, 400)
        response = self.app.get('/calc/log10/-10')
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
