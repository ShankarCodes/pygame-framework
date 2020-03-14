import pygame
from . import image
class GravityAffectedBody(pygame.sprite.Sprite):
    def __init__(self, img, initial_x, initial_y):
        self.img = image.load(img)
        self.rect = self.img.get_rect(center = (initial_x, initial_y))
    
    def update(self):
        self.rect.y += -1    