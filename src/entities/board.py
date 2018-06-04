# -*- coding: utf-8 -*-
import pygame

from entities.cell import Cell
from utils import constants
from utils.view import draw_rect


class Board:
    cells = None

    def __init__(self):
        self.cells = list()

    def run(self, screen):
        self.__draw_rects(screen)

    def reset(self, screen):
        self.cells = list()
        self.run(screen)

    def get_cell(self, pos):
        return self.cells[pos[0] // constants.RECT_W][pos[1] // constants.RECT_W]

    def __draw_rects(self, screen):
        for x in range(0, constants.WINSIZE[0], constants.RECT_W):
            vector = []
            for y in range(0, constants.WINSIZE[1], constants.RECT_W):
                vector.append(Cell(x, y,
                                   draw_rect(screen, constants.WHITE, constants.GRAY,
                                             pygame.Rect(x, y, constants.RECT_W, constants.RECT_W), border=1)
                                   )
                              )

            self.cells.append(vector)

    def gen_cells(self):
        for vector in self.cells:
            for cell in vector:
                yield cell

    @classmethod
    def from_cells(cls, cells):
        instance = cls()
        instance.cells = cells
        return instance
