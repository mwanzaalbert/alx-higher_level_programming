#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
matrix_mul Module.

This module provides a function for performing matrix multiplication.
It validates the input matrices, checks compatibility for multiplication, and
returns the resulting matrix.

The module handles various edge cases, such as:
- Input types that are not lists of lists
- Matrices with inconsistent row sizes
- Empty matrices
- Matrices containing non-numeric elements
- Incompatible matrices for multiplication

## Example Usage:
```python
from matrix_mul import matrix_mul

# Valid multiplication example
result = matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(result)  # Output: [[19, 22], [43, 50]]
"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-20"
__version__ = "1.0"


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the resulting matrix.

    Parameters_:
        m_a (list of lists): List[List[int or float]] First matrix.
        m_b (list of lists): List[List[int or float]] Second matrix.

    Returns_:
        List[List[int or float]]: The resulting matrix after multiplication.

    Raises_:
        TypeError: If the inputs are not lists of lists or contain non-numeric
                   elements.
        ValueError: If matrices are empty, rows have inconsistent sizes, or
                    cannot be multiplied.
    """
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if any(not isinstance(element, (int, float)) for row in m_a
            for element in row):
        raise TypeError(
            "m_a should contain only integers or floats")

    if any(not isinstance(element, (int, float)) for row in m_b
            for element in row):
        raise TypeError(
            "m_b should contain only integers or floats")

    # Validate matrices
    # Number of columns in m_a must equal number of rows in m_b.
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
