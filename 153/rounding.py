from math import ceil, floor
from typing import Iterable, List


def round_up_or_down(transactions: Iterable[float], up: bool = True) -> List[int]:
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    round_func = ceil if up else floor
    return [round_func(x) for x in transactions]
