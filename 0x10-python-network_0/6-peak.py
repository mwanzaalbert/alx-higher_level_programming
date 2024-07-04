#!/usr/bin/python3
"""
Module: peak_finder.

This module provides a function to find a peak in a list of unsorted integers.

The function `find_peak` uses a binary search approach to efficiently locate a
peak element in the given list. A peak element is defined as an element that is
greater than or equal to its neighbors (if they exist). If multiple peak elements
exist, any one of them may be returned.

Functions_:
    - find_peak(list_of_integers): Finds a peak in a list of unsorted integers.

Example usage:
    >>> from peak_finder import find_peak
    >>> find_peak([1, 2, 4, 6, 3])
    6
    >>> find_peak([4, 2, 1, 2, 3, 1])
    4  # or 3, since both are peaks
    >>> find_peak([2, 2, 2])
    2  # any element can be considered a peak in this case
    >>> find_peak([])
    None  # empty list returns None
    >>> find_peak([-2, -4, 2, 1])
    2
    >>> find_peak([4, 2, 1, 2, 2, 2, 3, 1])
    4  # or 3, since both are peaks

Module notes_:
    - The function `find_peak` operates with O(log(n)) time complexity,
      where n is the number of elements in the input list. This is achieved
      by using binary search to narrow down the search space.

"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args_:
        list_of_integers (list): A list of unsorted integers.

    Returns_:
        int or None: The peak element in the list. If the list is empty, returns None.
                     A peak element is defined as an element that is greater than or equal
                     to its neighbors (if they exist).

    Notes_:
        - The function uses a binary search approach to find a peak efficiently.
        - Multiple peak elements may exist, and any one of them can be returned.
    """
    if not list_of_integers_:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]

# Testing the function with provided test cases
if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 4 (or 3, both are peaks)
    print(find_peak([2, 2, 2]))  # Output: 2 (any element can be a peak in this case)
    print(find_peak([]))  # Output: None (empty list)
    print(find_peak([-2, -4, 2, 1]))  # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4 (or 3, both are peaks)
