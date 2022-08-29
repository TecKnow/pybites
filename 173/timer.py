from datetime import datetime, timedelta

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def _parse_delta_string(delta_string: str) -> timedelta:
    string_parts = delta_string.lower().split()
    days = hours = minutes = seconds = 0
    for part in string_parts:
        part = part.strip()
        if part.endswith("d"):
            days += int(part[:-1])
        elif part.endswith("h"):
            hours += int(part[:-1])
        elif part.endswith("m"):
            minutes += int(part[:-1])
        elif part.endswith("s"):
            seconds += int(part[:-1])
        elif part.isdecimal():
            seconds += int(part)
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    date_format_string = "%Y-%m-%d %H:%M:%S"
    time_distance = _parse_delta_string(delay_time)
    future_datetime = start_time + time_distance
    future_time_string = future_datetime.strftime(date_format_string)
    return f"{task} @ {future_time_string}"
