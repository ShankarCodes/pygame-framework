import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)


class Screen:
    def __init__(self, title, x, y, fps = 60, options=None):
        if options is None:
            self.screen = pygame.display.set_mode((x, y))
        else:
            self.screen = pygame.display.set_mode((x, y),options)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.lt = pygame.time.get_ticks()
        self.dt = 0
        self.fps = fps
    def tick(self):
        self.lt = pygame.time.get_ticks()
        self.clock.tick(self.fps)
        dt = pygame.time.get_ticks() - self.lt
        return dt