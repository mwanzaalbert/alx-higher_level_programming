#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
text_indentation module.

This module provides a function to format text by adding two newlines
after each occurrence of specific punctuation characters: '.', ':', and '?'.

Function_:
    text_indentation(text):
        Formats the input text by inserting two newlines after each of the
        specified delimiters ('.', ':', '?'). Consecutive spaces after the
        delimiters are ignored.

Raises_:
    TypeError: If the input is not a string.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-19"
__version__ = "1.1"


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:

    '.', '?', and ':'.

    Args:
        text (str): The text to be processed and printed.

    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters to process
    characters = ".?:"
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            i += 1
            # Skip any spaces after the character
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
