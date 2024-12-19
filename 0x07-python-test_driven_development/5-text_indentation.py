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
    Format the input text by adding two newlines after each `.`, `:`, or `?`.

    Args_:
        text (str): The text to format.

    Raises_:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = {'.', '?', ':'}  # Use a set for faster lookups
    formatted_text = ""
    skip_space = False

    for char in text:
        if skip_space and char.isspace():
            continue
        skip_space = False

        formatted_text += char
        if char in delimiters:
            formatted_text += "\n\n"
            skip_space = True

    print(formatted_text.strip())
