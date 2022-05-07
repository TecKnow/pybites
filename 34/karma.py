from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    'Transaction',
    'giver points date',
    defaults=(None, None, datetime.now()))


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self._transactions = list()

    @property
    def fans(self):
        return len({x.giver for x in self._transactions})

    @property
    def points(self):
        return [x.points for x in self._transactions]

    @property
    def karma(self):
        return sum(self.points)

    def __add__(self, _o: Transaction):
        self._transactions.append(_o)

    def __str__(self) -> str:
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' if self.fans !=1 else ''}"
