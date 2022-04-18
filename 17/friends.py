from typing import Sequence
from itertools import permutations, combinations


def friends_teams(friends: Sequence[str], team_size: int = 2, order_does_matter: bool = False) -> Sequence[Sequence[str]]:
    enumerating_function = permutations if order_does_matter else combinations
    return tuple(enumerating_function(friends, team_size))
