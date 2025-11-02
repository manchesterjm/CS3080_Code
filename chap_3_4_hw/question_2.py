"""
List merger and sorter.

This module merges two lists and returns the sorted result.
"""

from typing import List


def merge_list(a: List[int], b: List[int]) -> List[int]:
    """
    Merge and sort two lists.

    Args:
        a: First list of integers
        b: Second list of integers

    Returns:
        List[int]: Sorted merged list

    Example:
        >>> merge_list([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    temp_list = a + b
    temp_list.sort()
    return temp_list


def main() -> None:
    """
    Test list merger with example lists.

    Returns:
        None
    """
    list_1 = [1, 3, 5, 7]
    list_2 = [2, 4, 6, 8]
    list_3 = [0, 7, 9, 12]
    list_4 = [0, 1, 2, 3, 4, 7, 12]

    print(merge_list(list_1, list_2))
    print(merge_list(list_3, list_4))


if __name__ == '__main__':
    main()
