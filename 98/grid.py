from optparse import Option
from typing import List, Tuple, Optional
from itertools import zip_longest

import re

Position_type = Tuple[int, int, int]
Step_type = Tuple[Optional[Position_type], Optional[Position_type]]

DOWN, UP, LEFT, RIGHT, ONWARD = '⇓', '⇑', '⇐', '⇒', ''
START_VALUE = 1


def _map_str_line_to_list_ints(map_line: str) -> List[int]:
    ints_re = re.compile(r"\d+")
    return [int(x) for x in ints_re.findall(map_line)]


def _map_str_to_int_grid(map_str: str) -> List[List[int]]:
    return [map_line_ints for map_line in map_str.splitlines() if (map_line_ints := _map_str_line_to_list_ints(map_line))]


def _int_grid_to_tuples_list(map_grid: List[List[int]]) -> List[Position_type]:
    return [(map_grid[y][x], y, x) for y in range(len(map_grid)) for x in range(len(map_grid[y]))]


def _map_str_to_route_tuples(grid_str: str) -> List[Position_type]:
    int_grid = _map_str_to_int_grid(grid_str)
    route_tuples = _int_grid_to_tuples_list(int_grid)
    return sorted(route_tuples)


def _route_tuples_to_steps(route: List[Position_type]) -> List[Step_type]:
    step_pairs = list(zip(route, route[1:]))
    return step_pairs


def _break_lines_at_direction_changes(route: str) -> str:
    direction_selector = f"(?P<direction>({UP})|({DOWN})|({LEFT})|({RIGHT})) "
    route = re.sub(direction_selector, r"\g<direction>\n", route, )
    return route


def _step_tuples_to_directions(route: List[Step_type]) -> List[Tuple[int, str]]:
    res = list()
    for step in route:
        direction = None
        (cur_step, cur_row, cur_col), (next_step, next_row, next_col) = step
        # IMPROVEMENT: This could be replaced with a dictionary lookup
        if next_row < cur_row:
            direction = UP
        elif next_row > cur_row:
            direction = DOWN
        elif next_col < cur_col:
            direction = LEFT
        elif next_col > cur_col:
            direction = RIGHT
        res.append((cur_step, direction))
    return res


def _prune_directions(directions: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    res = list()
    direction_pairs = list(zip(directions[1:], directions))
    for ((cur_step, cur_direction), (prev_step, prev_direction)) in direction_pairs:
        direction_sigil = ONWARD if cur_direction == prev_direction else cur_direction
        res.append((cur_step, direction_sigil))
    res.insert(0, (1, ONWARD))
    res.append((res[-1][0]+1, ONWARD))
    return res


def _direction_tuple_to_string(direction: Tuple[int, int]) -> str:
    position, direction_sigil = direction
    if direction_sigil:
        return f"{position} {direction_sigil}"
    return str(position)


def _direction_tuples_to_strings(directions: List[Tuple[int, str]]) -> List[str]:
    return ' '.join([_direction_tuple_to_string(direction) for direction in directions])


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
    START_VALUE coordinates and move through the numbers in order printing
    them.  Each time you turn append the grid with its corresponding symbol
    (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    route = _map_str_to_route_tuples(grid)
    step_pairs = _route_tuples_to_steps(route)
    directions = _step_tuples_to_directions(step_pairs)
    pruned_directions = _prune_directions(directions)
    direction_string = _direction_tuples_to_strings(pruned_directions)
    multiline_direction_string = _break_lines_at_direction_changes(
        direction_string)
    print(multiline_direction_string)
