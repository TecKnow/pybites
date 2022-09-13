from typing import Container, Set
from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)

date_re = re.compile(r"\d{4}-\d{2}-\d{2}")
date_format = "%Y-%m-%d"


def extract_dates(data: str) -> Set[date]:
    """Extract unique dates from DB table representation as shown in Bite"""
    return {datetime.strptime(found_date, date_format).date() for found_date in date_re.findall(data)}


def calculate_streak(dates: Container[date]) -> int:
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    previous_day_delta = timedelta(days=1)
    streak_days = 0
    query_date = TODAY
    if query_date in dates:
        streak_days += 1
    while True:
        query_date = query_date - previous_day_delta
        if query_date in dates:
            streak_days += 1
        else:
            break
    return streak_days
