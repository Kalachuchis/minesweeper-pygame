from typing import Tuple

import pygame as pg
from pygame import Rect


class Mine(Rect):
    def __init__(self, left, top, width, height, is_bomb):
        super().__init__(left, top, width, height)
        self.is_bomb = is_bomb
        self.mouse_in_self = False

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, "red", self)

    def clicked(self):
        self.inflate_ip(-1.5, -1.5)

    def on_mouse(self, mouse_pos: Tuple) -> bool:
        if self.collidepoint(mouse_pos) and not self.mouse_in_self:
            self.inflate_ip(2, 2)
            self.mouse_in_self = True
        elif not self.collidepoint(mouse_pos) and self.mouse_in_self:
            self.inflate_ip(-2, -2)
            self.mouse_in_self = False

        return self.mouse_in_self
