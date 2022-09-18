WHITE, BLACK = ' ', '#'


def create_chessboard(size: int=8) -> None:
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    even_row = [WHITE, BLACK]
    odd_row = [BLACK, WHITE]
    column_steps = size//2
    for r in range(size):
        if r % 2 == 0:
            print("".join(even_row * column_steps))
        else:
            print("".join(odd_row * column_steps))
pass