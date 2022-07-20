import argparse
from functools import reduce
from operator import add, sub, mul, truediv
from typing import List


_op_str_to_func = {"add": add, "sub": sub, "mul": mul, "div": truediv}


def calculator(operation: str, numbers: List[float]) -> float:
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    operation = _op_str_to_func[operation]
    return round(reduce(operation, numbers), 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(
        description="A simple calculator"
    )
    parser.add_argument(
        "-a",
        "--add",
        type=float,
        nargs="+",
        help="Sums numbers"
    )
    parser.add_argument(
        "-s",
        "--sub",
        type=float,
        nargs="+",
        help="Subtracts numbers"
    )
    parser.add_argument(
        "-m",
        "--mul",
        type=float,
        nargs="+",
        help="Multiplies numbers"
    )
    parser.add_argument(
        "-d",
        "--div",
        type=float,
        nargs="+",
        help="Divides numbers"
    )

    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)
