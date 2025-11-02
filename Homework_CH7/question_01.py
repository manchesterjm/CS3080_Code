"""
Lowercase underscore string validator.

This module validates strings that contain only lowercase letters
and underscores using regular expressions.
"""

import re


def str_chkr(a: str) -> bool:
    """
    Check if string contains only lowercase letters and underscores.

    Args:
        a: String to validate

    Returns:
        bool: True if string matches pattern, False otherwise

    Example:
        >>> str_chkr("hello_world")
        True
        >>> str_chkr("Hello_World")
        False
    """
    # Need the whole string to match this pattern
    # From start "^" only _ and only lower case "*" repeating to end "$"
    return bool(re.search("^[a-z_]*$", a))


def main() -> None:
    """
    Test string validator with example inputs.

    Returns:
        None
    """
    input_1 = 'aab_cbbbc'
    input_2 = 'aab_Abbbc'
    input_3 = 'Aaab_abbbc'

    print(str_chkr(input_1))
    print(str_chkr(input_2))
    print(str_chkr(input_3))


if __name__ == '__main__':
    main()
