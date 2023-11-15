from statistics import mean
from itertools import product

def original_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die."""
    return mean(range(1, n+1))


def new_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die when the player simultaneously rolls
    two dice and chooses the larger value.
    """
    return round(mean((max(x, y) for x, y in product(range(1, n+1), repeat=2))), 3)
