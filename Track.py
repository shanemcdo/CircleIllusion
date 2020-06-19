import pygame
import collections

Point = collections.namedtuple("Point", ['x', 'y'])

class Track:

    def __init__(self, screen: pygame.Surface, start: Point, end: Point, percentage_from_start: float, increasing: bool):
        self.screen = screen
        self.start = start
        self.end = end
        self.percentage_from_start = percentage_from_start
        self.increasing = increasing

    def draw(self) -> None:
        # pygame.draw.circle(self.screen, (255, 255, 255), self.start, 3)
        # pygame.draw.circle(self.screen, (255, 255, 255), self.end, 3)
        # pygame.draw.line(self.screen, (255, 255, 255), self.start, self.end)
        dec = self.percentage_from_start / 100
        pos = Point(
                int((1 - dec) * self.start.x + dec * self.end.x),
                int((1 - dec) * self.start.y + dec * self.end.y)
                )
        pygame.draw.circle(self.screen, (255, 0, 0), pos,10)

    def update(self, speed: float) -> None:
        if self.increasing:
            self.percentage_from_start += speed
            if self.percentage_from_start >= 100:
                self.increasing = False
        else:
            self.percentage_from_start -= speed
            if self.percentage_from_start <= 0:
                self.increasing = True
