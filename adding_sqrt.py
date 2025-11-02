"""
Square root summation calculator.

This module calculates the sum of square roots from 0 to 100 using NumPy.
"""

import numpy as np


def main() -> None:
    """
    Calculate and display the sum of square roots from 0 to 100.

    Computes the sum of sqrt(i) for i in range [0, 100] and compares it
    to the analytical approximation 2000/3.

    Returns:
        None
    """
    a = 0

    for i in range(101):
        a += np.sqrt(i)

    print(a)
    print(2000/3)


if __name__ == '__main__':
    main()
