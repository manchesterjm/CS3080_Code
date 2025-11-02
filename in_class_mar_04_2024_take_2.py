"""
Exception handling demonstration.

This module demonstrates basic exception handling for division by zero errors.
"""


def a_func(a: float, b: float) -> None:
    """
    Attempt division and handle exceptions.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        None
    """
    try:
        a / b
    except Exception:  # pylint: disable=broad-exception-caught
        print('we found an exception')


def main() -> None:
    """
    Execute division with exception handling.

    Returns:
        None
    """
    a_func(1, 0)


if __name__ == '__main__':
    main()
