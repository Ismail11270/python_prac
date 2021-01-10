import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Chess Game")
icon = pygame.image.load("textures\\icon.png")
pygame.display.set_icon(icon)

figure = pygame.image.load("textures\\ship2.png")
figX = 0
figY = 0
pygame.transform.scale(figure, (100,100))

direction = 0
speed = 0.1;

def move(x):
    global figX, figY
    figX += x
    # screen.blit(figure, (figX, figY))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = speed
            if event.key == pygame.K_LEFT:
                direction = -speed
        if event.type == pygame.KEYUP:
            direction = 0

    move(direction)
    screen.fill((255, 255, 255))
    screen.blit(figure, (figX, figY))
    pygame.display.update()


