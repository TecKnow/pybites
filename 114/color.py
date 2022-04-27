
import os
import sys
import urllib.request
from typing import Tuple

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color_name = color
        self.rgb = COLOR_NAMES.get(self.color_name.upper(), None)

    @staticmethod
    def hex2rgb(hex_color_str: str) -> Tuple[int, int, int]:
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(hex_color_str, str) or not len(hex_color_str) == 7 or not hex_color_str.startswith("#"):
            raise ValueError()
        return tuple(int(x, 16) for x in (hex_color_str[1:3], hex_color_str[3:5], hex_color_str[5:]))

    @staticmethod
    def rgb2hex(color_triple: tuple[int, int, int]) -> str:
        """Class method that converts an rgb value into a hex one"""
        if (
                not isinstance(color_triple, tuple)
                or len(color_triple) != 3
                or not all(isinstance(x, int) for x in color_triple)
                or not all(0 <= x <= 255 for x in color_triple)):
            raise ValueError()
        return f"#{color_triple[0]:02x}{color_triple[1]:02x}{color_triple[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}({self.color_name!r})"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb if self.rgb is not None else 'Unknown'}"
