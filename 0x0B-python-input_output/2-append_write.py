#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines a file-appending function."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF8 text file.

    Args_:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns_:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as outfile:
        return outfile.write(text)


if __name__ == "__main__":
    nb_characters = append_write("txt_files/file_append.txt",
                                 "This School is so cool!\n")
    print(nb_characters)
