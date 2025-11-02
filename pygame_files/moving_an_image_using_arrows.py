"""
Pygame arrow key image movement.

This module demonstrates image movement controlled by arrow keys
(up, down, left, right).
"""
# pylint: disable=no-member,no-name-in-module

import sys

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT


# Image configuration
DEFAULT_IMAGE_SIZE = (400, 200)

# Color constants
BACKGROUND_COLOR = (127, 127, 127)


def main() -> None:
    """
    Display image controlled by arrow keys.

    Returns:
        None
    """
    image = pygame.image.load('pygame_logo.png')
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Moving Image")
    rect = image.get_rect()

    x_center, y_center = 300, 300

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            screen.fill(BACKGROUND_COLOR)
            rect.center = x_center, y_center
            screen.blit(image, rect)

            pygame.display.update()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    x_center += 5
                if event.key == K_LEFT:
                    x_center -= 5
                if event.key == K_UP:
                    y_center -= 5
                if event.key == K_DOWN:
                    y_center += 5


if __name__ == '__main__':
    main()
