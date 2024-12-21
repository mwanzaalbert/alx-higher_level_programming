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

    # try:
    #     a = "My String"
    #     add_attribute(a, "name", "Bob")
    #     print(a.name)
    # except Exception as e:
    #     # Output: [TypeError] can't add new attribute
    #     print("[{}] {}".format(e.__class__.__name__, e))

    # add_attribute(mc, "age", "30")
    # print(mc.age)

    # try:
    #     a = "My String"
    #     add_attribute(mc, "age", "40")
    #     print(a.name)
    # except Exception as e:
    #     # Output: [TypeError] can't add new attribute
    #     print("[{}] {}".format(e.__class__.__name__, e))
