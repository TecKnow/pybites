from typing import Iterable, Tuple
from math import inf
IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village: Iterable[int]) -> Tuple[int, int, int]:
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    max_sum = -inf
    max_sum_start = max_sum_end = current_sum = current_start = 0
    for current_end, home in enumerate(village, 1):
        if current_sum <= 0:
            current_start = current_end
            current_sum = home
        else:
            current_sum += home

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_start = current_start
            max_sum_end = current_end
    if max_sum <= 0:
        print(IMPOSSIBLE)
        return (0, 0, 0)
    return (max_sum, max_sum_start, max_sum_end)
