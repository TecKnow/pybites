VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        input_string = input()
        input_lower = input_string.lower()
        if input_lower == "quit":
            print("bye")
            break
        elif input_lower in VALID_COLORS:
            print(input_lower)
        else:
            print("Not a valid color")
            continue;