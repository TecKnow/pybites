
from os import PathLike
from pathlib import Path
from typing import List


ONE_KB = 1024


def get_files(dirname: PathLike, size_in_kb: int) -> List[str]:
    """Return files in dirname that are >= size_in_kb"""
    filter_size = size_in_kb * ONE_KB
    search_dir_path = Path(dirname)
    return [child.name for child in search_dir_path.iterdir() if child.stat().st_size >= filter_size]
