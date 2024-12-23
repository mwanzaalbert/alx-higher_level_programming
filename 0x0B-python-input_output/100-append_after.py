#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Text search and insertion function module.

This module provides a function to insert text into a file after lines
containing a specified string.

The primary function, `append_after`, allows users to search for a specific
string in a text file and insert new text immediately after each line where
the search string appears. This can be useful for adding annotations,
comments, or other content dynamically to files.

Functions:
    append_after(filename, search_string, new_string):
        Inserts text after each line containing a given string in a file.

Usage Example:
    To insert the text '"C is fun!"\n' after every line containing "Python" in
    the file `append_after_100.txt`, run:

        append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

    This will modify the file in place, adding the new text after the matching
    lines.

Notes:
    - The file is opened and rewritten in place, so ensure you have a backup
    if the original file is critical.
    - The encoding used for reading and writing the file is UTF-8.
"""


def append_after(filename, search_string, new_string):
    """
    Insert text after each line containing a given string in a file.

    Args_:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each matching line.
    """
    with open(filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Rewrite the file with inserted text
    with open(filename, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
            if search_string in line:
                outfile.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
