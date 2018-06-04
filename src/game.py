# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from entities.board import Board
from utils import constants
from utils.positions import gen_cells_action


def select_cell(cell, screen):
    """

    :param cell:
    :param screen:
    :return:
    """
    if cell.alive:
        cell.die(screen)
    else:
        cell.awake(screen)
    return cell


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(constants.WINSIZE)
    pygame.display.set_caption(constants.TITLE)

    # statuses
    running, playing, is_mouse_down, current_cell = True, False, False, None

    screen.fill(constants.BLACK)

    board = Board()
    board.run(screen)

    pygame.display.update()
    # main game loop

    while running:
        ev = pygame.event.get()

        for event in ev:
            print(event)
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYUP and event.key == K_ESCAPE:
                # reset
                board.reset(screen)

            elif event.type == KEYDOWN and event.key == K_SPACE:
                playing = not playing

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == constants.MOUSELEFT:
                # Draw cell event
                is_mouse_down = True
                pos = pygame.mouse.get_pos()
                current_cell = select_cell(board.get_cell(pos), screen)

            elif event.type == pygame.MOUSEMOTION and is_mouse_down:
                # Draw cell event on mousedown
                pos = pygame.mouse.get_pos()
                cell = board.get_cell(pos)
                if cell == current_cell:
                    continue
                current_cell = select_cell(cell, screen)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == constants.MOUSELEFT:
                # Stop cell drawing when mouse up
                is_mouse_down = False

        if playing:
            # Resolve Game of life rules
            actions = list(gen_cells_action(board))

            for cell, action in actions:
                getattr(cell, action)(screen)
        pygame.display.update()
        clock.tick(40)


if __name__ == '__main__':
    main()
