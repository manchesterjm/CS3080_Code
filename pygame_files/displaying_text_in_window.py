import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

white=(255,255,255)
gray = (127, 127, 127)
 
screen.fill(gray)

text_font = pygame.font.SysFont("Arial", 36)
text_surface = text_font.render("Hello, World", True, white)
screen.blit(text_surface,(200 - text_surface.get_width() // 2, 150 - text_surface.get_height() // 2))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     
