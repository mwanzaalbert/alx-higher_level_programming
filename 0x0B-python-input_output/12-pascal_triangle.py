#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module provides functionality to generate Pascal's Triangle.

It contains one main function: `pascal_triangle` which generates a Pascal's
triangle up to a given number of rows.
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-22"
__version__ = "1.1"


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with `n` rows using an iterative approach.

    Parameters
    ----------
    n : int
        The number of rows of Pascal's Triangle to generate.

    Returns
    -------
    List[List[int]]
        A list of lists
        Each inner list represents a row in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for row in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        current_row = [1]  # Start the new row with 1

        # Compute the middle elements by summing pairs of elements
        # from the previous row
        for i in range(1, row):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)  # End the new row with 1
        triangle.append(current_row)  # Add the new row to the triangle

    return triangle


def print_triangle(triangle):
    """Print the triangle."""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
