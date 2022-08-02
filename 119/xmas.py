def generate_xmas_tree(rows: int = 10) -> str:
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    max_width = 2*rows - 1
    return '\n'.join([
        ("*" * (2*row_number - 1)).center(max_width)
        for row_number in range(1, rows+1)])
