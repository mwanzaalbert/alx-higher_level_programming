#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest for max_integer function.

This module contains a collection of test cases to validate the correctness
of the `max_integer` function. The function is designed to find and return
the maximum integer in a list of integers. If the list is empty, the function
returns None.

The test cases cover the following scenarios:
- The maximum integer is at the end of the list.
- The maximum integer is at the beginning of the list.
- The maximum integer is in the middle of the list.
- The list contains one negative number.
- The list contains only negative numbers.
- The list has a single element.
- The list is empty.

Each test case ensures the function behaves as expected under the specified
conditions.
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-19"
__version__ = "1.1"

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer function."""

    def test_max_at_end(self):
        """Test for the maximum integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test for the maximum integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test for the maximum integer in the middle of the list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        """Test for a list with one negative number."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_all_negative_numbers(self):
        """Test for a list with only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test for a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test for an empty list."""
        self.assertIsNone(max_integer([]))
