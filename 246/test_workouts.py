from attr import Attribute
import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("input, expected_exception_type", (
    (3, AttributeError),
    (3.14, AttributeError),
    ({"mon": "upper"}, AttributeError),
    ([1, 2], AttributeError),
))
def test_invalid_inputs(capsys, input, expected_exception_type):
    with pytest.raises(expected_exception_type):
        print_workout_days(input)


@pytest.mark.parametrize("input", (
    "no_such_workout",
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
))
def test_empty_inputs(capsys, input):
    print_workout_days(input)
    captured = capsys.readouterr()
    assert captured.out == 'No matching workout\n'


@pytest.mark.parametrize("input, expected", (
    ('', "Mon, Tue, Wed, Thu, Fri\n"),
    ('upper', "Mon, Thu\n"),
    ("body", "Mon, Tue, Thu, Fri\n"),
    ("cardio", "Wed\n")
))
def test_valid_inputs(capsys, input, expected):
    print_workout_days(input)
    captured = capsys.readouterr()
    assert captured.out == expected


if __name__ == "__main__":
    pytest.main()
