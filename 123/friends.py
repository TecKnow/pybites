from typing import DefaultDict, Dict, List, Tuple, Set
from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


Friendships = List[Tuple[int, int]]
Users = Dict[int, str]


def _create_friend_sets(friendships: Friendships, users: Users) -> DefaultDict[int, Set[int]]:
    friend_sets = defaultdict(set)
    for a, b in friendships:
        friend_sets[a].add(b)
        friend_sets[b].add(a)
    return friend_sets


def get_friend_with_most_friends(friendships: Friendships, users: Users = users) -> Tuple[str, List[str]]:
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friend_sets = _create_friend_sets(friendships, users)
    size_of_biggest_friend_set = max(len(x) for x in friend_sets.values())
    biggest_userid, biggest_set = [
        (username, friend_set)
        for username, friend_set in friend_sets.items()
        if len(friend_set) == size_of_biggest_friend_set][0]
    return users[biggest_userid], [users[friend_id] for friend_id in biggest_set]
