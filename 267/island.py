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
        y, x = r+a, c+b

        def _out_of_bounds():
            """Tiles off the edge of the map count as ocean 
               for the purposes of calculating island perimiter
            """
            return y < 0 or y >= len(map_) or x < 0 or x >= len(map_[y])
        nums += 1 if _out_of_bounds() or map_[y][x] == 0 else 0
    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimiter = sum((get_others(map_, row_num, col_num)
                     for row_num in range(len(map_))
                     for col_num in range(len(map_[row_num]))
                     if map_[row_num][col_num] == 1))

    return perimiter
