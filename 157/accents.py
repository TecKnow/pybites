import unicodedata


def filter_accents(text: str) -> str:
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return ''.join((character for character in text.lower() if "WITH" in unicodedata.name(character)))
