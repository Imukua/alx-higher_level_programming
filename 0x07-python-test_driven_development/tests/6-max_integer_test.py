#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case class for the max_integer function"""

    def test_empty_list(self):
        """Test behavior with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test behavior with a list containing a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test behavior with a list of positive numbers"""
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test behavior with a list of negative numbers"""
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test behavior with a list of mixed positive and negative numbers"""
        result = max_integer([-5, 2, -3, 0, 4, -1])
        self.assertEqual(result, 4)
    def test_string(self):
        """Test a string."""
        string = "ianar"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Mukuaa", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
