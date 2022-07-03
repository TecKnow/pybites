from typing import Tuple


def rgb_to_hex(rgb: Tuple[int, int, int]):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(0 <= c <= 255 for c in rgb):
        raise ValueError()
    r, g, b = rgb
    return f"#{r:02X}{g:02X}{b:02X}"
