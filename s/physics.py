import pygame

class Body(pygame.sprite.Sprite):
    def __init__(self, img, rect):
        self.image = img
        self.rect = rect
        super().__init__()
        


class GravityAffectedBody(Body):
    def __init__(self, img, rect):
        super().__init__(img, rect)
    def update(self):
        self.cupdate()
        self.rect.y += 1    
    
    def cupdate(self):
        pass