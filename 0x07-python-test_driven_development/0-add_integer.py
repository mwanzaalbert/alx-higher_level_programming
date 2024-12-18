#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The following module defines a function `add_integer` that adds two numbers.

Functionality:
---------------
- The `add_integer` function takes two parameters:
  - `a`: The first number to be added. It must be an integer or float.
  - `b`: The second number to be added. It must be an integer or float.
         Defaults to 98 if not provided.

- The function performs type validation:
  - If either `a` or `b` is not an integer or float, it raises a `TypeError`
    with an appropriate error message.
  - If either value is a float, it is cast to an integer before performing the
    addition.

- The function handles corner cases such as missing arguments, invalid types,
 and floats with large values (e.g., infinity).


"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-18"
__version__ = "1.1"


def add_integer(a, b=98):
    """
    Add two integers.

    This function takes two arguments and returns their sum. If one or both
    arguments are floats, they are cast to integers before addition. The second
    argument is optional and defaults to 98.

    Args_:
        a (int or float): The first number to add. Must be an integer or float.
        b (int or float, optional): The second number to add.
                                    Must be an integer or float.
                                    Defaults to 98.

    Returns_:
        int: The sum of `a` and `b` after casting both to integers (if needed).

    Raises_:
        TypeError: If `a` or `b` is not an integer or float.
        OverflowError: If a float arg. is too large to convert to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
