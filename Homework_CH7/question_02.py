"""
Upper-lowercase sequence finder.

This module searches for sequences where an uppercase letter is
followed by a lowercase letter.
"""

import re


def checker(a: str) -> bool:
    """
    Search for uppercase letter followed by lowercase letter.

    Args:
        a: String to search

    Returns:
        bool: True if pattern found, False otherwise

    Example:
        >>> checker("Python")
        True
        >>> checker("python")
        False
    """
    return bool(re.search('[A-Z][a-z]', a))


def main() -> None:
    """
    Test sequence finder with example inputs.

    Returns:
        None
    """
    input_1 = 'AaBbGg'
    input_2 = 'Python'
    input_3 = 'python'
    input_4 = 'PYTHON'
    input_5 = 'aA'
    input_6 = 'Aa'

    print(checker(input_1))
    print(checker(input_2))
    print(checker(input_3))
    print(checker(input_4))
    print(checker(input_5))
    print(checker(input_6))


if __name__ == '__main__':
    main()
