from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')

RED = State("red", "Stop", 2)
YELLOW = State("amber", "Caution", 0.5)
GREEN = State("green", "Go", 2)

LIGHT_CYCLE = RED, GREEN, YELLOW
LIGHT_CYCLE_INFINITE = cycle(LIGHT_CYCLE)


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    return LIGHT_CYCLE_INFINITE


if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
