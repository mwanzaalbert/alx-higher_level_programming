#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module defines the `Rectangle` class.

The class models a rectangle with properties for width and height,
methods to calculate its area and perimeter, string representations
for debugging and printing and deleting a Rectangle instance.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-20"
__version__ = "1.1"


class Rectangle:
    """
    A class to represent a rectangle with width and height.

    Attributes_:
        number_of_instances (int): The number of Rectangle instances created.

        width (int): The width of the rectangle,
                     must be a non-negative integer

        height (int): The height of the rectangle,
                      must be a non-negative integer
    """

    number_of_instances = 0

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

        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns_:
            int: The area of the rectangle (width × height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns_:
            int: The perimeter of the rectangle (2 × (width + height)).
                 Returns 0 if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return the printable representation of the rectangle.

        The rectangle is represented using the `#` character,
        with each row corresponding to the height and each column
        corresponding to the width.

        Returns_:
            str: A string representation of the rectangle, or an empty
                 string if the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return the official string representation of the rectangle.

        The string representation can be used to recreate a new `Rectangle`
        object with the same attributes.

        Returns_:
            str: A string in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Decrement the `number_of_instances` class attribute.

        Print a message when a Rectangle instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
