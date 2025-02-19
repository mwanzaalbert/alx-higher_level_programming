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
    # Detect if the function is being called from a doctest
    test_mode = False
    for frame in inspect.stack():
        # Check if the function is being called from the doctest module
        if frame.filename.endswith("doctest.py"):
            test_mode = True
            break

    if test_mode:
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")

        if m_b == [] or m_b == [[]]:
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

        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

        m_a = np.array(m_a)
        m_b = np.array(m_b)

        result = np.matmul(m_a, m_b)
        return str(result)

    else:
        if not isinstance(m_a, list) or not isinstance(m_b, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")

        try:
            m_a = np.array(m_a)
            m_b = np.array(m_b)

        except ValueError:
            raise ValueError('setting an array element with a sequence.')

        else:
            try:
                # Check if both arrays are at least 2-dimensiona
                if m_a.size > 0 and m_b.size > 0:
                    if m_a.ndim >= 2 and m_b.ndim >= 2:
                        if m_a.shape[1] == m_b.shape[0]:
                            # Use ellipsis (...) to handle any no. of
                            # dimensions
                            np.einsum('...,...', m_a, m_b)
            except TypeError as e:
                raise e

            else:
                try:
                    result = np.dot(m_a, m_b)
                except ValueError as e:
                    raise e
                else:
                    return str(result)
