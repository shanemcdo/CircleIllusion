import pygame
import collections
import numpy as  np

Point = collections.namedtuple("Point", ['x', 'y'])

class Track:

    def __init__(self, screen: pygame.Surface, center: Point, radius: float, theta: float, offset: float):
        self.screen = screen
        self.center = center
        self.radius = radius
        self.theta = theta
        self.offset = offset

    def draw(self) -> None:
        x = int(self.radius * np.cos(self.theta))
        y = 0
        pos = Point(
                int(self.center.x + np.cos(self.offset) * x - np.sin(self.offset) * y),
                int(self.center.y + np.sin(self.offset) * x + np.cos(self.offset) * y)
                )
        pygame.draw.circle(self.screen, (255, 0, 0), pos, 10)

    def update(self, speed: float) -> None:
        self.theta += speed
        if self.theta > np.pi * 2:
            self.theta = 0
