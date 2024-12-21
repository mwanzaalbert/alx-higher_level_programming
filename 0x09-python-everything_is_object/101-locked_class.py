#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
LockedClass module.

This module defines the LockedClass, a class that restricts the user
from dynamically creating new instance attributes except for
`first_name`.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-21"
__version__ = "1.1"


class LockedClass:
    """
    Prevent dynamic creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """Initialize a LockedClass instance."""
        pass


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
