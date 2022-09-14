from typing import Iterator
import re

line_comment_re = re.compile(r"^\s*#.*$")
pep_eight_comment_re = re.compile(r"^(?P<code>.*)(?P<comment> # .*)$")
multiline_comment_start_re = re.compile(r'^\s*"""(?P<code>.*)$')
miltiline_comment_end_re = re.compile(r'^.*"""\s*$')

def _non_comment_generator(code:str) -> Iterator[str]:
    inside_triple_quotes = False
    for line in code.splitlines():
        if not inside_triple_quotes and (m:= multiline_comment_start_re.match(line)):
            line = m.group("code")
            inside_triple_quotes = True
        if inside_triple_quotes and miltiline_comment_end_re.match(line):
            inside_triple_quotes = False
            continue
        if line_comment_re.match(line):
            continue
        line = line if not (m := pep_eight_comment_re.match(line)) else m.group('code')
        if not inside_triple_quotes:
            yield line


def strip_comments(code: str) -> str:
    # see Bite description
    return "\n".join(_non_comment_generator(code))

single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

if __name__ == "__main__":
    print(strip_comments(multiline_docstring))