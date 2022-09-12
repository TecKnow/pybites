from datetime import timedelta
import re
from typing import List, Iterator, NamedTuple

caption_re = re.compile(
    r"""
      (?:\s*)(?P<ID>\d+)(?:\s)*\n
      (?P<start>\d+:\d+:\d+,\d+)(?:\s*)-->(?:\s*)(?P<stop>\d+:\d+:\d+,\d+)(?:\s*)\n
      (?P<text>(.*?(?=(\n)|$)))(?:(?:\n\n)|$)
      # The line above combines a non-greedy quantifier (*) with positive lookahead
      # 
      # The non-greedy quantifier wants consume as little as possible.
      # This prevents it from skipping to the end of the input, but by default it
      # would consume 0 characters.  That's not enough.
      # 
      # The positive lookahead forces the non-greedy quantifier to consume until
      # the next character would be a newline or the end of the string.  
      # Then the ((\n\n) | $) grouping tries to match, including the 
      # un-consumed \n from the lookahead.  If it fails, the expression backtracks 
      # and the non-greedy quantifier is forced to continue until just before the
      # next \n.
    """,
    flags=re.DOTALL | re.VERBOSE)
timestamp_re = re.compile(
    r"(?:\D*)(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+),(?P<milliseconds>\d+)(?:\D*)")


class Caption(NamedTuple):
    ID: int
    start_time: timedelta
    stop_time: timedelta
    text: str

    @property
    def duration(self) -> float:
        return int((self.stop_time - self.start_time).total_seconds())

    @property
    def rate(self) -> float:
        return len(self.text.strip()) / self.duration


def _timestamp_str_to_delta(timestamp_str: str, subsecond=False) -> timedelta:
    match = timestamp_re.match(timestamp_str)
    if match is None:
        raise ValueError(
            f"Unable to parse {timestamp_str} as a subtitle timestamp")
    ts_parts = {k: int(v) for k, v in match.groupdict().items()}
    if not subsecond:
        del ts_parts["milliseconds"]
    return timedelta(**ts_parts)


def _captions(text: str) -> Iterator[Caption]:
    for cap_match in caption_re.finditer(text):
        ID = int(cap_match.group("ID"))
        start = _timestamp_str_to_delta(cap_match.group("start"))
        stop = _timestamp_str_to_delta(cap_match.group("stop"))
        cap_text = cap_match.group("text")
        yield Caption(ID, start, stop, cap_text)


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    return [c.ID for c in sorted(_captions(text), key=lambda x: x.rate, reverse=True)]
