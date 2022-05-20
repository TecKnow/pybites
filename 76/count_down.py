from collections.abc import Collection
from functools import singledispatch
from numbers import Number


@singledispatch
def count_down(data_type):
    if not isinstance(data_type, Collection):
        raise ValueError()
    data_type = [str(x) for x in data_type]
    while data_type:
        print(''.join(data_type))
        data_type = data_type[:-1]


@count_down.register
def _(data_type: Number):
    count_down(str(data_type))
