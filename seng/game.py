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
        self.block_list = None
        super().__init__()
        entity.Player.__init__(self,x,y,hp,ap)
    def update(self):
        self.rect.x = self.x
        if self.block_list is not None:
            hits = pygame.sprite.spritecollide(self, self.block_list, False)
            for block in hits:
                if self.dx > 0:
                    self.rect.right = block.rect.left
                if self.dx < 0:
                    self.rect.left = block.rect.right
        
        self.rect.y = self.y