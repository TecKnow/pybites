from typing import Iterable, Tuple
from collections import Counter


def major_n_minor(numbers: Iterable[int]) -> Tuple[int, int]:
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    frequency_counter = Counter(numbers)
    frequencies = frequency_counter.most_common()
    return frequencies[0][0], frequencies[-1][0]
