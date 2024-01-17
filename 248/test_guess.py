import pytest

from guess import GuessGame, InvalidNumber


def test_constructor_not_number():
    with pytest.raises(InvalidNumber, match="Not a number"):
        GuessGame("foo")


def test_constructor_negative_number():
    with pytest.raises(InvalidNumber, match="Negative number"):
        GuessGame(-5)


def test_constructor_number_too_high():
    with pytest.raises(InvalidNumber, match="Number too high"):
        GuessGame(16)


def test_constructor_minimum_number():
    g = GuessGame(0)
    assert g.secret_number == 0


def test_constructor_maximum_number():
    g = GuessGame(15)
    assert g.secret_number == 15


def test_winning_game(capsys, monkeypatch):
    inputs = iter(("1", "6", "5"))
    expected_output = ("Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too high\n"
                       "Guess a number: \n"
                       "You guessed it!\n")
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    g = GuessGame(5, max_guesses=3)
    g()
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_losing_game(capsys, monkeypatch):
    inputs = iter(("1", "2", "3", "7", "6"))
    expected_output = ("Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too high\n"
                       "Guess a number: \n"
                       "Too high\n"
                       "Sorry, the number was 5\n"
                       )
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    g = GuessGame(5)
    g()
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_exceptional_game(capsys, monkeypatch):
    inputs = iter(("1", "e", "2", "3", "7", "6"))
    expected_output = ("Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Enter a number, try again\n"
                       "Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too low\n"
                       "Guess a number: \n"
                       "Too high\n"
                       "Guess a number: \n"
                       "Too high\n"
                       "Sorry, the number was 5\n"
                       )
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    g = GuessGame(5)
    g()
    captured = capsys.readouterr()
    assert captured.out == expected_output
