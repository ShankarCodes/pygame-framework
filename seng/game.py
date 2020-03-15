from . import tile
from . import entity
from . import image
import pygame

class Block(pygame.sprite.Sprite,tile.Block):
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect(center=(x,y))
        super().__init__()
        tile.Block.__init__(self, x, y)
        
    
class Player(pygame.sprite.Sprite,entity.Player):
    def __init__(self,img,x,y,hp,ap):
        self.image = image.load(img)
        self.rect = self.image.get_rect(center=(x,y))
        super().__init__()
        entity.Player.__init__(self,x,y,hp,ap)
    def update(self):
     
        self.rect.x = self.x
        self.rect.y = self.y