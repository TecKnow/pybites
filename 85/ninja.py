from math import inf

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:

    def __init__(self, score=0):
        self._score: int = score
        self._last_earned_belt: str = None

    @staticmethod
    def _get_belt(new_score):
        """Might be a useful helper"""
        scores = [*SCORES] + [inf]
        belts = [None] + [*RANKS]
        scores_to_belts_dict = dict(zip(scores, belts))
        for k, v in scores_to_belts_dict.items():
            if new_score < k:
                return v

    def _get_score(self):
        return self._score

    def _set_score(self, new_score: int) -> None:
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")
        if self._score >= new_score:
            raise ValueError("Cannot lower score")
        else:
            self._score = new_score
        if self._last_earned_belt != (new_belt := self._get_belt(self._score)):
            self._last_earned_belt = new_belt
            print(
                f"Congrats, you earned {self._score} points obtaining the PyBites Ninja {self._last_earned_belt.title()} Belt")
        else:
            print(f"Set new score to {self._score}")

    score = property(_get_score, _set_score)
