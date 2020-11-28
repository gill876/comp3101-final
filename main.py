"""I/O System Game"""
import pygame
import constants


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode(constants.WINDOW_RESOLUTION)

# Caption and Icon
pygame.display.set_caption(constants.WINDOW_NAME)
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)

running = True

while  running:
    screen.fill(constants.BACKGROUND_COLOR)

    background = pygame.image.load(constants.BACKGROUND_IMAGE)
    screen.blit(background, constants.BACKGROUND_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()