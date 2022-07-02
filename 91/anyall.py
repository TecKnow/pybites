VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all((character in VOWELS for character in input_str.casefold()))


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any((character in PYTHON for character in input_str.casefold()))


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(character.isdigit() for character in input_str.casefold())
