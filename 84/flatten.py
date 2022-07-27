from typing import Iterable


def flatten(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item
