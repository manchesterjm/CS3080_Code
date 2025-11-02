"""
Random list element selector.

This module returns a random element from a given list.
"""

from random import randint
from typing import List, TypeVar


T = TypeVar('T')


def rtn_rnd(a: List[T]) -> T:
    """
    Return a random element from list.

    Args:
        a: List of elements

    Returns:
        T: Randomly selected element from list

    Example:
        >>> result = rtn_rnd([1, 2, 3, 4, 5])
        >>> result in [1, 2, 3, 4, 5]
        True
    """
    return a[randint(0, len(a) - 1)]


def main() -> None:
    """
    Test random element selector with example lists.

    Returns:
        None
    """
    list_1 = [5, -9, 70, 15]
    list_2 = [0, 1, 2, 3, 4, 7, 12]

    print(rtn_rnd(list_1))
    print(rtn_rnd(list_2))


if __name__ == '__main__':
    main()
