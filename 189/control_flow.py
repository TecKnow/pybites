from typing import Generator

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names: str) -> Generator[str, None, None]:
    i = 0
    for name in names:
        if i >= MAX_NAMES or name.startswith(QUIT_CHAR):
            break
        elif name.startswith(IGNORE_CHAR) or any((c.isdigit()for c in name)):
            continue
        i += 1
        yield name
