import pygame

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

box_x, box_y = int(size[0]//2), int(size[1]//2)

dt = 0
dx = 0
dy = 0

speed = 0.8

spaceship = pygame.image.load("player.png").convert_alpha()

def draw_box(scr, x, y, color):
    pygame.draw.rect(scr, color, [x,y,50,50])

while not done:
    lt = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1 * speed * dt
            if event.key == pygame.K_DOWN:
                dy = 1 * speed * dt
            if event.key == pygame.K_LEFT:
                dx = -1 * speed * dt
            if event.key == pygame.K_RIGHT:
                dx = 1 * speed * dt
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                dx = 0
    
    #All calculations.
    
    if box_x + dx > 650 or box_x + dx < 0:
        dx = 0
    if box_y + dy > 450 or box_y + dy < 0:
        dy = 0
    
    box_x = box_x + dx
    box_y = box_y + dy 
    
    #All drawing code.
    screen.fill(WHITE)
    #draw_box(screen, box_x, box_y, WHITE)
    screen.blit(spaceship,(box_x,box_y))
    
    #Updating screen.
    pygame.display.flip()
    clock.tick(60)
    dt = pygame.time.get_ticks() - lt
    