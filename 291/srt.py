from datetime import timedelta
import re
from typing import List, Iterator, NamedTuple

caption_re = re.compile(
    r"(?:\s*)(?P<ID>\d+)(?:\s)*\n(?P<start>\d\d:\d\d:\d\d,\d\d\d)(?:\s*)-->(?:\s*)(?P<stop>\d\d:\d\d:\d\d,\d\d\d)(?:\s)*\n(?P<text>(.*?(?=(\n)|$)))(?:(?:\n\n)|$)", flags=re.DOTALL)


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


text1 = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""
text2 = """
18
00:01:12,100 --> 00:01:17,230
If you want a bit more minimalistic view, you can actually hide the sidebar.

19
00:01:18,200 --> 00:01:19,500
If you go to Settings

20
00:01:23,000 --> 00:01:26,150
scroll down to 'Focus Mode'.

21
00:01:28,200 --> 00:01:35,180
You can actually hide the sidebar and have only the description and the code editor.
"""  # noqa E501
text3 = '\n'.join(text1.splitlines()[:9])
text4 = '\n'.join(text2.splitlines()[5:])
# testing hours as well
text5 = """
32
00:59:45,000 --> 00:59:48,150
talking quite normal here

33
01:00:00,000 --> 01:00:07,000
he is talking slooooow

34
02:04:28,000 --> 02:04:30,000
she is talking super fast here!
"""


def _timestamp_str_to_delta(timestamp_str: str, subsecond=False) -> timedelta:

    *hm, s_ = timestamp_str.split(":")
    timestamp_parts = hm + s_.split(',')
    hours, minutes, seconds,  milliseconds = (int(x) for x in timestamp_parts)
    res: timedelta
    if subsecond:
        timedelta(hours=hours, minutes=minutes,
                  seconds=seconds, milliseconds=milliseconds)
    else:
        res = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return res


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


if __name__ == "__main__":
    from pprint import pprint
    pprint(list(((c.ID, c.duration, c.rate, c.text)
           for c in _captions(text1))))
