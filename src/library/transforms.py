import pygame
from pygame import Surface
from typing import *

Point = Tuple[float, float]

# Maths from https://stackoverflow.com/a/54714144/21399
def blit_rotate(
        surf: Surface,
        image: Surface,
        pos: Point,
        origin: Point,
        angle: float
        ):
    """
    Blit a rotated surface such that the origin point of the image is placed at the given position on the canvas.

    :param surf: Destination surface
    :param image: Source surface
    :param pos: Point on destination
    :param origin: Point on source to rotate around
    :param angle: Angle in degrees
    """

    def _first(p: Point) -> float: return p[0]
    def _second(p: Point) -> float: return p[1]

    # calculate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=_first)[0], min(box_rotate, key=_second)[1])
    max_box = (max(box_rotate, key=_first)[0], max(box_rotate, key=_second)[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(origin[0], -origin[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - origin[0] + min_box[0] - pivot_move[0], pos[1] - origin[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)
