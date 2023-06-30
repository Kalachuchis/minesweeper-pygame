from typing import List, Tuple

import pygame as pg

from minesweeper import Mine

SCREEN_SIZE = (720, 720)
MINE_SIZE = (20, 20)
MINE_DIMS = (10, 10)


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


class GameController:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 60
        self.mine_list = []
        self.mine_pos = get_mine_positions(MINE_DIMS, MINE_SIZE)

    def event_loop(self):
        mine: Mine
        for event in pg.event.get():
            self.mouse_pos = pg.mouse.get_pos()
            print("Mouse pos", self.mouse_pos)
            for mine in self.mine_list:
                if mine.on_mouse(self.mouse_pos):
                    print(mine)

            if event.type == pg.QUIT:
                self.running = False

    def main_loop(self):
        mine_po: Tuple
        for mine_po in self.mine_pos:
            self.mine_list.append(Mine(mine_po[0], mine_po[1], *MINE_SIZE, True))

        while self.running:
            self.event_loop()
            self.screen.fill("blue")
            for mine in self.mine_list:
                mine.draw(self.screen)
            pg.display.flip()
            self.clock.tick(self.tick)


def main():
    pg.init()
    GameController().main_loop()
    pg.quit()


if __name__ == "__main__":
    main()
