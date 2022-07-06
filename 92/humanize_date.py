from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date: datetime) -> str:
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime):
        raise ValueError()
    delta_seconds = (datetime.now() - date).total_seconds()
    if  delta_seconds < 0:
        raise ValueError()
    for threshold, phrase , divider in TIME_OFFSETS:
        if delta_seconds <= threshold:
            units_ago = int(delta_seconds) if divider is None else int(delta_seconds//divider)
            return phrase.format(units_ago)
    else:
        return date.strftime("%m/%d/%y")