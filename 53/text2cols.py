from pprint import pprint
from textwrap import wrap, fill
from itertools import zip_longest

COL_WIDTH = 20


def text_to_columns(text: str) -> str:
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    padded_paragraphs = [line.strip() for line in text.split("\n\n")]
    paragraphs = [wrap(paragraph, width=COL_WIDTH)
                  for paragraph in padded_paragraphs]
    paragraphs = [[line.ljust(COL_WIDTH) for line in paragraph]
                  for paragraph in paragraphs]
    output_parts = zip_longest(*paragraphs, fillvalue="".ljust(COL_WIDTH))
    formatted_text = "\n".join((" ".join(row) for row in output_parts))
    return formatted_text


if __name__ == "__main__":
    text = """My house is small but cosy.

            It has a white kitchen and an empty fridge.

            I have a very comfortable couch, people love to sit on it."""

    print(text_to_columns(text))
