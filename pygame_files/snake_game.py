"""
Classic Snake game implementation using Pygame.

This module implements a complete snake game with scoring, collision detection,
and game over functionality.
"""
# pylint: disable=no-member,consider-using-sys-exit,too-many-branches,too-many-statements

import random
import time

import pygame


# Game configuration
SNAKE_SPEED = 10

# Window dimensions
WINDOW_X = 720
WINDOW_Y = 480

# Color constants
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)


def show_score(game_window: pygame.Surface, score_value: int, color: pygame.Color,
               font: str, size: int) -> None:
    """
    Display current score on game window.

    Args:
        game_window: Pygame display surface
        score_value: Current score to display
        color: Color for score text
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
    game_window.blit(score_surface, score_rect)


def game_over(game_window: pygame.Surface, score_value: int, window_x: int, window_y: int) -> None:
    """
    Display game over screen and exit.

    Args:
        game_window: Pygame display surface
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
    game_over_rect.midtop = (window_x/2, window_y/4)

    # Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 5 seconds we will quit the program
    time.sleep(5)

    # Deactivating pygame library
    pygame.quit()

    # Quit the program
    quit()


def main() -> None:
    """
    Run the snake game main loop.

    Returns:
        None
    """
    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('GeeksforGeeks Snakes')
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # Defining snake default position
    snake_position = [100, 50]

    # Defining first 4 blocks of snake body
    snake_body = [
        [100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
    ]

    # Fruit position
    fruit_position = [
        random.randrange(1, (WINDOW_X//10)) * 10,
        random.randrange(1, (WINDOW_Y//10)) * 10
    ]

    fruit_spawn = True

    # Setting default snake direction towards right
    direction = 'RIGHT'
    change_to = direction

    # Initial score
    score = 0

    # Main game loop
    while True:

        # Handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously we don't want snake to move
        # into two directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # If fruits and snakes collide then scores will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [
                random.randrange(1, (WINDOW_X//10)) * 10,
                random.randrange(1, (WINDOW_Y//10)) * 10
            ]

        fruit_spawn = True
        game_window.fill(BLACK)

        for pos in snake_body:
            pygame.draw.rect(
                game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)
            )
        pygame.draw.rect(
            game_window, WHITE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
        )

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > WINDOW_X-10:
            game_over(game_window, score, WINDOW_X, WINDOW_Y)
        if snake_position[1] < 0 or snake_position[1] > WINDOW_Y-10:
            game_over(game_window, score, WINDOW_X, WINDOW_Y)

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, score, WINDOW_X, WINDOW_Y)

        # Displaying score continuously
        show_score(game_window, score, WHITE, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        fps.tick(SNAKE_SPEED)


if __name__ == '__main__':
    main()
