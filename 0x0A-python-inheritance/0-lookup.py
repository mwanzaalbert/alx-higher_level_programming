#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines an object attribute lookup function."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-21"
__version__ = "1.1"


def lookup(obj) -> list:
    """
    Return a list of an object's available attributes and methods.

    Args_:
        obj (Any): The object whose attributes and methods are to be retrieved.

    Returns_:
        List[str]: A list of names of the object's attributes and methods.
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        """Empty class."""

        pass

    class MyClass2(object):
        """A class with attributes."""

        my_attr1 = 3

        def my_meth(self):
            """Define a class method."""
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
