#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 27-02-2024
"""

def makeChange(coins, total):
    """ find mininum number of coin values that sum to the total
    """
    if (total == 0):
        return 0
    maxval = total + 1
    # build the array to hold number of coin values for each coin
    dp = [maxval] * (maxval) 
    # we know 0 coins satisfy a value of 0
    dp[0] = 0
    # for all amounts up until the desired amount calculate the number
    # of coins required
    for a in range(1, maxval):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[total] if dp[total] != maxval else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
