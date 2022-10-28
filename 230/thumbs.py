THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __mul__(self, other: int) -> str:
        if not isinstance(other, int):
            return NotImplemented
        elif other == 0:
            raise ValueError()
        elif other <= -4:
            return f"{THUMBS_DOWN} ({abs(other)}x)"
        elif -4 < other < 0:
            return THUMBS_DOWN * abs(other)
        elif 0 < other < 4:
            return THUMBS_UP * other
        elif 4 <= other:
            return f"{THUMBS_UP} ({other}x)"
        else:
            raise ValueError()

    def __rmul__(self, other: int) -> str:
        return self.__mul__(other)
