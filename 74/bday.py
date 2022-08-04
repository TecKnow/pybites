import calendar
import datetime


def weekday_of_birth_date(date: datetime.date) -> str:
    """Takes a date object and returns the corresponding weekday string"""
    weekday_number = calendar.weekday(date.year, date.month, date.day)
    return calendar.day_name[weekday_number]
