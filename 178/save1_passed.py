import os
import re
from collections import Counter
from urllib.request import urlretrieve

from dateutil.parser import parse

logline_re_str = r"Date:\s*(?P<date>[^|]*)\s+\|\s*\d*\s*file(?:s){0,1}\s*changed,\s*(?:(?P<insertions>\d*)\s*insertion(?:s){0,1}\(\+\)){0,1}(?:,){0,1}\s*(?:(?P<deletions>\d*)\s*deletion(?:s){0,1}\(\-\)){0,1}"
logline_re = re.compile(logline_re_str)

abr_strs = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
mon_num_strs = "01 02 03 04 05 06 07 08 09 10 11 12".split()
abr_to_num_dict = dict(zip(abr_strs, mon_num_strs))

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)

    Example line:
    Date:   Thu Feb 21 16:21:50 2019 +0100 | 3 files changed, 78 insertions(+), 2 deletions(-)
    """
    month_lines = Counter()
    with open(commit_log) as log_file:
        for line in log_file:
            match_obj = logline_re.match(line)
            date_obj = parse(match_obj.group("date"))
            if year is None or int(date_obj.year) == year:
                date_str = YEAR_MONTH.format(y=int(date_obj.year), m=int(date_obj.month))
                insertions = match_obj.group("insertions")
                insertions = int(insertions) if insertions is not None else 0
                deletions = match_obj.group("deletions")
                deletions = int(deletions) if deletions is not None else 0
                month_lines[date_str] += insertions
                month_lines[date_str] += deletions
        sorted_month_lines = month_lines.most_common()
        return (sorted_month_lines[-1][0], sorted_month_lines[0][0])
