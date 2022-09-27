# See tests for a more comprehensive complementary table
from typing import Dict, Mapping, Union


SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


def _clean_table(str_table: str) -> Dict[str, str]:
    return {a: b for a, *_, b in [line.split() for line in str_table.upper().strip().splitlines()[2:]]}


# Recommended helper function
def _clean_sequence(sequence: str, str_table: str) -> str:
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    trans_table = _clean_table(str_table)
    return ''.join(c for c in sequence.upper() if c in trans_table.keys())


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    return _clean_sequence(sequence, str_table)[::-1]


def complement(sequence: str, str_table: str = SIMPLE_COMPLEMENTS_STR) -> str:
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    trans_dict: Dict[str, Union[int, str, None]] = dict(
        _clean_table(str_table))
    return _clean_sequence(sequence, str_table).translate(str.maketrans(trans_dict))


def reverse_complement(sequence: str, str_table: str = SIMPLE_COMPLEMENTS_STR) -> str:
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    cmp = complement(sequence, str_table)
    rev_cmp = reverse(cmp, str_table)
    return rev_cmp


if __name__ == "__main__":
    import pprint
    pprint.pprint(_clean_table(SIMPLE_COMPLEMENTS_STR))
