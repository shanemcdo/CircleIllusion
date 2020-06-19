import pygame
from Track import Track, Point
import numpy as np

class CircleIllusion:
    """
    Draw a circle created out of balls moving on seperate tracks using pygame
    """

    def __init__(self, width, height, radius = 280, speed = 0.05):
        self.size = Point(width, height)
        self.radius = radius
        self.speed = speed
        self.running = True
        pygame.display.init()
        pygame.display.set_caption("Circle Illusion")
        self.screen = pygame.display.set_mode(self.size)
        self.tracks = []
        self.create_tracks(50)

    def create_tracks(self, num: int) -> None:
        offset = Point(self.size.x // 2, self.size.y // 2)
        i = 0
        while i < np.pi:
            x = int(self.radius * np.cos(i))
            y = int(self.radius * np.sin(i))
            start = Point(x + offset.x, y + offset.y)
            end = Point(-x + offset.x, -y + offset.y)
            angle = i
            increasing = True
            percentage = 100 * angle / np.pi
            self.tracks.append(Track(self.screen, start, end, percentage, increasing))
            i += np.pi / num

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            for track in self.tracks:
                track.draw()
                track.update(self.speed)
            pygame.display.update()
