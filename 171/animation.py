from itertools import cycle
from math import ceil
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    spinner_state_cycle = cycle(SPINNER_STATES)
    for i, step in enumerate(spinner_state_cycle):
        if i * STATE_TRANSITION_TIME >= seconds:
            break
        print(f"\r{step}", end='', flush=True)
        sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(1.2)
