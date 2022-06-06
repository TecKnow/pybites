from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    hundred_days = timedelta(days=100)
    finish_date = start_100days + hundred_days
    format_string = "%Y-%m-%d"
    return finish_date.strftime(format_string)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    duration = pycon_date - pybites_founded
    return duration.days
