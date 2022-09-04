from os import PathLike
from pathlib import Path
from typing import Union, Tuple


def count_dirs_and_files(directory: Union[str, PathLike] = '.') -> Tuple[int, int]:
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    files = directories = 0
    for path in Path(directory).glob("**/*"):
        if path.is_file():
            files += 1
        if path.is_dir():
            directories += 1
    return directories, files
