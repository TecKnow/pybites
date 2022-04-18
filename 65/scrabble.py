import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return tuple(_get_word_permutations_iterator(_get_permutations_draw_iterator(draw)))


def _get_permutations_draw_iterator(draw):
    """Helper to iterate all permutations of a draw"""
    for string_length in range(1, len(draw)+1):
        yield from ("".join(perm).lower() for perm in itertools.permutations(draw, string_length))


def _get_word_permutations_iterator(permutations_draw_iterator):
    yield from (candidate for candidate in permutations_draw_iterator if candidate in dictionary)
