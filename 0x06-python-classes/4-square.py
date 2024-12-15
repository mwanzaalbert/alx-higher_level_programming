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

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the calculated area of the square instance."""
        return (self.__size * self.__size)


# Test Code
if __name__ == '__main__':
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(),
                                         my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(),
                                         my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(),
                                             my_square.size))
    except Exception as e:
        print(e)
