from functools import total_ordering
from numbers import Real
from typing import Union


@total_ordering
class Account:

    def __init__(self, name: str, start_balance: Real = 0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self) -> Real:
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, __o: "Account") -> bool:
        return self.balance == __o.balance

    def __lt__(self, __o: "Account") -> bool:
        return self.balance < __o.balance

    def __getitem__(self, index: Union[int, slice]) -> Real:
        return self._transactions[index]

    def __iter__(self):
        return self._transactions.__iter__()

    def __add__(self, __o: int) -> "Account":
        if not isinstance(__o, int):
            return NotImplemented
        self._transactions.append(__o)
        return self

    def __sub__(self, __o: int) -> "Account":
        if not isinstance(__o, int):
            return NotImplemented
        self._transactions.append(-__o)
        return self

    def __str__(self) -> str:
        return f"{self.name} account - balance: {self.balance}"
