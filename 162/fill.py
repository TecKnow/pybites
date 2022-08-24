from typing import Any
HTML_SPACE = '&nbsp;'


def prefill_with_character(value: Any, column_length: int = 4, fill_char: str = HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    len_diff = column_length - len(str(value))
    return f"{fill_char * len_diff}{value}"
