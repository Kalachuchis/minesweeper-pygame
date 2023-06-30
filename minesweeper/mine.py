from typing import Tuple

import pygame as pg
from pygame import Rect


class Mine(Rect):
    def __init__(self, left, top, width, height, is_bomb):
        super().__init__(left, top, width, height)
        self.is_bomb = is_bomb
        self.not_on_mouse = True

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, "red", self)

    def clicked(self):
        self.inflate_ip(-1.5, -1.5)

    def on_mouse(self, mouse_pos: Tuple):
        print("og", self)
        if self.collidepoint(mouse_pos) and self.not_on_mouse:
            self.inflate_ip(2, 2)
            self.not_on_mouse = False
        elif not self.collidepoint(mouse_pos) and not self.not_on_mouse:
            self.inflate_ip(-2, -2)
            self.not_on_mouse = True
