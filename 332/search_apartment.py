from typing import List
from math import inf

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """

    iteration_order = enumerate(buildings)
    if direction == EAST:
        iteration_order = ((len(buildings) - idx, height)
                           for (idx, height) in enumerate(reversed(buildings), 1))
    max_height = -inf
    res = list()
    for idx, height in iteration_order:
        if height > max_height:
            max_height = height
            res.append(idx)
    return sorted(res)


if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
