from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string_deque = deque(string)
    string_deque.rotate(-n)
    rotated_string = ''.join(string_deque)
    return rotated_string
