#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(pow, row, [2] * len(row))) for row in matrix]
