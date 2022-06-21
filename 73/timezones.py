import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc: datetime, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = pytz.utc.localize(utc)
   #  print(utc)
    for timezone_name in timezones:
        try:
            local_time = utc.astimezone(pytz.timezone(timezone_name))
            if not local_time.hour in MEETING_HOURS:
                return False
        except pytz.UnknownTimeZoneError as e:
            raise ValueError(f"Unknown timezone: {timezone_name}") from e
    else:
        return True
