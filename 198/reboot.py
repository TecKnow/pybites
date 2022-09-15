from datetime import datetime, timedelta
from typing import Iterable, Iterator, Sequence, Tuple, List


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def _get_datetimes(reboots: str) -> Iterator[datetime]:
    for line in reboots.splitlines():
        if not line:
            continue
        elements = line.split()
        if not elements[0].casefold() == "reboot":
            print(f"Found unknown line: {line}")
            continue
        reboot_date_string = " ".join(elements[-4:])
        yield datetime.strptime(reboot_date_string, "%a %b %d %H:%M")


def _compute_deltas(datetimes: Sequence[datetime]) -> Iterable[Tuple[timedelta, datetime]]:
    datetimes = list(datetimes)
    datetime_pairs = zip(datetimes, datetimes[1:])
    for end, start in datetime_pairs:
        yield (end - start, end)


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    uptimes = list(_compute_deltas(_get_datetimes(reboots)))
    record_delta, record_datetime = max(uptimes)
    return record_delta.days, record_datetime.replace(year=datetime.now().year).strftime("%Y-%m-%d")
