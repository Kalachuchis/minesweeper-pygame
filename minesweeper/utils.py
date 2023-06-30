from typing import List, Tuple


def get_mine_positions(mine_dimension: Tuple, mine_size: Tuple) -> List:
    positions = []
    pad_left = 10
    pad_top = 10
    gap = 5

    for x in range(mine_dimension[0]):
        for y in range(mine_dimension[1]):
            x_curr = pad_left + (mine_size[0] * x) + (gap * x)
            y_curr = pad_top + (mine_size[1] * y) + (gap * y)

            positions.append((x_curr, y_curr))

    return positions
