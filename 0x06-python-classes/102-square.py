#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Define a class Square with comparison operators' overloading methods."""

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

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

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

    def area(self):
        """Return the calculated area of the square instance."""
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Determine if two Square instances are equal in area.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the areas of both squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Determine if two Square instances are not equal in area.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the areas of both squares are not equal,
                  False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Determine if current Square instance is smaller in area than another.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the current square's area is less than the other
                  square's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Determine if Square instance is less than or equal to another in area.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the current square's area is less than or equal to
                  the other square's area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Determine if the Square instance is larger in area than another.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the current square's area is greater than the
                  other square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Determine if Square instance's larger than or equal to another in area.

        Args_:
            other (Square): Another Square instance to compare.

        Returns_:
            bool: True if the current square's area is greater than or
                  equal to the other square's area, False otherwise.
        """
        return self.area() >= other.area()


# Test Code
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
