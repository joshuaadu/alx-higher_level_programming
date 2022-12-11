#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    if len(matrix) < 1:
        return
    new_matrix = []
    # loop through each row of the matrix
    for row in matrix:
        # loop through each index and square the value
        new_matrix.append(list(map(lambda x: x * x, row)))
    return new_matrix
