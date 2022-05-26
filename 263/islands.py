from copy import deepcopy


def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    grid = deepcopy(grid)
    islands = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if (element := grid[row][column]) == 1:
                islands += 1
                mark_islands(row, column, grid)
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    if grid[i][j] == 1:
        grid[i][j] = 9
        if i-1 >= 0:
            mark_islands(i-1, j, grid)
        if i+1 < len(grid):
            mark_islands(i+1, j, grid)
        if j-1 >= 0:
            mark_islands(i, j-1, grid)
        if j+1 < len(grid[i]):
            mark_islands(i, j+1, grid)
