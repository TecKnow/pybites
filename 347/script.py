from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB".casefold())
RIGHT_HAND_CHARS = set("YUIOPHJKLNM".casefold())


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    word = word.casefold()
    if not set(word) - LEFT_HAND_CHARS:
        return Hand.LEFT
    if not set(word) - RIGHT_HAND_CHARS:
        return Hand.RIGHT
    return Hand.BOTH


if __name__ == "__main__":
    print(get_hand_for_word("nymph"))
