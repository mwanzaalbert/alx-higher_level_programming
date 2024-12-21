#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines a function to add a new attribute to an object."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if possible.

    Args_:
        obj (object): The object to which the attribute will be added.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises_:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)


if __name__ == "__main__":
    class MyClass():
        """Empty class."""

        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)  # Output: John

    # raises an exception
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
