import pygame 
import pygame.gfxdraw
import time
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = 3.141592653589793

TITLE = "Shankar Game"

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(TITLE)

done = False
clock = pygame.time.Clock()

#size, bold, italics
font = pygame.font.SysFont('Calibri',25,True,False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    screen.fill(WHITE)
    
    text = font.render(f"{time.time()}",True,BLACK)
    screen.blit(text,(200,200))
    pygame.display.flip()
    clock.tick(240)