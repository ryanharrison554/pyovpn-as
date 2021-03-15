"""Tests functions in the pyovpn_as.client module
"""
import unittest
import unittest.mock

from pyovpn_as import client


class TestValidateEndpoint(unittest.TestCase):
    """TestCase for the validate_endpoint function
    """

    def test_valid_endpoint_returns_true(self):
        endpoint = 'https://ip-address/RPC2/'
        self.assertTrue(client.validate_endpoint(endpoint))

    def test_http_scheme_returns_false(self):
        endpoint = 'http://ip-address/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_ftp_scheme_returns_false(self):
        endpoint = 'ftp://ip-address/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_username_in_netloc_returns_false(self):
        endpoint = 'https://username@ip-address/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_passsword_in_netloc_returns_false(self):
        endpoint = 'https://:password@ip-address/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_only_userpass_in_netloc_returns_false(self):
        endpoint = 'https://username:password@/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_blank_netloc_returns_false(self):
        endpoint = 'https:///RPC2/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_get_query_returns_false(self):
        endpoint = 'https://ip-address/?param=val'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_parameters_returns_false(self):
        endpoint = 'https://ip-address/RPC2;param=val'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_fragments_returns_false(self):
        endpoint = 'https://ip-address/#fragment'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_valid_port_number_returns_true(self):
        endpoint = 'https://ip-address:443/'
        self.assertTrue(client.validate_endpoint(endpoint))

    def test_high_port_number_returns_false(self):
        endpoint = 'https://ip-address:65536/'
        self.assertFalse(client.validate_endpoint(endpoint))

    def test_negative_port_number_returns_false(self):
        endpoint = 'https://ip-address:-1/'
        self.assertFalse(client.validate_endpoint(endpoint))

