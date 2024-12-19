#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module: say_my_name.

This module contains a single function, `say_my_name`, which prints a full name
based on the provided first and last name arguments. It ensures the inputs are
strings and handles cases where the last name is not provided.

Functions:
----------
- say_my_name(first_name, last_name=""): Prints the full name of a person,
  ensuring the inputs are valid strings.

Exceptions:
-----------
- Raises `TypeError` if `first_name` or `last_name` is not a string.

Usage:
------
Call `say_my_name` with the required `first_name` argument and an optional
`last_name` argument to print the full name:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Alice")
    My name is Alice
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-19"
__version__ = "1.1"


def say_my_name(first_name, last_name=""):
    """
    Print a person's name in the format "My name is <first_name> <last_name>".

    Parameters_:
    -----------
    first_name : str
        The first name of the person. This is a required argument.
    last_name : str, optional
        The last name of the person. Defaults to an empty string.

    Raises_:
    -------
    TypeError
        If `first_name` or `last_name` is not of type `str`.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
