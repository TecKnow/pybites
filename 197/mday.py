from datetime import date
from calendar import Calendar


def get_mothers_day_date(year: int) -> date:
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    res = None
    for year_, month, mo_day, week_day in Calendar(firstweekday=6).itermonthdays4(year, 5):
        if year_ == year and month == 5 and week_day == 6 and mo_day > 7:
            res = date(year=year, month=5, day=mo_day)
            break
    assert res is not None
    return res
