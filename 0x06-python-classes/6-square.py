#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Define a class Square with coordinates setter and getter methods."""

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
        if self.__size:
            for _ in range(self.__size):
                print(" " * self.__position[0], end='')
                # print("_" * self.__position[0] if self.__position[1]
                #       else "_" * self.__position[0], end='')
                # (print("_" * self.__position[1], end='')if self.__position[1]
                #  else print("_" * self.__position[0], end=''))
                # if self.__position[1]:
                #     for _ in range(self.__position[1]):
                #         print("_", end="")
                # else:
                #     for _ in range(self.__position[0]):
                #         print("_", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()


if __name__ == '__main__':
    try:
        my_square = Square(3, "Position")
    except Exception as e:
        print(e)

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

    my_square = Square(5, (3, 2))
    my_square.my_print()
    print("--")
