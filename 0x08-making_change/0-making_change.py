#!/usr/bin/python3

""" This Contains makeChange function"""


def makeChange(coins, total):
    """
        This determine the fewest number of coins needed to
        meet a given amount total.

        Args:
            coins (list): This is a list of the values of the coins in
            your possession.
            total (int): This is the total amount to make with the coins.

        Returns:
            int: The fewest number of coins needed to meet the total.
        If the total cannot be met by any number of coins, return -1.
        """

    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
