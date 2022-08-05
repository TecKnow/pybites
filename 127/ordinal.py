from collections import defaultdict
from typing import DefaultDict

suffixes = DefaultDict(
    lambda: "th",
    {
        "1": "st",
        "2": "nd",
        "3": "rd",
    }
)


def get_ordinal_suffix(number: int) -> str:
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    number_string = str(number)
    ones_digit = number_string[-1]
    suffix = "th"
    if len(number_string) < 2 or number_string[-2] != "1":
        suffix = suffixes[ones_digit]
    return f"{number_string}{suffix}"
