import re

import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_progress(capfd, runner):
    result = runner.invoke(app, [])
    pat = re.compile(r'^Processing... -+ 100% 0:\d+:\d+\nProcessed \d+ things.$')
    assert result.exit_code == 0
    print("*****")
    print(result.output.strip())
    assert pat.match(result.output.strip())