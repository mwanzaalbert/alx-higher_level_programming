#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Test Suites for the Square class model."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-25"
__version__ = "1.1"

import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Square._Base__nb_objects = 0

    def test_class_exists_and_inherits_rectangle(self):
        """Test that the Square class exists and inherits from Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_create_square_with_size(self):
        """Test creating a square with only size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_create_square_with_size_and_x(self):
        """Test creating a square with size and x."""
        s = Square(5, 7)
        self.assertEqual(s.x, 7)

    def test_create_square_with_size_x_and_y(self):
        """Test creating a square with size, x, and y."""
        s = Square(5, 7, 2)
        self.assertEqual(s.y, 2)

    def test_create_square_with_all_attributes(self):
        """Test creating a square with size, x, y, and id."""
        s = Square(5, 7, 2, 89)
        self.assertEqual(s.id, 89)

    def test_str_overloaded(self):
        """Test that __str__ is overloaded."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_area_method(self):
        """Test the area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display_method(self):
        """Test the display method."""
        s = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update_args(self):
        """Test the update method with *args."""
        s = Square(5, 1, 2, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 6)
        self.assertEqual(s.size, 6)
        s.update(89, 6, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 6, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s = Square(5, 1, 2, 10)
        s.update(id=89)
        self.assertEqual(s.id, 89)
        s.update(id=89, size=8)
        self.assertEqual(s.size, 8)
        s.update(id=89, size=8, x=3)
        self.assertEqual(s.x, 3)
        s.update(id=89, size=8, x=3, y=4)
        self.assertEqual(s.y, 4)

    def test_size_getter_and_setter(self):
        """Test the getter and setter for size."""
        s = Square(5)
        s.size = 12
        self.assertEqual(s.size, 12)
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 12)

    def test_size_setter_raises_typeerror(self):
        """Test setting size raises TypeError."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "12"

    def test_size_setter_raises_valueerror(self):
        """Test setting size raises ValueError."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -12

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(5, 2, 1, 10)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(len(d), 4)
        self.assertIn("id", d)
        self.assertIn("size", d)
        self.assertIn("x", d)
        self.assertIn("y", d)
        self.assertEqual(d["id"], 10)
        self.assertEqual(d["size"], 5)
        self.assertEqual(d["x"], 2)
        self.assertEqual(d["y"], 1)


class TestSquareAdditional(unittest.TestCase):
    """Additional unittests for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Square._Base__nb_objects = 0

    def test_boundary_values(self):
        """Test boundary values for size, x, and y."""
        s = Square(1, 0, 0)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_invalid_update_args(self):
        """Test update method with invalid *args."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update("12")  # id must be an integer
        with self.assertRaises(ValueError):
            s.update(12, -1)  # size must be > 0
        with self.assertRaises(ValueError):
            s.update(12, 5, -1)  # x must be >= 0
        with self.assertRaises(ValueError):
            s.update(12, 5, 1, -1)  # y must be >= 0

    def test_invalid_update_kwargs(self):
        """Test update method with invalid **kwargs."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(id="12", size=5)  # id must be an integer
        with self.assertRaises(ValueError):
            s.update(size=-5)  # size must be > 0
        with self.assertRaises(ValueError):
            s.update(x=-3)  # x must be >= 0
        with self.assertRaises(ValueError):
            s.update(y=-3)  # y must be >= 0

    def test_partial_update_args(self):
        """Test update method with partial *args."""
        s = Square(5)
        s.update(12, 8)  # Update id and size
        self.assertEqual(s.id, 12)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 0)  # x remains unchanged
        self.assertEqual(s.y, 0)  # y remains unchanged

    def test_default_values(self):
        """Test default values for x and y."""
        s = Square(10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_combined_valid_and_invalid_kwargs(self):
        """Test update method with a mix of valid and invalid kwargs."""
        s = Square(10)
        with self.assertRaises(ValueError):
            s.update(size=5, y=-10)  # y must be >= 0
        self.assertEqual(s.size, 10)  # Ensure size wasn't updated due to error

    def test_immutability_of_private_attributes(self):
        """Test immutability of private attributes."""
        s = Square(10)

        # This creates a new attribute but doesn't modify _Square__size
        s.__size = 20
        self.assertNotEqual(s.__size, s.size)  # s.__size is a new attribute
        self.assertEqual(s.size, 10)  # Original size remains unchanged


class TestSquareEdgeCases(unittest.TestCase):
    """Unittests for additional edge cases in Square."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Square._Base__nb_objects = 0

    def test_negative_x_or_y(self):
        """Test creating or updating Square with negative x or y."""
        with self.assertRaises(ValueError):
            Square(5, -1, 2)
        with self.assertRaises(ValueError):
            Square(5, 1, -2)
        s = Square(5)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-2)

    def test_large_id_values(self):
        """Test creating a Square with very large id values."""
        s = Square(5, 0, 0, 2**63 - 1)
        self.assertEqual(s.id, 2**63 - 1)

    def test_float_inputs(self):
        """Test creating or updating Square with float values."""
        with self.assertRaises(TypeError):
            Square(5.5)
        with self.assertRaises(TypeError):
            Square(5, 7.7)
        with self.assertRaises(TypeError):
            Square(5, 7, 2.2)
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(size=5.5)

    def test_id_reuse(self):
        """Test reusing the same id across multiple Square objects."""
        s1 = Square(5, 0, 0, 1)
        s2 = Square(10, 1, 1, 1)
        self.assertEqual(s1.id, s2.id)

    def test_empty_update(self):
        """Test calling update with no arguments or keyword arguments."""
        s = Square(5, 1, 2, 10)
        s.update()
        self.assertEqual(s.to_dictionary(), {
                         "id": 10, "size": 5, "x": 1, "y": 2})

    def test_invalid_to_dictionary_return(self):
        """Test behavior if to_dictionary returns invalid data."""
        class InvalidSquare(Square):
            def to_dictionary(self):
                return {"id": self.id}  # Missing keys

        s = InvalidSquare(5, 1, 2, 10)
        d = s.to_dictionary()
        self.assertNotIn("size", d)
        self.assertNotIn("x", d)
        self.assertNotIn("y", d)

    def test_update_size_to_zero(self):
        """Test updating size to 0 directly or via update."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.update(size=0)

    def test_mutability_of_to_dictionary_output(self):
        """
        Test modifying the output of to_dictionary doesn't affect the object.
        """
        s = Square(5, 2, 1, 10)
        d = s.to_dictionary()
        d["size"] = 99
        self.assertEqual(s.size, 5)

    def test_display_with_large_x_y(self):
        """Test display with large x or y values."""
        s = Square(2, 10, 5)
        expected_output = "\n\n\n\n\n          ##\n          ##\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)


class TestSquareAdditionalEdgeCases(unittest.TestCase):
    """Additional unittests for missed edge cases in Square."""

    def setUp(self):
        """Set up for test methods"""
        self.square_csv = "Square.json"
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove(self.square_csv)
        except FileNotFoundError:
            pass

    def test_create_square_with_non_integer_inputs(self):
        """Test creating a square with non-integer inputs."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(TypeError):
            Square(5, "7")
        with self.assertRaises(TypeError):
            Square(5, 7, "2")

    def test_create_square_with_zero_or_negative_size(self):
        """Test creating a square with zero or negative size."""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size_setter_updates_width_and_height(self):
        """Test that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_to_dictionary_after_update(self):
        """Test to_dictionary reflects updates in attributes."""
        s = Square(5, 2, 1, 10)
        s.size = 8
        s.x = 3
        s.y = 4
        d = s.to_dictionary()
        self.assertEqual(d["size"], 8)
        self.assertEqual(d["x"], 3)
        self.assertEqual(d["y"], 4)

    def test_update_with_invalid_keyword_arguments(self):
        """Test update method with invalid **kwargs."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.update(invalid_key=123)  # Should not affect the object
        self.assertEqual(s.size, 5)

    def test_str_with_edge_cases(self):
        """Test __str__ with edge cases."""
        s = Square(10, 0, 0, 9999)
        self.assertEqual(str(s), "[Square] (9999) 0/0 - 10")

    def test_integration_with_base_methods(self):
        """Test integration of Square with Base methods."""
        s1 = Square(5, 2, 1, 10)
        s2 = Square(7, 0, 0, 11)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(squares[1].to_dictionary(), s2.to_dictionary())

    def test_clone_square(self):
        """Test deep copying of a Square object."""
        import copy
        s1 = Square(5, 2, 1, 10)
        s2 = copy.deepcopy(s1)
        self.assertNotEqual(id(s1), id(s2))
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        s2.size = 10
        self.assertNotEqual(s1.size, s2.size)


if __name__ == "__main__":
    unittest.main(verbosity=2)
