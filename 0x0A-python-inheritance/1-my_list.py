#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The module defines a custom list class `MyList`.

The class extends the built-in `list` class. It includes a method to print
the elements of the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in `list` class.

    Has an additional method to print the list elements in sorted order.
    """

    def print_sorted(self) -> None:
        """
        Print the elements of the list in ascending sorted order.

        The original list remains unchanged.
        """
        sorted_list: list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    # # Create an instance of MyList
    # my_list = MyList()

    # # Append elements to the list
    # my_list.append(1)
    # my_list.append(4)
    # my_list.append(2)
    # my_list.append(3)
    # my_list.append(5)

    # # Print the original list
    # print(my_list)

    # # Print the sorted version of the list
    # my_list.print_sorted()

    # # Print the original list again to show it remains unchanged
    # print(my_list)

    import doctest
    doctest.testfile('tests/1-my_list.txt', verbose=True)
