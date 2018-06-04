# -*- coding: utf-8 -*-


def draw_rect(surface, fill_color, outline_color, rect, border=1):
    """
    Draw cells on surface
    :param surface: surface
    :param fill_color: cell color
    :param outline_color: out color
    :param rect: rect to draw
    :param border: border width
    :return: rect
    """
    surface.fill(outline_color, rect)
    surface.fill(fill_color, rect.inflate(-border * 2, -border * 2))
    return rect
