import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def main(username: str,
    passwd: Annotated[str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)]):
    print(  f"Hello {username}. Doing something very secure with password.\n"
            f"...just kidding, here it is, very insecure: {passwd}\n",)



if __name__ == "__main__":
    app()