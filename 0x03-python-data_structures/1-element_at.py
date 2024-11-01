#!/usr/bin/python3

def element_at(my_list, idx):
    try:
        assert idx in range(0, len(my_list))
    except AssertionError:
        return None
    else:
        return my_list[idx]
