from datetime import date, timedelta
from typing import Iterator

TODAY = date.today()


def gen_bite_planning(num_bites: int = 1, num_days: int = 1, start_date: date = TODAY) -> Iterator[date]:
    num_days_delta = timedelta(days=num_days)
    current_date = start_date + num_days_delta
    while True:
        for n in range(num_bites):
            yield current_date
        current_date += num_days_delta
        
