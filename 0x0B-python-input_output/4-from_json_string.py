#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module: json_to_object.

Description_:
    Provides a function to deserialize a JSON string into a Python object.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

import json
from typing import Any


def from_json_string(my_str: str) -> Any:
    """
    Convert a JSON-formatted string into its corresponding Python object.

    Parameters_:
    - my_str (str): A string containing JSON data to be deserialized.

    Returns_:
    - Any: The Python object represented by the JSON string.

    Example_:
        >>> from_json_string('{"name": "Alice", "age": 30}')
        {'name': 'Alice', 'age': 30}
    """
    return json.loads(my_str)


if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14},
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
