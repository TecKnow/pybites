from collections.abc import MutableSequence
from collections import UserList
import statistics
from numbers import Real
from decimal import Decimal, DecimalException
from typing import Union, Iterable


class IntList(UserList, MutableSequence):

    def append(self, item: Union[Real, Decimal]) -> None:
        try:
            d = Decimal(item)
            self.data.append(d)
        except (DecimalException, ValueError) as e:
            raise TypeError from e

    def extend(self, other: Iterable[Union[Real, Decimal]]) -> None:
        for x in other:
            self.append(x)

    def __add__(self, other: Iterable[Union[Real, Decimal]]) -> "IntList":
        new_list = IntList(self.data).extend(other)
        return new_list

    def __iadd__(self, other: Iterable[Union[Real, Decimal]]) -> "IntList":
        self.extend(other)
        return self

    @property
    def mean(self) -> Real:
        return float(statistics.mean(self))

    @property
    def median(self) -> Real:
        return float(statistics.median(self))
