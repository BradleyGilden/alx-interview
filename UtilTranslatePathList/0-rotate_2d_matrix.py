#!/usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Author: Bradley Dillion Gilden
Date: 20-02-2024
"""

def rotate_2d_matrix(matrix):
    """ rotates a matrix in its place
    """
    # first reverse the matrix
    matrix.reverse()
    n = len(matrix)
    # then proceed to swap indices
    for i in range(n):
        for j in range(n):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
    rotate_2d_matrix(matrix)
    rotate_2d_matrix(matrix2)
    print(matrix)
    print(matrix2)
