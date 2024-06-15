import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '4', f"Resultado incorrecto en la petición API a {url}")

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '2', f"Resultado incorrecto en la petición API a {url}")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '12', f"Resultado incorrecto en la petición API a {url}")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '5.0', f"Resultado incorrecto en la petición API a {url}")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '8', f"Resultado incorrecto en la petición API a {url}")

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '4.0', f"Resultado incorrecto en la petición API a {url}")

    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode()
        self.assertEqual(result, '2.0', f"Resultado incorrecto en la petición API a {url}")

    def test_api_log10_non_positive(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        url = f"{BASE_URL}/calc/log10/-10"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
