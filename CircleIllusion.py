import pygame
from Track import Track, Point

class CircleIllusion:
    """
    Draw a circle created out of balls moving on seperate tracks using pygame
    """

    def __init__(self, width, height, speed = 0.05):
        self.size = Point(width, height)
        self.speed = speed
        self.running = True
        pygame.display.init()
        pygame.display.set_caption("Circle Illusion")
        self.screen = pygame.display.set_mode(self.size)
        self.track = Track(self.screen, Point(30, 300), Point(570, 300), 0)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self.track.draw()
            self.track.update(self.speed)
            pygame.display.update()
