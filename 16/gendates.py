from datetime import datetime, timedelta

from sqlalchemy import true

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    current_date = PYBITES_BORN
    hundred_days = timedelta(days=100)
    while True:
        current_date += hundred_days
        yield current_date
