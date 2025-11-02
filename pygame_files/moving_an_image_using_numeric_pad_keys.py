import pygame, sys
from pygame.locals import *

image = pygame.image.load('pygame_logo.png')
# (width, height)
DEFAULT_IMAGE_SIZE = (400, 200)
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

pygame.init()
# (width, height)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Moving Image")
background_color = (127,127,127)
rect = image.get_rect()

x_center, y_center = 300, 300

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        screen.fill(background_color)
        rect.center = x_center, y_center        
        screen.blit(image, rect)

        pygame.display.update()

        if event.type == KEYDOWN:
            if event.key == K_KP1:
                x_center -= 5
                y_center += 5
            if event.key == K_KP2:
                y_center += 5
            if event.key == K_KP3:
                x_center += 5
                y_center += 5
            if event.key == K_KP4:
                x_center -= 5
            if event.key == K_KP6:
                x_center += 5
            if event.key == K_KP7:
                x_center -= 5
                y_center -= 5
            if event.key == K_KP8:
                y_center -= 5
            if event.key == K_KP9:
                x_center += 5
                y_center -= 5
