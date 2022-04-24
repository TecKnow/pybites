import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("arg, expected", [
    [[1, -1], ValueError],
    [[10, 1], ValueError],
    [[1, 1.5], TypeError],
    [[True, 1], TypeError],
    ["123", TypeError],
    [123, TypeError],
])
def test_exception_cases(arg, expected):
    with pytest.raises(expected):
        list_to_decimal(arg)


@pytest.mark.parametrize("arg, expected", [
    [(1, 2, 3), 123],
    [{1: "one", 2: "two", 3: "three"}, 123],
    [{1, 2, 3}, 123],
    [(0, 1, 2, 3), 123],
    [(9, 8, 7), 987]
])
def test_regular_cases(arg, expected):
    assert list_to_decimal(arg) == expected


if __name__ == "__main__":
    pytest.main()
