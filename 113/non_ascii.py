from string import printable

_printable_set = set(printable)
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if set(word) - _printable_set]
