import pygame
from seng2 import entity
from seng2 import tile
from seng2.create import *

pygame.init()

size = (700,500)

done = False
screen = Screen("Shankar", 700, 500, 30)


player = entity.Player("player.png",100, 100, 50, 20)
player.speed = 0.8

pl_list = pygame.sprite.Group()
pl_list.add(player)

bl_list = pygame.sprite.Group()
all = pygame.sprite.Group()

blk = tile.ImpassableBlock("blk.png",200,200)
blk1 = tile.GravityAffectedBlock("blk.png",250,200)
bl_list.add(blk)
bl_list.add(blk1)

all.add(blk)
all.add(player)
all.add(blk1)
player.block_list = bl_list
dt = 0
while not done:
    di = ""
    
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
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.dy = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.dx = 0
    player.move(dt, di)
    #All drawing code.
    screen.screen.fill(WHITE)
    #screen.blit(bg,(0,0))
    #draw_box(screen, box_x, box_y, WHITE)
    hit = pygame.sprite.spritecollide
    #screen.blit(player.image,player.x,player.y)
    pl_list.update()
    bl_list.update()
    all.draw(screen.screen)
    #Updating screen.
    pygame.display.flip()
    dt = screen.tick()
    