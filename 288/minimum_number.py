from typing import List


def minimum_number(digits: List[int]) -> int:
    if not digits:
        return 0
    sorted_digits = sorted(set(digits))
    str_digits = [str(x) for x in sorted_digits]
    number_str = ''.join(str_digits)
    return int(number_str)
