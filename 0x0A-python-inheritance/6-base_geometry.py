#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
BaseGeometry module.

This module defines an abstract base class BaseGeometry. The class contains
a public instance method `area()` that raises an exception with the message
'area() is not implemented'. This serves as a placeholder to be overridden
by subclasses that represent specific geometric shapes.

An empty class BaseGeometry is also provided to serve as a foundation for
other geometric shapes.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


class BaseGeometry:
    """Abstract class for geometric shapes."""

    def area(self):
        """
        Compute the area of a shape.

        Raises_:
            Exception: Always raises an exception because this method
            is not implemented in the base class.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    # Create an instance of BaseGeometry
    bg = BaseGeometry()

    try:
        # Attempt to call the area method, which will raise an exception
        print(bg.area())
    except Exception as e:
        # Print the exception details
        print("[{}] {}".format(e.__class__.__name__, e))
