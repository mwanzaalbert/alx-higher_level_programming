#!/usr/bin/python3

import hidden_4


if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    # Get all names defined by the hidden_4 module
    names = dir(hidden_4)

    # Filter names that do not start with '__'
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort names in alphabetical order
    # filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
