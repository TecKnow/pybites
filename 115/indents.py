def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    res = 0
    for ch in text:
        if ch == " ":
            res += 1
        else:
            break
    return res
