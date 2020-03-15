import pygame
from . import image

class Block(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect(center=(x,y))
        super().__init__()

class ImpassableBlock(Block):
    def __init__(self, img, x, y):
        super().__init__(img, x, y) 
        

class GravityAffectedBlock(ImpassableBlock):
    def __init__(self, img, x, y):
        super().__init__(img, x, y) 
    
    def update(self):
        self.rect.y+=2