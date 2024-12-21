#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines an inheritance class-checking function."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-21"
__version__ = "1.1"


def inherits_from(obj, a_class):
    """
    Inheritance class-checking function.

    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args_:
        obj (any): The object to evaluate.
        a_class (type): The class to check inheritance against.

    Returns_:
        bool: True if the object is an instance of a class that
              inherits from the specified class; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
