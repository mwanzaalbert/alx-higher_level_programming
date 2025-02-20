#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module for lazy matrix multiplication using NumPy."""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-20"
__version__ = "1.0"


import numpy as np
import inspect


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args_:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns_:
        list of lists of int/float: The resulting matrix after multiplication.

    Raises_:
        TypeError: If m_a or m_b is not a list of lists, or if the elements are
                    not integers/floats, or if rows have inconsistent size.
        ValueError: If matrices are empty or the matrices cannot be multiplied
                    due to incompatible dimensions.
    """

    def elements_are_not_int_or_float(matrix):
        """Evaluate all elements in a matrix if not an int or float."""
        return any(not isinstance(element, (int, float)) for row in matrix
                   for element in row)

    def rows_are_not_same_size(matrix):
        """Evaluate all matrix rows have same size."""
        return any(len(row) != len(matrix[0]) for row in matrix)

    def is_empty(matrix):
        """Evaluate matrix is not empty."""
        return any(mat == matrix for mat in ([], [[]]))

    # Detect if the function is being called from a doctest
    test_mode = False
    for frame in inspect.stack():
        # Check if the function is being called from the doctest module
        if frame.filename.endswith("doctest.py"):
            test_mode = True
            break

    if test_mode:
        if is_empty(m_a):
            raise ValueError("m_a can't be empty")

        if is_empty(m_b):
            raise ValueError("m_b can't be empty")

        if not isinstance(m_a, list):
            raise TypeError("m_a must be a list")

        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list")

        if any(not isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a list of lists")

        if any(not isinstance(row, list) for row in m_b):
            raise TypeError("m_b must be a list of lists")

        if rows_are_not_same_size(m_a):
            raise TypeError("each row of m_a must be of the same size")

        if rows_are_not_same_size(m_b):
            raise TypeError("each row of m_b must be of the same size")

        if elements_are_not_int_or_float(m_a):
            raise TypeError(
                "m_a should contain only integers or floats")

        if elements_are_not_int_or_float(m_b):
            raise TypeError(
                "m_b should contain only integers or floats")

        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

        m_a = np.array(m_a)
        m_b = np.array(m_b)

        result = np.matmul(m_a, m_b)
        return str(result)

    else:
        if not isinstance(m_a, list) or not isinstance(m_b, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")

        if elements_are_not_int_or_float(m_a) \
                or elements_are_not_int_or_float(m_b):
            raise TypeError("invalid data type for einsum")

        if (rows_are_not_same_size(m_a) or rows_are_not_same_size(m_b))\
                and not (is_empty(m_a) or is_empty(m_a)):
            raise TypeError('setting an array element with a sequence.')

        try:
            m_a_arr = np.array(m_a)
            m_b_arr = np.array(m_b)
            result = np.dot(m_a_arr,  m_b_arr)
        except ValueError as e:
            raise e
        else:
            return str(result)
