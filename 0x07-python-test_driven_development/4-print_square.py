#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module: print_square.

This module defines a single function, `print_square`, which prints a square
made of the `#` character. The size of the square is determined by the input
parameter `size`. The function validates the input to ensure it is a
non-negative integer.

Functions:
----------
- print_square(size): Prints a square of a specified size using the `#`
  character.

Exceptions:
-----------
- Raises `TypeError` if `size` is not an integer.
- Raises `ValueError` if `size` is a negative integer.

"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-19"
__version__ = "1.1"


def print_square(size):
    """
    Print a square of `#` characters of the given size.

    Parameters_:
    -----------
    size : int
        The size of the square (number of rows and columns).
        Must be a non-negative integer.

    Raises_:
    -------
    TypeError
        If `size` is not an integer.
    ValueError
        If `size` is a negative integer.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
