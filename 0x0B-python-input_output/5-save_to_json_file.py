#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module: json_file_writer.

Description:
    Provides a function to write a Python object to a text file in JSON format.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

import json
from typing import Any


def save_to_json_file(my_obj: Any, filename: str) -> None:
    """
    Write a Python object to a text file using its JSON representation.

    Parameters_:
    - my_obj (Any): The Python object to be serialized and written to the file.
    - filename (str): The name of the file where the JSON data will be saved.

    Returns_:
    - None

    Example_:
        >>> save_to_json_file({"name": "Alice", "age": 30}, "data.json")
        # The file 'data.json' will contain:
        # {"name": "Alice", "age": 30}
    """
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)


if __name__ == "__main__":
    filename = "json_files/my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "json_files/my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }

    save_to_json_file(my_dict, filename)

    try:
        filename = "json_files/my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
