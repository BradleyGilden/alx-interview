#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 05-02-2024
"""
import sys


def place(row, col, x):
    """verifies that we are able to place a queen at (row, col)"""
    for r, c in enumerate(x):
        if (c == col or row + col == r + c or row - col == r - c):
            return False
    return True


def NQueens(N, row=0, x=[]):
    """
    finds all possible orientations for N number of queens for an NxN chess
    board
    """
    for col in range(N):
        if (place(row, col, x)):
            x.append(col)
            # last row was found
            if (row == N - 1):
                # print nested list of nqueens co-ordinates
                print([[row, col] for row, col in enumerate(x)])
            else:
                NQueens(N, row + 1, x)
            x.pop()  # back track by removing last queens postion


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Usage: nqueens N")
        exit(1)
    elif (not sys.argv[1].isdecimal()):
        print("N must be a number")
        exit(1)
    elif (int(sys.argv[1]) < 4):
        print("N must be at least 4")
        exit(1)
    NQueens(int(sys.argv[1]))
