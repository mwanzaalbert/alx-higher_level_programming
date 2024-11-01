#!/usr/bin/python3

def element_at(my_list, idx):
    return my_list[idx] if idx in range(0, len(my_list)) else None
