import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()


@app.command()
def myTable():
    myTable: Table = Table(title="Star Wars Movies")

    myTable.add_column("Name")
    myTable.add_column("Favorite Tool/Framework")

    myTable.add_row("Bob", "Vim")
    myTable.add_row("Julian", "Flask")
    myTable.add_row("Robin", "VS Code")

    console = Console()
    console.print(myTable)


if __name__ == "__main__":
    app()
