import types
from itertools import islice
from typing import Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def group(iterable: Iterable[T], n: int) -> List[List[T]]:
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    res = list()
    iterator = iter(iterable)
    while True:
        new_sublist = list(islice(iterator, n))
        if new_sublist:
            res.append(new_sublist)
        else:
            break
    return res


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
