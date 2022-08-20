from operator import add, sub, mul, truediv

operator_dict = dict(zip("+ - * /".split(), (add, sub, mul, truediv)))


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    a, opp, b = calculation.split()
    a, b = int(a), int(b)
    opp_func = operator_dict.get(opp)
    if opp_func is None:
        raise ValueError(f"Unsupported operation: {opp}")
    try:
        return opp_func(a, b)
    except ZeroDivisionError:
        raise ValueError(f"Division by zero is undefined and unsupported")
