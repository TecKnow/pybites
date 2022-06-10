from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    paren_re = re.compile(r"\((.+)\)")
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    file_lines = (line.strip() for line in open(COURSE_TIMES))
    duration_strs = (match.group(1)
                     for line in file_lines if (match := paren_re.search(line)))
    return list(duration_strs)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    timestamp_re = re.compile(r"(\d+):(\d+)")
    duration_strs = (match.group(1, 2)
                     for line in timestamps if (match := timestamp_re.search(line)))
    duration_ints = ((int(mins), int(secs)) for (mins, secs) in duration_strs)
    duration_deltas = (timedelta(minutes=mins, seconds=secs)
                       for (mins, secs) in duration_ints)
    total_time = sum(duration_deltas, timedelta())
    return (str(total_time))
