from calendar import calendar
from typing import Dict

weekday_header = "Su Mo Tu We Th Fr Sa"


def get_weekdays(calendar_output: str) -> Dict[int, str]:
    """Receives a multiline Unix cal output and returns a mapping (dict) where
        keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.splitlines()
    weekday_abbreviations = lines[1].split()
    date_rows = calendar_output.splitlines()[2:]
    weekday_columns = [[row[n:(n+2)] for row in date_rows]
                       for n in range(0, len(date_rows[0]), 3)]
    weekday_tuples = list(zip(weekday_abbreviations, weekday_columns))
    weekday_dict = {
        int(d): w for w, ds in weekday_tuples for d in ds if d.strip()}
    return weekday_dict
