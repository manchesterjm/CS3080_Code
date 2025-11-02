"""
Test utilities for prime number checking and Excel file handling.

This module demonstrates prime number validation and basic Excel file
operations using openpyxl.
"""

import math

import openpyxl


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num: Integer to check for primality

    Returns:
        bool: True if num is prime, False otherwise

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if num < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def main() -> None:
    """
    Display openpyxl version and load test workbook.

    Returns:
        None
    """
    print(openpyxl.__version__)

    wb_one = openpyxl.load_workbook('test.xlsx')
    print(wb_one.sheetnames)


if __name__ == '__main__':
    main()
