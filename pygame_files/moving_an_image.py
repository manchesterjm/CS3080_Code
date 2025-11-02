import pygame, sys

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

x_center, y_center = 200, 300

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    rect.center = x_center, y_center        
    screen.blit(image, rect)
    
    if x_center > 400:
        x_center = 200

    pygame.display.update() 

    x_center += 0.1
