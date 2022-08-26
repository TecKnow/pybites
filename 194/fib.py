from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n: int) -> int:
    if n in range(0, 3):
        return 1
    else:
        return cached_fib(n-2) + cached_fib(n-1)
