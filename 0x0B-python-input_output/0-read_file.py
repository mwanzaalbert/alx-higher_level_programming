#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module defines a text file-reading function.

The function reads and prints the contents of a UTF-8 encoded txt file.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Args_:
        filename (str): The path to the file to read. Defaults to an empty
                        string.
    """
    with open(filename, encoding="utf-8") as infile:
        data = infile.read()
        print(data)


if __name__ == "__main__":
    read_file("txt_files/my_file_0.txt")
