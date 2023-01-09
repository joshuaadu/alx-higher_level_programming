#!/usr/bin/python3
# 2-matrix_divided.py
"""
This module defines a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):

    """
    Divides all elements of a matrix by a number div and returns a new matrix

    It takes two arguments:
        matrix: a list of lists of integers or floats
        div: a number (integer or float) greater than 0
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all([isinstance(col, (int, float))
                    for row in matrix for col in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    row_len = len(matrix[0])
    if not all([len(row) == row_len for row in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda col: round(col / div, 2), row))
            for row in matrix])


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
    print()
    # matrix = [1, 2, 3]
    # print(matrix_divided(matrix, 3))
    # print(matrix)
    # print()
    # matrix = []
    # print(matrix_divided(matrix, 3))
    # print(matrix)
    # print()
    # matrix = None
    # print(matrix_divided(matrix, 3))
    # print(matrix)
