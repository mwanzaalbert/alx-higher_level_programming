#!/usr/bin/python3

def islower(c):
    """
    Check if a character is lowercase.

    Args:
    - c: a character (string of length 1)

    Returns:
    - True if c is lowercase
    - False otherwise
    """
    if len(c) != 1:
        return False  # c must be a string of length 1
    else:
        char_code = ord(c)  # get the Unicode code point of the character
        return char_code >= 97 and char_code <= 122  # lowercase letters have Unicode codes in the range [97, 122]

