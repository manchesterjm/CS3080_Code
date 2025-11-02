import pygame, sys

# initial score
score = 0

pygame.init()
# (width, height)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Trying show_score() Function")
background_color = (127,127,127)
white = (255, 255, 255)

# displaying Score function
def show_score(color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	screen.blit(score_surface, score_rect)

screen.fill(background_color)
show_score(white, 'times new roman', 20)
pygame.display.update() 

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
