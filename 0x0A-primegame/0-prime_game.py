#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 10-03-2024
"""


def isPrime(num):
    """ determines if number is a prime number
    """
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


def deleteMultiples(primeIndex, picks):
    """ deletes all multiples ahead of prime
    """
    n = primeIndex + 1
    while n < len(picks):
        if picks[n] % picks[primeIndex] == 0:
            del picks[n]
        else:
            n += 1


def isWinner(x, nums):
    """ determines winner of prime game"""
    # Maria starts first
    mariaWins, benWins = 0, 0

    for i in range(x):
        picks = [j for j in range(1, nums[i] + 1)]
        n = 0
        benMadeMove, mariaMadeMove = False, False
        mariaTurn = True
        while n < len(picks):
            if isPrime(picks[n]):
                # delete the multiples of the prime
                deleteMultiples(n, picks)
                # then delete the prime
                del picks[n]
                # track which player made a move
                benMadeMove = not mariaTurn
                mariaMadeMove = mariaTurn
                # after a prime is chosen, switch turns
                mariaTurn = not mariaTurn
            else:
                n += 1
            if n >= len(picks):
                # if it's ben's turn, but ben has not made a move
                if (not mariaTurn and not benMadeMove):
                    mariaWins += 1
                # if it's marias turn but maria has not made a move
                elif (mariaTurn and not mariaMadeMove):
                    benWins += 1

    return 'Maria' if mariaWins > benWins else 'Ben'


if __name__ == '__main__':
    print('Winner:', isWinner(5, [2, 5, 1, 4, 3]))
