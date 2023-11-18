import pytest

from art_thief import art_thief


@pytest.mark.parametrize(
    "paintings, expected",
    [
        ([], 0),  # Test with no paintings
        ([5], 5),  # Test with one painting
        ([3, 5], 5),  # Test with two paintings
        ([6, 1, 9, 7, 4, 8, 3, 5, 2, 10], 38),  # Test with ten paintings
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),  # Test with consecutive values
        ([10, 10, 10, 10, 10], 30),  # Test with same values
        ([3, 1, 10, 50, 2, 9], 62),  # Test that breaks the odd-even pattern
    ],
)
def test_art_thief(paintings, expected):
    assert art_thief(paintings) == expected