#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


def print_list_integer(my_list: List[int] = []) -> None:
    """
    Print each integer in a list on a new line.

    Args:
        my_list (List[int]): List of integers to print.

    Raises:
        ValueError: If an element in the list is not an integer.

    Examples:
        >>> print_list_integer([1, 2, 3, 4, 5])
        1
        2
        3
        4
        5

        >>> print_list_integer([])

        >>> print_list_integer([1])
        1

        >>> print_list_integer([1, 2, 3])
        1
        2
        3

        >>> print_list_integer([1, 2, "H", 9])
        Traceback (most recent call last):
            ...
        ValueError: All elements must be integers.
    """
    for i in my_list:
        if not isinstance(i, int):
            raise ValueError("All elements must be integers.")
        print('{:d}'.format(i))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
