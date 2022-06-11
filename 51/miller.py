from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
        left on Planet Earth (calculated from start_date)"""
    time_remaining_delta = PY2_DEATH_DT - start_date
    hours_per_day = 24
    seconds_per_hour = 60*60
    time_remaining_hours = time_remaining_delta.days * \
        24 + time_remaining_delta.seconds / seconds_per_hour
    return round(time_remaining_hours, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
        left on Planet Miller (calculated from start_date)"""
    seconds_per_year = 365*24*60*60
    seconds_per_hour = 60*60
    time_dilation_factor = seconds_per_hour / (7 * seconds_per_year)
    earth_seconds_left = py2_earth_hours_left(start_date) * seconds_per_hour
    dilated_seconds = earth_seconds_left * time_dilation_factor
    dilated_minutes = dilated_seconds / 60
    return round(dilated_minutes, 2)
