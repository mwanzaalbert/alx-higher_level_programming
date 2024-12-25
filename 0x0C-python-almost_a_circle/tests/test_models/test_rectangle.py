#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Test Suites for the Rectangle class model."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-25"
__version__ = "1.1"

import unittest
import io
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects before each test."""
        Rectangle._Base__nb_objects = 0

    def test_inheritance(self):
        """Test that the Rectangle class exists and inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instance_creation(self):
        """
        Test creating a rectangle instances with positional args
        and optional args.
        """
        r1 = Rectangle(10, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 12)

        r2 = Rectangle(10, 12, 2)
        self.assertEqual(r2.x, 2)

        r3 = Rectangle(10, 12, 2, 3)
        self.assertEqual(r3.y, 3)

        r4 = Rectangle(10, 12, 2, 3, 42)
        self.assertEqual(r4.id, 42)

    def test_getters_and_setters(self):
        """Test setting and accessing of instance properties."""
        r = Rectangle(10, 12)

        r.width = 20
        self.assertEqual(r.width, 20)

        r.height = 15
        self.assertEqual(r.height, 15)

        r.x = 5
        self.assertEqual(r.x, 5)

        r.y = 6
        self.assertEqual(r.y, 6)

    def test_type_errors(self):
        """Test validation of args during instantiantion."""
        with self.assertRaises(TypeError):
            Rectangle("10", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, "12")
        with self.assertRaises(TypeError):
            Rectangle(10, 12, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 2, "3")

        r = Rectangle(10, 12)
        with self.assertRaises(TypeError):
            r.width = "20"
        with self.assertRaises(TypeError):
            r.height = "15"
        with self.assertRaises(TypeError):
            r.x = "5"
        with self.assertRaises(TypeError):
            r.y = "6"

    def test_value_errors(self):
        """Test validation of args during instantiantion."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, -12)
        with self.assertRaises(ValueError):
            Rectangle(10, 12, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 12, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        r = Rectangle(10, 12)
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.x = -5
        with self.assertRaises(ValueError):
            r.y = -6

    def test_area(self):
        """Test calculation of areas."""
        r1 = Rectangle(10, 12)
        self.assertEqual(r1.area(), 120)

        r2 = Rectangle(12, 10)
        self.assertEqual(r2.area(), 120)

        r3 = Rectangle(10, 10)
        self.assertEqual(r3.area(), 100)

    def test_display(self):
        """Test shape display in stdout."""
        r1 = Rectangle(3, 2)
        expected_output = "###\n###\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test state representation of an instance."""
        r1 = Rectangle(10, 12, 3, 6, 8)
        self.assertEqual(str(r1), "[Rectangle] (8) 3/6 - 10/12")

    def test_update_args(self):
        """Test updating of an instance using variadic length args."""
        r = Rectangle(10, 12, 2, 3, 42)
        r.update(24)
        self.assertEqual(r.id, 24)
        r.update(24, 20)
        self.assertEqual(r.width, 20)
        r.update(24, 20, 15)
        self.assertEqual(r.height, 15)
        r.update(24, 20, 15, 5)
        self.assertEqual(r.x, 5)
        r.update(24, 20, 15, 5, 6)
        self.assertEqual(r.y, 6)

    def test_update_kwargs(self):
        """Test updating of an instance using kwargs."""
        r = Rectangle(10, 12, 2, 3, 42)
        r.update(id=24)
        self.assertEqual(r.id, 24)
        r.update(width=20)
        self.assertEqual(r.width, 20)
        r.update(height=15)
        self.assertEqual(r.height, 15)
        r.update(x=5)
        self.assertEqual(r.x, 5)
        r.update(y=6)
        self.assertEqual(r.y, 6)


class TestRectangleAdditional(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects before each test."""
        Rectangle._Base__nb_objects = 0

    def test_boundary_values(self):
        """Test boundary values for width, height, x, and y."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 2, 0, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_invalid_update_args(self):
        """Test update method with invalid *args."""
        r = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            r.update("12", 5, 6, 7, 8)  # id must be an integer
        with self.assertRaises(ValueError):
            r.update(12, -1, 6, 7, 8)  # width must be > 0
        with self.assertRaises(ValueError):
            r.update(12, 5, 6, -7, 8)  # x must be >= 0

    def test_invalid_update_kwargs(self):
        """Test update method with invalid **kwargs."""
        r = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            r.update(id="12", width=5, height=6)  # id must be an integer
        with self.assertRaises(ValueError):
            r.update(width=-5)  # width must be > 0
        with self.assertRaises(ValueError):
            r.update(x=-3)  # x must be >= 0

    def test_partial_update_args(self):
        """Test update method with partial *args."""
        r = Rectangle(10, 10)
        r.update(12, 5)  # Update only id and width
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)  # Height remains unchanged

    def test_default_values(self):
        """Test default values for x and y."""
        r = Rectangle(10, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_combined_valid_and_invalid_kwargs(self):
        """Test update method with a mix of valid and invalid kwargs."""
        r = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r.update(width=5, height=-10)  # height must be > 0

        # Ensure width wasn't updated due to error
        self.assertEqual(r.width, 10)

    def test_error_messages(self):
        """Test error messages in exceptions."""
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 10)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_display_with_offsets(self):
        """Test display method with offsets."""
        r = Rectangle(3, 2, 1, 2)
        expected_output = "\n\n ###\n ###\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_string_representation_edge_cases(self):
        """Test string representation with edge cases."""
        r = Rectangle(1000, 2000, 300, 400, 9999)
        self.assertEqual(str(r), "[Rectangle] (9999) 300/400 - 1000/2000")

    def test_immutability_of_private_attributes(self):
        """Test immutability of private attributes."""
        r = Rectangle(10, 20)

        # This creates a new attribute
        r.__height = 30  # but doesn't modify _Rectangle__height
        r.__width = 40   # Same for __width
        # r.__height is a new attribute

        self.assertNotEqual(r.__height, r.height)
        # Original height remains unchanged
        self.assertEqual(r.height, 20)
        # Original width remains unchanged
        self.assertEqual(r.width, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Unit tests for the to_dictionary method of the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Rectangle._Base__nb_objects = 0

    def test_has_to_dictionary_method(self):
        """Test if the to_dictionary method exists."""
        r = Rectangle(10, 20)
        self.assertTrue(hasattr(r, "to_dictionary")
                        and callable(r.to_dictionary))

    def test_to_dictionary_returns_dict(self):
        """Test if to_dictionary returns a dictionary."""
        r = Rectangle(10, 20)
        result = r.to_dictionary()
        self.assertIsInstance(result, dict)

    def test_to_dictionary_contains_exactly_5_keys(self):
        """Test if the returned dictionary has exactly 5 keys."""
        r = Rectangle(10, 20, 1, 2, 42)
        result = r.to_dictionary()
        self.assertEqual(len(result), 5)

    def test_to_dictionary_contains_id(self):
        """Test if the returned dictionary contains the id key."""
        r = Rectangle(10, 20, 1, 2, 42)
        result = r.to_dictionary()
        self.assertIn("id", result)
        self.assertEqual(result["id"], 42)

    def test_to_dictionary_contains_width(self):
        """Test if the returned dictionary contains the width key."""
        r = Rectangle(10, 20)
        result = r.to_dictionary()
        self.assertIn("width", result)
        self.assertEqual(result["width"], 10)

    def test_to_dictionary_contains_height(self):
        """Test if the returned dictionary contains the height key."""
        r = Rectangle(10, 20)
        result = r.to_dictionary()
        self.assertIn("height", result)
        self.assertEqual(result["height"], 20)

    def test_to_dictionary_contains_x(self):
        """Test if the returned dictionary contains the x key."""
        r = Rectangle(10, 20, 1)
        result = r.to_dictionary()
        self.assertIn("x", result)
        self.assertEqual(result["x"], 1)

    def test_to_dictionary_contains_y(self):
        """Test if the returned dictionary contains the y key."""
        r = Rectangle(10, 20, 1, 2)
        result = r.to_dictionary()
        self.assertIn("y", result)
        self.assertEqual(result["y"], 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
