#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Rectangle module.

This module defines a Rectangle class that inherits from BaseGeometry.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle instance.

        Args_:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width

        self.__height = height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
