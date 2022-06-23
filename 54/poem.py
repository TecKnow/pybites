INDENTS = 4


def print_hanging_indents(poem):
    lines = [line.strip() for line in poem.splitlines(keepends=True)]
    for line_number in range(len(lines)):
        if (line := lines[line_number]):
            if (previous_line_number := line_number-1) < 0 or not lines[previous_line_number]:
                print(line)
            else:
                print(f"{' ' * INDENTS}{line}")
