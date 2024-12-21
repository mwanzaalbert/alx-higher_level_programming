#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Integer subclassing module.

This module defines the MyInt class, a rebellious integer class.

MyInt inverts the behavior of the equality (`==`) and inequality (`!=`)
operators.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


class MyInt(int):
    """A rebel integer class where `==` and `!=` are inverted."""

    def __eq__(self, other):
        """Override `==` to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override `!=` to invert its behavior."""
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)          # Output: 3
    print(my_i == 3)     # Output: False
    print(my_i != 3)     # Output: True
