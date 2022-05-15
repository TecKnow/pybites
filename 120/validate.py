from functools import wraps
from multiprocessing.sharedctypes import Value


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for x in args:
            if not isinstance(x, int):
                raise TypeError()
            elif not x >= 0:
                raise ValueError()
        return func(*args, **kwargs)
    return wrapper
