#!/usr/bin/python3
""" This is the Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return (0)
    hops, roots = 0, 2
    while roots <= n:
        # if n evenly divides by root
        if n % roots == 0:
            # total even-divisions by root = total operations
            hops += roots
            # set n to the remainder
            n = n / roots
            # reduce root to find remaining smaller vals that evenly-divide n
            roots -= 1
        # increment root until it evenly-divides n
        roots += 1
    return (hops)
