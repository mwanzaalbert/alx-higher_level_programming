#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module definesan object converting function to JSON representation."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"

import json
from typing import Any


def to_json_string(my_obj: Any) -> str:
    """
    Convert a Python object to its JSON string representation.

    Parameters_:
    - my_obj (Any): The Python object to be serialized to JSON.

    Returns_:
    - str: The JSON string representation of the input object.

    Example_:
        >>> to_json_string({"name": "Alice", "age": 30})
        '{"name": "Alice", "age": 30}'
    """
    return json.dumps(my_obj)


# Test code
if __name__ == "__main__":
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

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
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

    try:
        my_set = {132, 3}
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
