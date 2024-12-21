#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines a class class-checking function."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-21"
__version__ = "1.1"


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance or an inherited instance of a class.

    Args_:
        obj (any): The object to evaluate.
        a_class (type): The class to check against.

    Returns_:
        bool: True if the object is an instance or an inherited instance
              of the specified class, False otherwise.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

    if is_kind_of_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))

    if is_kind_of_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
