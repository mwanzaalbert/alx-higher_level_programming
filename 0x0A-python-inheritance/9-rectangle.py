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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns_:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of a Rectangle.

        Returns_:
            str: A string in the format [Rectangle] width/height.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
