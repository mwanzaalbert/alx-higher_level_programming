#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Square module.

This module defines a Square class that inherits from Rectangle class defined
in 9-rectangle.py.
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using the Rectangle class."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args_:
            size (int): The size of one side of the square.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
