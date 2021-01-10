import space
import pygame
import params
import random

SIZE_X = params.SIZE_X
SIZE_Y = params.SIZE_Y

pygame.init()
screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
pygame.display.set_caption("Chess Game")
icon = pygame.image.load("textures\\icon.png")

pygame.display.set_icon(icon)
background = pygame.image.load(params.background)
player = space.Player(1)

ufos = [space.Ufo([200, 0])]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.direction = [1, 0]
            if event.key == pygame.K_LEFT:
                player.direction = [-1, 0]
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.direction == [-1, 0]:
                player.direction = [0, 0]
            if event.key == pygame.K_RIGHT and player.direction == [1, 0]:
                player.direction = [0, 0]
    player.update()
    ufos[:] = [ufo for ufo in ufos if ufo.update(player.missiles)]
    screen.blit(pygame.transform.scale(background, (SIZE_X, SIZE_Y)), (0, 0))
    player.render(screen)
    for ufo in ufos:
        ufo.render(screen)
    pygame.display.update()

