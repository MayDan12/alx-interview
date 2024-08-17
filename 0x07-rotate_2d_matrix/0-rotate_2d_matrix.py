#!/usr/bin/python3
"""
This function rotates a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    This Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        The matrix (list of list of int): The matrix to rotate.
    """
    d = len(matrix)

    # Transpose the matrix
    for i in range(d):
        for j in range(i + 1, d):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(d):
        matrix[i].reverse()