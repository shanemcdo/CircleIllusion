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
        # initial horizontal movement
        pos = Point(
                int(self.radius * np.cos(self.theta)) + self.center.x,
                self.center.y
                )
        pos = Track.rotate(self.offset, pos, self.center)
        pygame.draw.circle(self.screen, (255, 0, 0), pos, 10)

    def update(self, speed: float) -> None:
        self.theta += speed
        if self.theta > np.pi * 2:
            self.theta = 0

    @staticmethod
    def rotate(angle: float, point: Point, center: Point = Point(0, 0)) -> Point:
        return Point(
                int(center.x + np.cos(angle) * (point.x - center.x) - np.sin(angle) * (point.y - center.y)),
                int(center.y + np.sin(angle) * (point.x - center.x) + np.cos(angle) * (point.y - center.y))
                )
