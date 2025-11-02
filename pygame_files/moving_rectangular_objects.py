import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400,300))
rect1 = Rect(50, 60, 200, 80)
rect2 = rect1.copy()

white = (255, 255, 255)
x_offset, y_offset = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        rect2.move_ip(x_offset, y_offset)
        screen.fill(white)
        pygame.draw.rect(screen, (255,0,0), rect1, 1)
        pygame.draw.rect(screen, (0,0,255), rect2, 5)
        pygame.display.update()
        x_offset, y_offset = 0, 0    

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x_offset = -5
                y_offset = 0
            if event.key == K_RIGHT:
                x_offset = 5
                y_offset = 0
            if event.key == K_UP:
                x_offset = 0
                y_offset = -5
            if event.key == K_DOWN:
                x_offset = 0
                y_offset = 5
