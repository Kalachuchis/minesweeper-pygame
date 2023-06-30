from typing import Tuple

import pygame as pg

from minesweeper import MineBlock
from minesweeper.utils import get_mine_positions

SCREEN_SIZE = (720, 720)
MINE_SIZE = (20, 20)
MINE_DIMS = (10, 10)


class GameController:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 60
        self.mine_list = []
        self.mine_pos = get_mine_positions(MINE_DIMS, MINE_SIZE)

    def event_loop(self):
        mine: MineBlock
        event: pg.event.Event
        for event in pg.event.get():
            self.mouse_pos = pg.mouse.get_pos()
            for mine in self.mine_list:
                mine.check(event, self.mouse_pos)
                # if mine.on_mouse(self.mouse_pos):
                # mine.click(event)

            if event.type == pg.QUIT:
                self.running = False

    def main_loop(self):
        mine_po: Tuple
        for mine_po in self.mine_pos:
            self.mine_list.append(MineBlock(mine_po[0], mine_po[1], *MINE_SIZE, True))

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
