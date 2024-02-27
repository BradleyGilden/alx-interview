#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 27-02-2024
"""

def makeChange(coins, total):
    """ find mininum number of coin values that sum to the total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
