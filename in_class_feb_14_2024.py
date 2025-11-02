"""
Regular expression pattern matching demonstration.

This module demonstrates using regular expressions to find words
containing specific patterns within a test string.
"""

import re


def find_pat(string: str, pat: str) -> re.Match:
    """
    Find pattern in string using regular expression.

    Args:
        string: String to search
        pat: Regular expression pattern to find

    Returns:
        re.Match: Match object if pattern found, None otherwise

    Example:
        >>> result = find_pat("testing string", r"\\w*ring\\w*")
        >>> print(result)
    """
    a = re.search(pat, string)
    return a


def main() -> None:
    """
    Search for words containing 'ring' in test string.

    Returns:
        None
    """
    patrn = r"\w*ring\w*"
    test = "this is a tent string with a prize in it and it is the best"

    print(find_pat(test, patrn))
    print(bool(find_pat(test, patrn)))


if __name__ == '__main__':
    main()
