class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self) -> None:
        self.max_score = None

    def __call__(self, score: int) -> int:
        self.max_score = score if self.max_score is None or self.max_score < score else self.max_score
        return self.max_score
