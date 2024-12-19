#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module for performing matrix division.

This module provides a single function, `matrix_divided`, which takes a matrix
and divides each element by a given divisor. The function ensures the matrix
is well-formed and handles various edge cases such as invalid inputs or
division by zero.

Functions_:
    matrix_divided(matrix, div): Divides all elements of a matrix by a number.

"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-19"
__version__ = "1.1"


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args_:
        matrix (list of list of int/float): A list of lists where each sublist
            represents a row of the matrix and contains integers or floats.

        div (int/float): The number by which each element of the matrix will
                         be divided.

    Raises_:
        TypeError: If the matrix is not a list of lists of integers/floats,
            if the rows of the matrix are not of the same size,
            or if `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Returns_:
        list of list of float: A new matrix with each element divided by `div`,
            rounded to 2 decimal places.
    """
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(matrix) is not list or \
        any(not isinstance(element, (int, float)) for row in matrix
            for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element/div, 2) for element in row] for row in matrix]
