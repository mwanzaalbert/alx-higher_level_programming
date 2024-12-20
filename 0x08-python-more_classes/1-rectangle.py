#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module defines the `Rectangle` class.

The class models a rectangle with properties for width and height,
including validation.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-20"
__version__ = "1.0"


class Rectangle:
    """
    A class to represent a rectangle with width and height.

    Attributes_:
        width (int): The width of the rectangle,
                     must be a non-negative integer

        height (int): The height of the rectangle,
                      must be a non-negative integer
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args_:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises_:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns_:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args_:
            value (int): The new width of the rectangle.
                         Must be a non-negative integer.

        Raises_:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns_:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args_:
            value (int): The new height of the rectangle.
                         Must be a non-negative integer.

        Raises_:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
