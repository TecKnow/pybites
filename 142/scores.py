from itertools import chain
from typing import Collection, Container, Iterable, Generator, Iterator
from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def _die_roll_filter(rolls: Iterable[int], roll_range: Container = DICE_VALUES) -> Iterator[int]:
    for roll in rolls:
        if roll not in roll_range:
            raise ValueError(
                f"Found the value {roll}, but die rolls must be in {roll_range}")
        yield roll


def _high_roll_filter(rolls: Iterable[int], min_value: int = MIN_SCORE) -> Iterator[int]:
    for roll in rolls:
        if roll >= MIN_SCORE:
            yield roll


def _player_score_len_filter(players: Iterable[Player], scores_len: int) -> Iterator[Player]:
    for player in players:
        if len(player.scores) != scores_len:
            raise ValueError(
                f"All player's score lists must be the same length.  Found {len(player.scores)} but expected {scores_len}")
        yield player


def calculate_score(scores: Collection[int]) -> int:
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    return sum(_high_roll_filter(_die_roll_filter(scores)))


def get_winner(players: Collection[Player]) -> Player:
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    players_iterator = iter(players)
    first_player = next(players_iterator)
    scores_length = len(first_player.scores)
    players_iterator = chain([first_player], players_iterator)
    players_iterator = _player_score_len_filter(
        players_iterator, scores_len=scores_length)
    return max(players_iterator, key=lambda p: sum(p.scores))
