from itertools import chain

STAR = '*'


def gen_rhombus(width: int) -> str:
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    row_widths = chain(range(1, width+1, 2), range(width-2, 0, -2))
    for current_width in row_widths:
        yield (STAR * current_width).center(width)
