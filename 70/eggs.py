from typing import Iterator
from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.current < self.limit:
            self.current += 1
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration()
