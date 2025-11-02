"""
Logging configuration demonstration.

This module demonstrates basic logging configuration and a simple loop
with console output.
"""

import logging


# Configure logging
logging.basicConfig(
    filename='errorlog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def looper(n: int) -> None:
    """
    Print numbers from 0 to n inclusive.

    Args:
        n: Upper limit for loop (inclusive)

    Returns:
        None

    Example:
        >>> looper(5)
        0
        1
        2
        3
        4
        5
    """
    for i in range(n+1):
        print(i)


def main() -> None:
    """
    Execute loop demonstration.

    Returns:
        None
    """
    looper(20)


if __name__ == '__main__':
    main()
