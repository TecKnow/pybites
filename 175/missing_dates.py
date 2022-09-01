from typing import Collection, List
from datetime import date
from dateutil.rrule import rrule, DAILY


def get_missing_dates(dates: Collection[date]) -> List[date]:
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    first, last = min(dates), max(dates)
    date_iterator = rrule(DAILY, dtstart=first, until=last)
    return [
        iterated_date
        for iterated_datetime in date_iterator
        if (iterated_date := iterated_datetime.date()) not in dates]
