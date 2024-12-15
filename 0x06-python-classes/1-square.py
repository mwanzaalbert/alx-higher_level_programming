#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Define a class Square with a constructor method."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-15"
__version__ = "1.1"


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
