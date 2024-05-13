#!/usr/bin/env python3
"""Unit tests for utility functions"""

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json

class TestAccessNestedMap(TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_outcome):
        """Test access_nested_map function"""
        actual_outcome = access_nested_map(nested_map, path)
        self.assertEqual(actual_outcome, expected_outcome)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expctd_msg):
        """Test access_nested_map function for KeyError"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(expctd_msg, context.exception)


class TestGetJson(TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function"""

        # Mock the return value of requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        with patch('requests.get', return_value=mock_response):
            # Call the get_json function
            actual_response = get_json(test_url)
            # Assert that the actual_response is equal to test_payload
            self.assertEqual(actual_response, test_payload)
            mock_response.json.assert_called_once()
