from pathlib import Path


def wc(file_: str) -> str:
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file_path = Path(file_)
    text = file_path.read_text()
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    return f"{lines} {words} {chars} {file_path}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
