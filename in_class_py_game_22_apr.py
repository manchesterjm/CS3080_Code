"""
Pygame shape drawing demonstration.

This module demonstrates basic pygame initialization, window creation,
and shape drawing functionality.
"""
# pylint: disable=invalid-name,no-member

import sys

import pygame


# Color constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def main() -> None:
    """
    Create pygame window and draw a red rectangle.

    Returns:
        None
    """
    pygame.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Making Shapes')

    pygame.draw.rect(screen, RED, pygame.Rect(100, 30, 60, 60), 4)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
