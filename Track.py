import pygame
import collections

Point = collections.namedtuple("Point", ['x', 'y'])

class Track:

    def __init__(self, screen: pygame.Surface, start: Point, end: Point, dist_from_start: float):
        self.screen = screen
        self.start = start
        self.end = end
        self.dist_from_start = dist_from_start
