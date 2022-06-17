from typing import List
from math import comb


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    # The complication here is an off-by-one error
    # since mathematicians start counting at 1 and
    # computer science starts counting at 0.
    # Therefore the expected result is actually the N-1th row.
    #
    # combined with the fact that range is an end-exclusive interval
    # but the range of values that must be tested is from 0..N inclusive
    # this problem runs counter to programmer intuition in every possible way
    # but it is not otherwise complicated.

    return [comb(N-1, k) for k in range(N)]
    # return row
