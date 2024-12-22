#!/usr/bin/python3

"""
Module: json_file_reader.

Description:
    Provides a function to read a JSON file and convert its content into a
    Python object.
"""

import json
from typing import Any


def load_from_json_file(filename: str) -> Any:
    """
    Read a JSON file and creates a Python object from its contents.

    Parameters_:
    - filename (str): The name of the file containing JSON data.

    Returns_:
    - Any: The Python object represented by the JSON data in the file.

    Example_:
        If the file 'data.json' contains:
        {"name": "Alice", "age": 30}

        >>> load_from_json_file("data.json")
        {'name': 'Alice', 'age': 30}
    """
    with open(filename, "r") as infile:
        return json.load(infile)


if __name__ == "__main__":
    filename = "json_files/my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "json_files/my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "json_files/my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "json_files/my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
