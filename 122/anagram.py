from collections import Counter
from string import whitespace

_whitespace_transtable = str.maketrans('', '', whitespace)


def is_anagram(word1: str, word2: str) -> bool:
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    c1 = Counter(word1.translate(_whitespace_transtable).casefold())
    c2 = Counter(word2.translate(_whitespace_transtable).casefold())
    return c1 == c2
