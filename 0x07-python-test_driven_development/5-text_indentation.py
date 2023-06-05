#!/usr/bin/python3
"""
Print a text with 2 new lines after
each of these characters
. ? :
"""


def text_indentation(text):

    flag = True
    delimiters = ['?', '.', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in text:
        if ch == ' ' and flag is True:
            continue

        if ch in delimiters:
            print("{}".format(ch), end="")
            print("\n")
            flag = True
        else:
            print(ch, end="")
            flag = False
