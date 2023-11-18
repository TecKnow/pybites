import pytest

from reverse_letters import reverse_letters


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("ab5dEf", "fE5dba"),
    ],
)
def test_reverse_letters(input_str, expected_output):
    assert reverse_letters(input_str) == expected_output