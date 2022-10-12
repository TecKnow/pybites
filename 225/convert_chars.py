PYBITES = "pybites"


def convert_pybites_chars(text: str) -> str:
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    res = str()
    for ch in text:
        if ch.casefold() in PYBITES.casefold():
            if ch.isupper():
                res += ch.lower()
            else:
                res += ch.upper()
        else:
            res += ch
    return res
