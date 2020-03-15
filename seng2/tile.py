import pygame
from . import image

class Block(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect(center=(x,y))
        super().__init__()
    