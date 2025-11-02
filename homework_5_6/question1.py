"""
Duplicate character finder.

This module finds and displays duplicate characters in a string.
"""

from typing import Dict


def dup_chk(a: str) -> None:
    """
    Find and print duplicate characters in string.

    Args:
        a: String to check for duplicate characters

    Returns:
        None

    Example:
        >>> dup_chk("hello")
        l
    """
    a = a.lower()
    dict1: Dict[str, int] = {}
    for i in a:
        dict1[i] = dict1.get(i, 0) + 1
    print(*(key for key, value in dict1.items() if value >= 2), end=' ')
    print('')


def main() -> None:
    """
    Test duplicate character finder with example strings.

    Returns:
        None
    """
    string_1 = "hello"
    string_2 = "abcCdbB"
    string_3 = "abcdefghiJKL"

    dup_chk(string_1)
    dup_chk(string_2)
    dup_chk(string_3)


if __name__ == '__main__':
    main()
