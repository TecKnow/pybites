from datetime import date, datetime
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """

    monthly_prices = dict()
    for movie_rented in renting_history:
        year_month_str = movie_rented.date.strftime("%Y-%m")
        monthly_prices[year_month_str] = monthly_prices.get(
            year_month_str, 0) + movie_rented.price

    res = {k: RENT if v <= STREAMING_COST_PER_MONTH else STREAM for k,
           v in monthly_prices.items()}
    print(res)
    return res
