#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""


def minOperations(n):
    """find minimum amount of operations to reach n number of H characters"""
    if (type(n) is not int or n <= 1):
        return 0
    if (n == 2):
        return 2
    # assume we have already copied and pasted the initial h_character
    h_count = 2
    # current value stored in clipboard
    clipboard = 1
    copy = 1
    paste = 0

    while (h_count != n):
        if (n % (h_count + clipboard) == 0):
            paste += 1
            h_count += clipboard
            copy += 1
            clipboard = h_count
        else:
            h_count += clipboard
            paste += 1

    return copy + paste


if __name__ == '__main__':
    n = 15
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
