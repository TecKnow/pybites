import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()

def test_no_argument(runner: CliRunner) -> None:
    result = runner.invoke(app, [])
    assert result.exit_code != 0

def test_basic_argument(runner: CliRunner) -> None:
    result = runner.invoke(app, ["David"])
    assert result.stdout == "Hello David!\n"

def test_help(runner: CliRunner) -> None:
    result = runner.invoke(app, "--help")
    assert "CLI that allows you to greet a person." in result.stdout
    assert "The name of the person to greet." in result.stdout