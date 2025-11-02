"""
Pygame score display demonstration.

This module demonstrates how to display a score counter on a pygame window
using a custom font.
"""
# pylint: disable=no-member,invalid-name

import sys

import pygame


# Window dimensions
WINDOW_SIZE = (600, 600)

# Color constants
BACKGROUND_COLOR = (127, 127, 127)
WHITE = (255, 255, 255)

# Initial score - module level constant for demonstration
SCORE = 0


def show_score(
    screen: pygame.Surface, score_value: int, color: tuple, font: str, size: int
) -> None:
    """
    Display score on pygame surface.

    Args:
        screen: Pygame display surface
        score_value: Current score to display
        color: RGB color tuple for text
        font: Font name
        size: Font size

    Returns:
        None
    """
    # Creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # Create the display surface object score_surface
    score_surface = score_font.render('Score : ' + str(score_value), True, color)

    # Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # Displaying text
    screen.blit(score_surface, score_rect)


def main() -> None:
    """
    Create pygame window and display score.

    Returns:
        None
    """
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Trying show_score() Function")

    screen.fill(BACKGROUND_COLOR)
    show_score(screen, SCORE, WHITE, 'times new roman', 20)
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
