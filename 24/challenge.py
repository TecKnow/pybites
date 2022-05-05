from abc import ABC, abstractmethod
from numbers import Number, Integral
from typing import Any, Collection


class Challenge(ABC):

    def __init__(self, number: Number, title: str) -> None:
        super().__init__()
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self) -> str:
        pass


class BlogChallenge(Challenge):
    def __init__(self, number: Number, title: str, merged_prs: Collection[Integral]) -> None:
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, pr: Integral) -> bool:
        return pr in self.merged_prs

    @property
    def pretty_title(self) -> str:
        return f"PCC{self.number} - {self.title.capitalize()}"


class BiteChallenge(Challenge):
    def __init__(self, number: Number, title: str, result: Any) -> None:
        super().__init__(number, title)
        self.result = result

    def verify(self, result: str) -> bool:
        return self.result == result

    @property
    def pretty_title(self) -> str:
        return f"Bite {self.number}. {self.title}"
