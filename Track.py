import pygame
import collections
import numpy as  np

Point = collections.namedtuple("Point", ['x', 'y'])

class Track:
    """
    Draw a point moving along a track at a certain offset angle
    """

    def __init__(self, screen: pygame.Surface, center: Point, radius: float, theta: float):
        self.screen = screen
        self.center = center
        self.radius = radius
        self.theta = theta
        self.offset = theta

    def draw_line(self) -> None:
        # get points for line
        start = Point(
                int(self.center.x + np.cos(self.offset) * self.radius),
                int(self.center.y + np.sin(self.offset) * self.radius)
                )
        end = Point(
                self.center.x - (start.x - self.center.x),
                self.center.y - (start.y - self.center.y),
                )
        # draw line
        pygame.draw.circle(self.screen, (128, 128, 128), start, 3)
        pygame.draw.circle(self.screen, (128, 128, 128), end, 3)
        pygame.draw.line(self.screen, (128, 128, 128), start, end)

    def draw_point(self) -> None:
        # get main point
        pos = Point(
                int(self.radius * np.cos(self.theta)) + self.center.x,
                self.center.y
                )
        pos = Track.rotate(self.offset, pos, self.center)
        # draw main point
        pygame.draw.circle(self.screen, Track.get_color(self.offset), pos, 10)

    def draw(self) -> None:
        self.draw_line()
        self.draw_point()

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

    @staticmethod
    def get_color(angle: float) -> pygame.Color:
        color = pygame.Color(0, 0, 0)
        color.hsva = (angle * 2 / np.pi * 180, 100, 100, 100)
        return color
