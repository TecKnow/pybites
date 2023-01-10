import typer  # use typer.run and typer.Argument


def sum_numbers(a: int, b: int) -> int:
    """Sums two numbers"""
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"), 
    b: int = typer.Argument(..., help="The value of the second summand")) -> int:
    """CLI that allows you to add two numbers"""
    print(sum_numbers(a, b))


if __name__ == "__main__":
    typer.run(main)