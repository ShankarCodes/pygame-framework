from . import image
from . import tile

import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect(center=(x,y))
        self.dx = 0
        self.dy = 0
        if not hasattr(self,'hp'):
            self.hp = 0
        if not hasattr(self,'ap'):
            self.ap = 0
        self.speed = 2
        self.isalive = True
        super().__init__()
        
    def damage(self,ap):
        self.hp = self.hp - ap
        if self.hp < 0:
            self.isalive = False
    
    def attack(self,other):
        other.hp = other.hp - self.ap
        if other.hp < 0:
            other.isalive = False
    
    def move(self, dt, direction):
        if direction == 'L':
            self.dx = -1
        if direction == 'R':
            self.dx = 1
        if direction == 'U':
            self.dy = -1
        if direction == 'D':
            self.dy = 1
        self.rect.y += self.speed * dt * self.dy
        self.rect.x += self.speed * dt * self.dx
    
    def set_speed(self, speed):
        self.speed = speed    

class Player(Entity):
    def __init__(self, img, x, y, hp, ap):
        self.hp = hp
        self.ap = ap
        self.block_list = None
        super().__init__(img, x, y)
    
    def update(self):
        if self.block_list is not None:
            hits = pygame.sprite.spritecollide(self, self.block_list, False)
            for block in hits:
                if isinstance(block, tile.ImpassableBlock):
                    if self.dx > 0:
                        self.rect.right = block.rect.left
                    if self.dx < 0:
                        self.rect.left = block.rect.right
                    if self.dy > 0:
                        self.rect.bottom = block.rect.top
                    if self.dy < 0:
                        self.rect.top = block.rect.bottom
     
class Enemy(Entity):
    def __init__(self, img, x, y, hp, ap):
        self.hp = hp
        self.ap = ap
        super().__init__(img, x, y)
        


