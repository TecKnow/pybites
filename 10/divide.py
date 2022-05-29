def positive_divide(numerator, denominator):
    try:
        res = numerator / denominator
    except ZeroDivisionError:
        res = 0
    if res < 0:
        raise ValueError()
    return res
