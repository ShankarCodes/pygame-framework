import pygame

def load(filename):
    return pygame.image.load(filename).convert_alpha()


class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = load(filename)
    
    def get(x, y, width, height):
        image = pygame.Surface((int(width), int(height))).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
        
        