#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx not in range(0, len(my_list)):
        return copy

    copy[idx] = element
    return copy
