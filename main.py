import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1280, 720))

running = True

while  running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False