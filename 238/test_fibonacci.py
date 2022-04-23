import pytest
from fractions import Fraction
from fibonacci import fib

# write one or more pytest functions below, they need to start with test_


def test_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1


def test_initial_recursions():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5


def test_negative_int():
    with pytest.raises(ValueError):
        fib(-1)


def test_decimal():
    with pytest.raises(ValueError):
        fib(2.5)


def test_string():
    with pytest.raises(TypeError):
        fib("foo")
