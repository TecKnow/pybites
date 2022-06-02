import random

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    default_sequences = [names, aliases, points, awake]
    sequences = default_sequences if not args else args
    for row in zip(*sequences):
        row = (str(column) for column in row)
        row = SEPARATOR.join(row)
        yield row
