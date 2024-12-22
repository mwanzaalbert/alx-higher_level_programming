#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Module: add_items_to_json.

Description:
    Adds command-line arguments to a JSON file as a list. If the file doesn't
    exist, it creates one.

Dependencies:
- 5-save_to_json_file
- 6-load_from_json_file
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

import os
import sys
from typing import List, Any

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_or_modify_json_file(filename: str, items_to_add: List[Any]) -> None:
    """
    Create or modify JSON file.

    Add a list of items to an existing JSON file, or creates a new JSON file
    if it doesn't exist.

    Parameters_:
    - filename (str): The path to the JSON file.
    - items_to_add (List[Any]): A list of items to add to the JSON file.

    Returns_:
    - None
    """
    if os.path.exists(filename):
        # Load existing data from the file
        data = load_from_json_file(filename)

        # Extend the existing list with new items
        data.extend(items_to_add)
    else:
        # If the file doesn't exist, initialize with the provided items
        data = items_to_add

    # Save the updated list back to the file
    save_to_json_file(data, filename)


if __name__ == "__main__":
    # Define the target JSON file
    file_name = "add_item.json"

    # Get command-line arguments, excluding the script name
    args = sys.argv[1:]

    # Add arguments to the JSON file
    try:
        add_to_or_modify_json_file(file_name, args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
