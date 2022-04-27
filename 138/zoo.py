from weakref import WeakSet
from typing import Set


class Animal:

    def __init__(self, name: str):
        self.name: str = name
        self.__class__.serial_counter += 1
        self.serial_number: int = self.__class__.serial_counter
        self.__class__.instance_references.add(self)

    def __str__(self):
        return f"{self.serial_number}. {self.name.title()}"

    @classmethod
    def zoo(cls):
        return '\n'.join(tuple(str(r) for r in sorted(cls.instance_references, key=lambda x: x.serial_number)))

    serial_counter: int = 10000
    instance_references: Set['Animal'] = set()
