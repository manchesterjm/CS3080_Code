import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Making Shapes')

red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

pygame.draw.rect(screen, red, pygame.Rect(100, 30, 60, 60), 4)

pygame.display.update()

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()