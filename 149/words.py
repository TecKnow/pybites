from curses.ascii import isdigit
from typing import List, Sequence


def sort_words_case_insensitively(words: Sequence[str]) -> List[str]:
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    return sorted(words, key=lambda x: (x[0].isdecimal(), x.casefold()))
