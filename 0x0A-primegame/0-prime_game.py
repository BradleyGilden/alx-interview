#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """ wrapper for the inner functions """

    def findMultiples(num, targets):
        """
        Finds multiples of a given number within a list
        """
        for i in targets:
            if i % num == 0:
                targets.remove(i)
        return targets

    def isPrime(i):
        """
        Check if a number is prime.
        """
        if i == 1:
            return False
        for j in range(2, i):
            if i % j == 0:
                return False
        return True

    def findPrimes(n):
        """
        Dispatch a given set into prime numbers and non-prime numbers.
        """
        counter = 0
        target = list(n)
        for i in range(1, len(target) + 1):
            if isPrime(i):
                counter += 1
                target.remove(i)
                target = findMultiples(i, target)
            else:
                pass
        return counter

    def getWinner(x, nums):
        """ finds the winner
        """
        players = {'Maria': 0, 'Ben': 0}
        cluster = set()
        for elem in range(x):
            nums.sort()
            num = nums[elem]
            for i in range(1, num + 1):
                cluster.add(i)
                if i == num + 1:
                    break
            temp = findPrimes(cluster)

            if temp % 2 == 0:
                players['Ben'] += 1
            elif temp % 2 != 0:
                players['Maria'] += 1

        if players['Maria'] > players['Ben']:
            return 'Maria'
        elif players['Maria'] < players['Ben']:
            return 'Ben'
        else:
            return None

    return getWinner(x, nums)
