#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module defines a file-writing function."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.

    Args_:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns_:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as outfile:
        return outfile.write(text)


if __name__ == "__main__":
    nb_characters = write_file("txt_files/my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
