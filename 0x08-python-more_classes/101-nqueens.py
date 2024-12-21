#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
N Queens Problem Solver.

This script solves the N Queens problem, which involves placing N non-attacking
queens on an N×N chessboard.

The solution uses a backtracking algorithm to find all possible arrangements of
queens.

Usage:
    python3 101-nqueens.py N

Arguments_:
    N (int): The size of the chessboard and the number of queens to place.
             Must be an integer >= 4.

Output_:
    Each solution is printed as a list of lists, where each inner list
    contains the row and column of a queen.

    Example_:
        [[0, 1], [1, 3], [2, 0], [3, 2]]

Error Handling_:
    - Prints "Usage: nqueens N" and exits with status 1 if the number of
      arguments is incorrect.
    - Prints "N must be a number" and exits with status 1 if N is not an
      integer.
    - Prints "N must be at least 4" and exits with status 1 if N < 4.

Modules:
    - sys: Used for cmd-line argument parsing and exiting with status codes.

"""

__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-21"
__version__ = "1.1"

import sys


def print_solution(solution):
    """Print the solution in the required format."""
    print([[row, col] for row, col in enumerate(solution)])


def is_safe(queen_positions, row, col):
    """Check if a queen can be placed on the board at (row, col)."""
    for r, c in enumerate(queen_positions[:row]):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N, row=0, queen_positions=[]):
    """Solve the N queens problem using backtracking."""
    if row == N:
        print_solution(queen_positions)
        return

    for col in range(N):
        if is_safe(queen_positions, row, col):
            queen_positions.append(col)
            solve_nqueens(N, row + 1, queen_positions)
            queen_positions.pop()


def main():
    """Parse input arguments and solve the N queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
