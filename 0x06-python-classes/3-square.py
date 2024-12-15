#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Define a class Square."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-15"
__version__ = "1.1"


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args_:
            size: represnets the size of the square defined
        Raises_:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)


# Test Code
if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
