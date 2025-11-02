"""
Consecutive element checker.

This module checks if a list contains three consecutive identical elements.
"""

from typing import List


def num_chkr(num_list: List[int]) -> bool:
    """
    Check if list contains three consecutive identical elements.

    Args:
        num_list: List of integers to check

    Returns:
        bool: True if three consecutive identical elements found, False otherwise

    Example:
        >>> num_chkr([1, 2, 2, 2, 3])
        True
        >>> num_chkr([1, 2, 3, 4, 5])
        False
    """
    for j in range(0, len(num_list)-3):
        if num_list[j] == num_list[j+1] and num_list[j] == num_list[j+2]:
            return True
    return False


def main() -> None:
    """
    Test consecutive element checker with example lists.

    Returns:
        None
    """
    list_1 = [-4, 9, 9, 9, 3, 8]
    list_2 = [5, 3, 3, 7, 7, -2, -2]
    list_3 = [12, 12, 12, 12, 5, 5, 5, 2, 2]

    print(num_chkr(list_1))
    print(num_chkr(list_2))
    print(num_chkr(list_3))


if __name__ == '__main__':
    main()
