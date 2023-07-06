from typing import Tuple

import pygame as pg

from minesweeper import MineBlock, MineField
from minesweeper.utils import get_mine_positions

SCREEN_SIZE = (720, 720)
FIELD_SIZE = (10, 10)
MINE_SIZE = (20, 20)


class GameController:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 60
        self.mine_field = MineField(MINE_SIZE, FIELD_SIZE, 10).generate_mine_field()
        self.mine_list = self.mine_field.mine_list
        self.mine_pos = get_mine_positions(FIELD_SIZE, MINE_SIZE)

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
    # print(MineField(MINE_SIZE, FIELD_SIZE, 10).generate_mine_locations())
