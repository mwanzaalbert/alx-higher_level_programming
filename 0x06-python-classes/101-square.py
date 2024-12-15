#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Define a class Square with string representation method."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-15"
__version__ = "1.1"


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args_:
            size: represnets the size of the square defined
        Raises_:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if (
                not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size

        self.__position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            # print()
            return

        # Print the vertical spacing
        for _ in range(self.__position[1]):
            print()

        # Print the square
        for index in range(self.__size):

            if index == self.__size - 1:
                print(" " * self.__position[0] + "#" * self.__size, end="")
            else:
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """State representation of a Square instance."""
        self.my_print()

        return ''


if __name__ == '__main__':
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
    print("--")

    my_square = Square(0, (10, 10))
    print(my_square)
    print("--")
