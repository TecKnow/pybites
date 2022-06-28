from typing import List
from math import inf

# Derived from: https://www.geeksforgeeks.org/coin-change-dp-7/
# Solution contributed by Bhavya Jain


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input:      n - the changes amount
                coins - the coin denominations
    Output: how many ways to make this changes
    """

    # your code ...
    num_coins = len(coins)

    table = [[inf] * num_coins for i in range(n+1)]
    table[0] = [1] * num_coins
    for i in range(1, n+1):
        for j in range(num_coins):
            include = table[i-coins[j]][j] if i-coins[j] >= 0 else 0
            exclude = table[i][j-1] if j >= 1 else 0
            table[i][j] = include + exclude
    return table[-1][-1]