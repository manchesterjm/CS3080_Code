"""
Pygame moving image demonstration.

This module demonstrates automatic horizontal image movement with looping
when the image reaches the boundary.
"""
# pylint: disable=no-member

import sys

import pygame


# Image configuration
DEFAULT_IMAGE_SIZE = (400, 200)

# Color constants
BACKGROUND_COLOR = (127, 127, 127)


def main() -> None:
    """
    Display moving image that loops horizontally.

    Returns:
        None
    """
    image = pygame.image.load('pygame_logo.png')
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Moving Image")
    rect = image.get_rect()

    x_center, y_center = 200, 300

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        rect.center = x_center, y_center
        screen.blit(image, rect)

        if x_center > 400:
            x_center = 200

        pygame.display.update()

        x_center += 0.1


if __name__ == '__main__':
    main()
