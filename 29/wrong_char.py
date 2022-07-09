from typing import Any, List


def get_index_different_char(chars: List[Any]):
    for i in range(len(chars)):
        a, b, c = str(chars[i-1]), str(chars[i]
                                       ), str(chars[(i+1) % len(chars)])
        if (a.isalnum() and c.isalnum() and not b.isalnum()
                or not a.isalnum() and not c.isalnum() and b.isalnum()):
            return i
