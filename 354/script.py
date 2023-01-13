import typer
from typing import Optional


def sum_numbers(a: int, b: int, c: Optional[int] = None) -> str:
    c_str = "None" if c is None else "smaller" if c < a + b else "not smaller"
    return f"The sum is {a +b} and c is {c_str}"


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: Optional[int] = typer.Option(
        None, help="The value to which the sum will be compared")
):
    """CLI that allows you to add two numbers"""
    print(sum_numbers(a, b, c))


if __name__ == "__main__":
    typer.run(main)
