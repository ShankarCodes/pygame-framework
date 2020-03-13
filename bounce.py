import pygame
pygame.init()


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

rect_x = 50
rect_y = 50

dx = 5
dy = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE,[rect_x,rect_y,50,50])
    
    if rect_x > 650 or rect_x < 0:
        dx *= -1
    if rect_y > 450 or rect_y < 0:
        dy *= -1
    
    rect_x += dx
    rect_y += dy
    pygame.display.flip()
    clock.tick(60)