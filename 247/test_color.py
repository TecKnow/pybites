from unittest.mock import patch, Mock

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

def test_gen_hex_color(gen):
    with patch('color.sample', new=Mock(side_effect=[[255,255,255]])) as sample_mock:
        res = next(gen)
        assert str(res) == "#FFFFFF"
    sample_mock.assert_called_once_with(range(0, 256), 3)