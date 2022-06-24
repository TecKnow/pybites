from string import punctuation


def remove_punctuation(input_string: str) -> str:
    """Return a str with punctuation chars stripped out"""
    return input_string.translate(remove_punctuation.translation_table)


remove_punctuation.translation_table = str.maketrans('', '', punctuation)
