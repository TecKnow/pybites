# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    nums = 0
    # your code here
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for a, b in directions:
        y = r+a
        x = c+b
        if 0 <= y < len(map_) and 0 <= x < len(map_[y]):
            nums += 1 if map_[y][x] == 0 else 0
        else:
            nums += 1
    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimiter = 0
    for row_num in range(len(map_)):
        for col_num in range(len(map_[row_num])):
            if map_[row_num][col_num] == 1:
                perimiter += get_others(map_, row_num, col_num)

    return perimiter
