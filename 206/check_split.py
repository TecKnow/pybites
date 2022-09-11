import re
from typing import Tuple, List
from decimal import ROUND_DOWN, ROUND_FLOOR, ROUND_UP, Decimal


float_re = re.compile(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")


def check_split(item_total: str, tax_rate: str, tip: str, people: int) -> Tuple[str, List[float]]:
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total_dec = Decimal(float_re.search(item_total)[0])
    tax_rate_dec = (Decimal(float_re.search(tax_rate)[
                    0]) / Decimal("100")) + Decimal("1")
    tip_dec = (Decimal(float_re.search(tip)[
               0]) / Decimal("100")) + Decimal("1")
    grand_total_dec = ((item_total_dec * tax_rate_dec).quantize(Decimal("1.00"))
                       * tip_dec).quantize(Decimal("1.00"))
    grand_total_str = f"${grand_total_dec}"
    splits = [(grand_total_dec / Decimal(people)
               ).quantize(Decimal("1.00"), rounding=ROUND_FLOOR)] * people
    while((delta := (grand_total_dec - sum(splits))) >= Decimal("0.01")):
        print("HELLO!")
        print(delta)
        for p in range(len(splits)):
            if grand_total_dec - sum(splits) >= Decimal("0.01"):
                splits[p] += Decimal("0.01")

    return (grand_total_str, splits)
