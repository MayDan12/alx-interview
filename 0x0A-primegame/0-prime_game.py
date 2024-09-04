#!/usr/bin/python3
"""
This is a Prime Game that calculate the winner
base on the prime
number choose in the given set of numbers.
"""


def prime(n):
    """This Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): The upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for g in range(2, n + 1):
        if (sieve[g]):
            prime.append(g)
            for h in range(g * g, n + 1, g):
                sieve[h] = False
    return prime


def isWinner(x, nums):
    """
    This Method that determine the winner of a prime number

    Args:
        xi: This is the nuber of rounds
        nums: This is an array of n

    Return:
        return name of the player that won the most rounds
    """

    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria, Ben = 0, 0

    for i in range(x):
        primes = prime(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # This Determine the overall winner
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
