import entity
import image
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



player = entity.Player1("player.png",100, 100, 50, 20)
player.speed = 0.8
pl_list = pygame.sprite.Group()
pl_list.add(player)
dt = 0
while not done:
    di = ""
    lt = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                di = 'U'#player.move(dt, 'U')
            if event.key == pygame.K_DOWN:
                di = 'D'#player.move(dt, 'D')
            if event.key == pygame.K_LEFT:
                di = 'L'#player.move(dt, 'L')
            if event.key == pygame.K_RIGHT:
                di = 'R'#player.move(dt, 'R')
                print('R')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.dy = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.dx = 0
    player.move(dt, di)
    #All drawing code.
    screen.fill(WHITE)
    #screen.blit(bg,(0,0))
    #draw_box(screen, box_x, box_y, WHITE)
    #screen.blit(player.image,player.x,player.y)
    pl_list.update()
    pl_list.draw(screen)
    #Updating screen.
    pygame.display.flip()
    clock.tick(60)
    dt = pygame.time.get_ticks() - lt
    