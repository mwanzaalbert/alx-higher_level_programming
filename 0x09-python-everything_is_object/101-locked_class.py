#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print(lc.dict)

    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        lc.age = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        lc.test = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
