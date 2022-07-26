from enum import Enum
from statistics import mean

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self) -> str:
        thumb_str = ''.join([THUMBS_UP] * self.value)
        return f"{self.name} => {thumb_str}"

    @classmethod
    def average(cls):
        return mean((score.value for score in Score))
