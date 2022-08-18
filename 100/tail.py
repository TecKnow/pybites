from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    return [line.strip() for line in filepath.read_text().strip().splitlines()][-n:]
