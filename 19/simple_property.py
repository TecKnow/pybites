from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime) -> None:
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return NOW > self.expires
