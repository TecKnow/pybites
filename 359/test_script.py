import pytest
from typer.testing import CliRunner

from script import app

runner = CliRunner()

def test_root_help():
    result = runner.invoke(app, ["--help"])
    expected_strings = {
                        "compare   Command that checks whether a number d is greater than a number c.",
                        "subtract  Command that allows you to add two numbers." }
    for expected_string in expected_strings:
        assert expected_string in result.stdout

def test_compare_help():
    result = runner.invoke(app, ["compare", "--help"])
    expected_strings = {"Usage: root compare [OPTIONS] C D",
                        "c      INTEGER  First number to compare against. [default: None]",
                        "d      INTEGER  Second number that is compared against first number."}
    for expected_string in expected_strings:
        assert expected_string in result.stdout

def test_subtract_help():
    result = runner.invoke(app, ["subtract", "--help"])
    expected_strings = {"Usage: root subtract [OPTIONS] A B",
                        "a      INTEGER  The value of the first summand [default: None]",
                        "b      INTEGER  The value of the second summand [default: None]"}
    for expected_string in expected_strings:
        assert expected_string in result.stdout

def test_compare_gt():
    result = runner.invoke(app, ["compare", "3", "7"])
    assert result.stdout == 'd=7 is greater than c=3\n'

def test_compare_lt():
    result = runner.invoke(app, ["compare", "7", "3"])
    assert result.stdout == 'd=3 is not greater than c=7\n'

def test_compare_eq():
    result = runner.invoke(app, ["compare", "7", "7"])
    assert result.stdout == 'd=7 is not greater than c=7\n'

def test_subract():
    result = runner.invoke(app, ["subtract", "7", "7"])
    assert result.stdout =='The delta is 0\n'