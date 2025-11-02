"""
Pygame text rendering demonstration.

This module demonstrates how to render and display text in a pygame window
with centered positioning.
"""
# pylint: disable=no-member

import sys

import pygame


# Color constants
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)


def main() -> None:
    """
    Create pygame window and display centered text.

    Returns:
        None
    """
    pygame.init()
    screen = pygame.display.set_mode((400, 300))

    screen.fill(GRAY)

    text_font = pygame.font.SysFont("Arial", 36)
    text_surface = text_font.render("Hello, World", True, WHITE)
    screen.blit(
        text_surface,
        (200 - text_surface.get_width() // 2, 150 - text_surface.get_height() // 2)
    )

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
