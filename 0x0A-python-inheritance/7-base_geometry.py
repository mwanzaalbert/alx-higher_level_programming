#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
BaseGeometry module.

This module defines an abstract base class, `BaseGeometry`, which serves as a
foundation for geometric shapes. It includes a method `area` to compute the
area of a shape, designed to be implemented by subclasses, and an
`integer_validator` method to validate input values.

Features_:
---------
- **BaseGeometry Class**:
    - Provides a blueprint for geometric shapes.
    - Implements methods that must be extended or used by derived classes.

Public Methods_:
---------------
- `area()`:
    - Raises an exception, acting as a placeholder for subclasses to override.
- `integer_validator(name, value)`:
    - Validates that a parameter is an integer greater than 0.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


class BaseGeometry:
    """Abstract base class for geometric shapes."""

    def area(self):
        """
        Compute the area of a shape.

        This method is intended to be overridden by subclasses.

        Raises_:
            Exception: Always raises an exception because it is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as a positive integer.

        Args_:
            name (str): The name of the parameter (for error messages).
            value (int): The parameter to validate.

        Raises_:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
