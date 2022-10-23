from decimal import ROUND_CEILING, Decimal


def round_to_next(number: int, multiple: int) -> int:
    dec_num = Decimal(number)
    dec_mul = Decimal(multiple)
    dec_div = dec_num / dec_mul
    dec_div = dec_div.quantize(Decimal("1"), rounding=ROUND_CEILING)
    return int(dec_div * dec_mul)
