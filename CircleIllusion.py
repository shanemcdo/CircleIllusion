import pygame
from Track import Track, Point

class CircleIllusion:
    """
    Draw a circle created out of balls moving on seperate tracks using pygame
    """

    def __init__(self, width, height):
        self.size = Point(width, height)
        self.running = True
        pygame.display.init()
        pygame.display.set_caption("Circle Illusion")
        self.screen = pygame.display.set_mode(self.size)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            pygame.display.update()
