"""
Pygame game over screen demonstration.

This module demonstrates a game over function that displays the final score
and automatically exits after 5 seconds.
"""
# pylint: disable=no-member,consider-using-sys-exit,invalid-name

import time

import pygame


# Window dimensions
WINDOW_X = 600
WINDOW_Y = 600

# Color constants
RED = (255, 0, 0)

# Initial score - module level constant for demonstration
SCORE = 0


def game_over(screen: pygame.Surface, score_value: int, window_x: int, window_y: int) -> None:
    """
    Display game over screen with final score.

    Args:
        screen: Pygame display surface
        score_value: Final score to display
        window_x: Window width
        window_y: Window height

    Returns:
        None
    """
    # Creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # Creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score_value), True, RED)

    # Create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # Setting position of the text
    game_over_rect.midtop = (window_x//2, window_y//4)

    # Blit will draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 5 seconds we will quit the program
    time.sleep(5)

    # Deactivating pygame library
    pygame.quit()

    # Quit the program
    quit()


def main() -> None:
    """
    Initialize pygame and display game over screen.

    Returns:
        None
    """
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Trying game_over() Function")

    game_over(screen, SCORE, WINDOW_X, WINDOW_Y)


if __name__ == '__main__':
    main()
