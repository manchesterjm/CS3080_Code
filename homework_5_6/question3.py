"""
Non-whitespace character counter.

This module counts the number of non-whitespace characters in a string.
"""


def char_count(a: str) -> None:
    """
    Count and print non-whitespace characters in string.

    Args:
        a: String to count characters from

    Returns:
        None

    Example:
        >>> char_count("hello world")
        10
    """
    count = sum(1 for i in a if not i.isspace())
    print(count)


def main() -> None:
    """
    Get user input and count non-whitespace characters.

    Returns:
        None
    """
    char_count(input("Please, enter a word : "))


if __name__ == '__main__':
    main()
