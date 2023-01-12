import time

import typer
from rich.progress import track


app = typer.Typer()


@app.command()
def progress(): 
    for value in track(range(100), description="Processing..."):
        time.sleep(0.01)
    print("Processed 100 things.")


if __name__ == "__main__":
    app()