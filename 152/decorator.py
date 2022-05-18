from curses import wrapper
from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def strip_range_factory(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            a = max(start, 0)
            b = min(end, len(res))
            if b < a:
                return res
            res = res[:a] + "."* min((b - a), len(res)) + res[b:]
            return res
        return wrapper
    return strip_range_factory