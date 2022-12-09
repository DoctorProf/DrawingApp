import pygame,sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((700, 800))
screen.fill((255,255,255))
MouseDown = False
Size=(10,10)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((randint(0,255),randint(0,255),randint(0,255)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                MouseDown = True
                a,b = event.pos[0],event.pos[1]
                pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), (a,b,Size[0],Size[1]))
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                MouseDown = False
        if event.type == pygame.MOUSEMOTION:
            if MouseDown:
                a,b = event.pos[0],event.pos[1]
                pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), (a,b,Size[0],Size[1]))

    pygame.display.update()