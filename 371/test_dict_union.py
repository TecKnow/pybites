from typing import Dict, Optional

import pytest  # type: ignore

from dict_union import combine_and_count

fruit = {"apple": 3, "banana": 2, "orange": 1}
veggies = {"radish": 5, "artichoke": 2, "chard": 1}


def test_non_overlapping_dicts() -> None:
    """The union of disjoint dicts is their sum."""
    assert combine_and_count(fruit, veggies) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
        "radish": 5,
        "artichoke": 2,
        "chard": 1,
    }


def test_overlapping_dicts() -> None:
    """Add values of identical keys."""
    more_fruit = {"pear": 5, "orange": 2, "kiwi": 1}
    assert combine_and_count(fruit, more_fruit) == {
        "apple": 3,
        "banana": 2,
        "orange": 3,
        "pear": 5,
        "kiwi": 1,
    }


def test_union_with_empty_dict() -> None:
    """If either arg is an empty dictionary, return the other."""
    empty_sack: Dict[Optional[str], Optional[int]] = {}
    assert combine_and_count(fruit, empty_sack) == fruit
    assert combine_and_count(empty_sack, fruit) == fruit
    assert combine_and_count(empty_sack, empty_sack) == empty_sack


def test_bad_union() -> None:
    """Trying to combine the uncombinable raises TypeError.

    This doesn't exhaustively check all possible bad-args handling,
    but does try a couple of cases.
    """
    bad_fruit = {"orange": "two", "durian": 1}  # value you can't add
    not_a_dict = "What am I, chopped liver?"  # not even a dictionary
    with pytest.raises(TypeError):
        combine_and_count(fruit, bad_fruit)
    with pytest.raises(TypeError):
        combine_and_count(not_a_dict, fruit)  # type: ignore