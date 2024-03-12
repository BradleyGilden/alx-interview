#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """Determines winner of the prime number game"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_n + 1, i):
                primes[j] = False

    marias_wins, bens_wins = 0, 0
    for n in nums:
        primes_count = sum(primes[:n+1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
