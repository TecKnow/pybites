import pytest

from pangram import validate_pangram


@pytest.mark.parametrize(
    "pangram",
    [
        "thequickbrownfoxjumpsoverthelazydog",
        "The quick brown fox jumps over a lazy dog",
        "The five boxing wizards jump quickly",
        "Pack my box with five dozen liquor jugs",
        "Amazingly few discotheques provide jukeboxes",
        "The quick onyx goblin jumps over the lazy dwarf",
    ],
)
def test_validate_pangram(pangram):
    assert validate_pangram(pangram)


@pytest.mark.parametrize(
    "non_pangram",
    [
        "PYBITES IS A COMMUNITY OF PYTHON CODERS",
        "pybites",
        "pretty much anything else",
    ],
)
def test_validate_non_pangram(non_pangram):
    assert not validate_pangram(non_pangram)