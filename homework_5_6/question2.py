"""
String half uppercaser.

This module converts the second half of a string to uppercase.
"""

import math


def up(a: str) -> None:
    """
    Convert second half of string to uppercase.

    Args:
        a: String to process

    Returns:
        None

    Example:
        >>> up("hello")
        heLLO
    """
    mid = math.ceil(len(a) / 2)
    a = a[:mid] + a[mid:].upper()
    print(a)


def main() -> None:
    """
    Get user input and convert second half to uppercase.

    Returns:
        None
    """
    test = input("Please, enter a word : ")
    up(test)


if __name__ == '__main__':
    main()
