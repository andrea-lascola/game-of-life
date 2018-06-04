# -*- coding: utf-8 -*-
import collections

from utils import constants

positions = collections.namedtuple('positions', constants.posValues)


def get_adiacent(pos):
    """
    Get Adiacent position
    :param pos: array [x,y]
    :return: positions
    """
    x, y = pos

    def calc(_x, _y):
        return None if any((
            0 > _x or _x >= constants.WINSIZE[0],
            0 > _y or _y >= constants.WINSIZE[1]
        )) else (_x, _y)

    return positions(
        top=calc(x, y - constants.RECT_W),
        left=calc(x - constants.RECT_W, y),
        bottom=calc(x, y + constants.RECT_W),
        right=calc(x + constants.RECT_W, y),
        topleft=calc(x - constants.RECT_W, y + constants.RECT_W),
        topright=calc(x + constants.RECT_W, y + constants.RECT_W),
        bottomleft=calc(x - constants.RECT_W, y - constants.RECT_W),
        bottomright=calc(x + constants.RECT_W, y - constants.RECT_W),
    )


def gen_cells_action(board):
    """
    Game of life game rules
    :param board: board Obj
    """
    for cell in board.gen_cells():
        poss = get_adiacent(cell.pos)
        adiacent_pos = filter(None, map(lambda x: getattr(poss, x), constants.posValues))
        adiacent_active_cells = filter(None, map(lambda x: board.get_cell(x).alive, adiacent_pos))

        if cell.alive:
            if len(adiacent_active_cells) < 2:
                yield (cell, 'die')
            elif len(adiacent_active_cells) > 3:
                yield (cell, 'die')
        else:
            if len(adiacent_active_cells) == 3:
                yield (cell, 'awake')
