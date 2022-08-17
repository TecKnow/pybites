from typing import List
from datetime import date, datetime

from dateutil.rrule import rrule, MO, TU, WE, TH, FR, WEEKLY

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date: date = TODAY) -> List[date]:
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    return [x.date() for x in rrule(WEEKLY, count=100, byweekday=(MO, TU, WE, TH, FR), dtstart=start_date)]
