from string import ascii_uppercase
from itertools import chain, cycle


def sequence_generator():
    yield from cycle(chain.from_iterable(enumerate(ascii_uppercase, 1)))
