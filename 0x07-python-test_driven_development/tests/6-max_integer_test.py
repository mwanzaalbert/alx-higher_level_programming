#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for the function def max_integer(list=[])"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([7, -2, 5]), 7)
        self.assertEqual(max_integer([7, 10, 5]), 10)
        self.assertEqual(max_integer([-1, -5, -7]), -1)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([]), None)
