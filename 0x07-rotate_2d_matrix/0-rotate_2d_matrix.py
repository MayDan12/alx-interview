#!/usr/bin/python3
"""
This defines a function that rotates an nxn 2D matrix
90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    This Rotate a 2d square matrix 90 degrees clockwise in-place
    Args:
        The matrix (list): 2d square matrix
    Return:
        Nothing
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each column
    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp