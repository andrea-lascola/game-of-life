# -*- coding: utf-8 -*-
import random

import pygame

from utils import constants
from utils.view import draw_rect


class Cell:
    def __init__(self, x, y, cell):
        self.x = x
        self.y = y
        self._cell = cell
        self.alive = False

    def __repr__(self):
        return "<Cell {0!s}, {1!s}>".format(self.x, self.y)

    @property
    def pos(self):
        return self.x, self.y

    def awake(self, screen):
        self.alive = True
        self._cell = draw_rect(screen, random.choice(constants.CELLCOLORS), constants.GRAY,
                               pygame.Rect(self.x, self.y, constants.RECT_W, constants.RECT_W), border=1)

    def die(self, screen):
        self.alive = False
        self._cell = draw_rect(screen, constants.WHITE, constants.GRAY,
                               pygame.Rect(self.x, self.y, constants.RECT_W, constants.RECT_W), border=1)
