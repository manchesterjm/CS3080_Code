import pygame
from pygame.locals import *

file_name = 'mouse_logo.jpg'
image = pygame.image.load(file_name)
# (width, height)
DEFAULT_IMAGE_SIZE = (30, 30)
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Moving with mouse")

white = (255, 255, 255)

while True:
   
   mouse_x_coor, mouse_y_coor = pygame.mouse.get_pos()
   
   screen.fill(white)
   screen.blit(image, (mouse_x_coor-(.5)*DEFAULT_IMAGE_SIZE[0], mouse_y_coor-5-(.5)*DEFAULT_IMAGE_SIZE[1]))
   
   pygame.display.update()

   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

