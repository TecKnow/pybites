from numbers import Real
from typing import List
from math import log10, floor


def _n_digit(number: Real, n_digits: int) -> int:
    if n_digits < 1:
        raise ValueError
    if number == 0:
        return 0
    starting_digits = floor(log10(abs(number))) + 1
    return int(number * pow(10, n_digits-starting_digits))


def n_digit_numbers(numbers: List[Real], n: int) -> List[int]:
    return [_n_digit(x, n) for x in numbers]
