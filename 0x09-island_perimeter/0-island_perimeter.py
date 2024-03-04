#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 04-03-2024
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == 1):
                if (i > 0 and grid[i - 1][j] == 0):
                    perimeter += 1
                if (j > 0 and grid[i][j - 1] == 0):
                    perimeter += 1
                if (j < cols - 1 and grid[i][j + 1] == 0):
                    perimeter += 1
                if (i < rows - 1 and grid[i + 1][j] == 0):
                    perimeter += 1
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print(island_perimeter(grid))
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
