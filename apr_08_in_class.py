"""
Checkerboard pattern generator.

This module creates a checkerboard pattern using NumPy arrays with user-specified dimensions.
"""

import numpy as np


def main() -> None:
    """
    Generate and display a checkerboard pattern.

    Prompts the user for board dimensions and creates a checkerboard pattern
    using NumPy array slicing with alternating 0s and 1s.

    Returns:
        None
    """
    num = int(input("Please enter the dimension of the board : "))

    board = np.zeros((num, num))
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    print(board)


if __name__ == '__main__':
    main()
