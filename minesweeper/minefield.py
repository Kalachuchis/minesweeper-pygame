from typing import List, Tuple

import numpy as np
import pygame as pg

from minesweeper.mine import MineBlock

MINE_SIZE = (20, 20)


class MineField:
    def __init__(
        self, mine_dimensions: Tuple, field_dimensions: Tuple, num_of_mines: int
    ):
        self.mine_dimensions = mine_dimensions
        self.field_dimensions = field_dimensions
        self.num_of_mines = num_of_mines

    def draw_mine_field(self, mine_list: List[MineBlock], screen: pg.Surface):
        pass

    def generate_mine_field(self):
        mine_locations = self.generate_mine_locations()
        mine_block_positions = self.generate_mine_block_positions()

        mine_list = [
            MineBlock(x, y, *MINE_SIZE, location)
            for (x, y), location in zip(mine_block_positions, mine_locations.flatten())
        ]

        self.mine_list = mine_list
        self.generate_observer_relations()
        return self

    def generate_observer_relations(self):
        # convert self.mine_list into an array with the dimensions of self.field_dimensions
        nd_mine_field = [
            self.mine_list[index : index + self.field_dimensions[1]]
            for index, _ in enumerate(self.mine_list[:: self.field_dimensions[0]])
        ]

        kernel_list = []
        for y, row in enumerate(nd_mine_field):
            for x, _ in enumerate(row):
                top = max(0, y - 1)
                bottom = min(y + 2, self.field_dimensions[1])
                left = max(0, x - 1)
                right = min(x + 2, self.field_dimensions[0])
                kernel_list.append(
                    [new_row[left:right] for new_row in nd_mine_field[top:bottom]]
                )

        for index, (kernel, center) in enumerate(zip(kernel_list, self.mine_list)):
            flattened_mine_list = [mine for row in kernel for mine in row]
            for mine in flattened_mine_list:
                center.add_abserver(mine)

    def generate_mine_locations(self) -> np.ndarray:
        total = np.prod(self.field_dimensions)
        prob = self.num_of_mines / total
        return np.random.choice([0, 1], size=self.field_dimensions, p=[1 - prob, prob])

    def generate_mine_block_positions(self) -> List[Tuple]:
        positions = []
        pad = 10
        gap = 5

        for x in range(self.field_dimensions[0]):
            for y in range(self.field_dimensions[1]):
                x_curr = pad + (self.mine_dimensions[0] * x) + (gap * x)
                y_curr = pad + (self.mine_dimensions[1] * y) + (gap * y)

                positions.append((x_curr, y_curr))

        return positions
