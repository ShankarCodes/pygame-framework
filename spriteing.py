import pygame
import random
from sengine import physics
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

TITLE = "Shankar Moves Box"

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(TITLE)

done = False
clock = pygame.time.Clock()

class Ball(physics.GravityAffectedBody):
    def __init__(self,x,y):
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        
        super().__init__(self.image,self.rect)
        
    def cupdate(self):
        self.check_bounce()
        #self.rect.x +=self.dx
        #self.rect.y +=self.dy
    def check_bounce(self):
        if self.rect.x > 600 or self.rect.x < 0:
            self.rect.x = 600
        if self.rect.y > 400 or self.rect.y < 0:
            self.rect.y = 400
ball = Ball(200,200)
ball_list = pygame.sprite.Group()
ball_list.add(ball)

while not done:
    lt = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = pygame.mouse.get_pos()
                ball_list.add(Ball(x,y))
            if event.button == 3:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in sprites if ball_list.rect.collidepoint(pos)]
                clicked_sprites.remove()
 
    
    ball_list.draw(screen)
    ball_list.update()
    
    pygame.display.flip()
    clock.tick(60)