from audioop import reverse
from bisect import insort
from dataclasses import dataclass, field
from functools import total_ordering
from math import floor
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@total_ordering
@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __eq__(self, __o: "Ninja") -> bool:
        if isinstance(__o, Ninja):
            return self.bites == __o.bites
        return NotImplemented

    def __gt__(self, __o: "Ninja") -> bool:
        if isinstance(__o, Ninja):
            return self.bites > __o.bites
        return NotImplemented

    def __str__(self) -> str:
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    ninjas: List[Ninja] = field(default_factory=list)

    def add(self, ninja: Ninja):
        insort(self.ninjas, ninja)

    def dump(self):
        return self.ninjas.pop(0)

    def highest(self, count: int = 1):
        return self.ninjas[:(len(self.ninjas)-count)-1:-1]

    def lowest(self, count: int = 1):
        return self.ninjas[:count]

    def pair_up(self, count=3):
        count = min(count, floor(len(self.ninjas)/2))
        pairs = list(zip(reversed(self.ninjas), self.ninjas,))
        return pairs[:count]

    def __len__(self) -> int:
        return len(self.ninjas)
