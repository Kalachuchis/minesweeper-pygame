from typing import Tuple

import pygame as pg
from pygame import Rect


class MineBlock(Rect):
    def __init__(self, left: int, top: int, width: int, height: int, is_bomb: bool):
        super().__init__(left, top, width, height)
        self.is_bomb = is_bomb
        self.mouse_in_self = False
        self.is_clicked = False

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, "red", self)

    def check(self, event: pg.event.Event, mouse_pos: Tuple):
        if self.on_mouse(mouse_pos):
            if event.type == pg.MOUSEBUTTONDOWN and not self.is_clicked:
                self.inflate_ip(-4, -4)
                self.is_clicked = True
            elif event.type == pg.MOUSEBUTTONUP and self.is_clicked:
                self.open()

        if event.type == pg.MOUSEBUTTONUP and self.is_clicked:
            if(self.mouse_in_self):
                self.inflate_ip(4, 4)
            else:
                self.inflate_ip(2,2)

            self.is_clicked = False

    def open(self):
        print(self.is_bomb)

    def on_mouse(self, mouse_pos: Tuple) -> bool:
        if self.collidepoint(mouse_pos) and not self.mouse_in_self:
            if not self.is_clicked:
                self.inflate_ip(2, 2)
            self.mouse_in_self = True
        elif not self.collidepoint(mouse_pos) and self.mouse_in_self:
            if not self.is_clicked:
                self.inflate_ip(-2, -2)
            self.mouse_in_self = False

        return self.mouse_in_self
