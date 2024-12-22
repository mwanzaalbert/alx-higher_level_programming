#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines function that converts an object to a JSON like frmt."""


__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


class MyClass:
    """
    Represents a simple test class with a name and a number.

    Attributes_:
        name (str): The name of the instance.
        number (int): A numeric attribute initialized to 0.
    """

    def __init__(self, name):
        """
        Initialize a MyClass instance.

        Args_:
            name (str): The name to assign to the instance.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns_:
            str: A formatted string containing the name and number.
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)


class MyClass2:
    """
    Represents a test class with additional functionality for scoring.

    Attributes_:
        score (int): A class attribute representing the score, shared by all
                    instances.
        __name (str): The private name of the instance.
        number (int): A numeric attribute initialized during instance creation.
        is_team_red (bool): Indicates team membership based on the number.
    """

    score = 0

    def __init__(self, name, number=4):
        """Initialize a MyClass2 instance.

        Args_:
            name (str): The name to assign to the instance.
            number (int, optional): The numeric attribute (default is 4).
        """
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        """Increment the score by 1."""
        self.score += 1

    def lose(self):
        """Decrement the score by 1."""
        self.score -= 1

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns_:
            str: A formatted string containing the private name, number,
                and score.
        """
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number,
                                                    self.score)


def class_to_json(obj):
    """
    Convert an object's attributes to a dictionary.

    Args_:
        obj (object): The object to convert.

    Returns_:
        dict: A dictionary containing the object's attributes.
    """
    return obj.__dict__


if __name__ == "__main__":
    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    print('\n=====\n')
    m = MyClass2("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
