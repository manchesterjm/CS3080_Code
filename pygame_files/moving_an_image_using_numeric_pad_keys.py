"""
Pygame numeric keypad image movement.

This module demonstrates 8-directional image movement using the numeric
keypad keys (1-9, excluding 5).
"""
# pylint: disable=no-member,no-name-in-module

import sys

import pygame
from pygame.locals import (K_KP1, K_KP2, K_KP3, K_KP4, K_KP6, K_KP7, K_KP8,
                            K_KP9, KEYDOWN, QUIT)


# Image configuration
DEFAULT_IMAGE_SIZE = (400, 200)

# Color constants
BACKGROUND_COLOR = (127, 127, 127)


def main() -> None:
    """
    Display image controlled by numeric keypad.

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
                if event.key == K_KP1:
                    x_center -= 5
                    y_center += 5
                if event.key == K_KP2:
                    y_center += 5
                if event.key == K_KP3:
                    x_center += 5
                    y_center += 5
                if event.key == K_KP4:
                    x_center -= 5
                if event.key == K_KP6:
                    x_center += 5
                if event.key == K_KP7:
                    x_center -= 5
                    y_center -= 5
                if event.key == K_KP8:
                    y_center -= 5
                if event.key == K_KP9:
                    x_center += 5
                    y_center -= 5


if __name__ == '__main__':
    main()
