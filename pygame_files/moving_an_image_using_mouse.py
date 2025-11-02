"""
Pygame mouse-controlled image movement.

This module demonstrates image movement that follows the mouse cursor position.
"""
# pylint: disable=no-member,no-name-in-module,consider-using-sys-exit

import pygame
from pygame.locals import QUIT


# Image configuration
FILE_NAME = 'mouse_logo.jpg'
DEFAULT_IMAGE_SIZE = (30, 30)

# Color constants
WHITE = (255, 255, 255)


def main() -> None:
    """
    Display image that follows mouse cursor.

    Returns:
        None
    """
    image = pygame.image.load(FILE_NAME)
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Moving with mouse")

    while True:

        mouse_x_coor, mouse_y_coor = pygame.mouse.get_pos()

        screen.fill(WHITE)
        screen.blit(
            image,
            (mouse_x_coor-(.5)*DEFAULT_IMAGE_SIZE[0], mouse_y_coor-5-(.5)*DEFAULT_IMAGE_SIZE[1])
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()
