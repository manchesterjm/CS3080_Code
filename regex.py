"""
Phone number pattern detector.

This module demonstrates basic pattern matching for phone numbers in the
format XXX-XXX-XXXX without using regular expressions.
"""
# pylint: disable=too-many-return-statements


def is_phone_number(text: str) -> bool:
    """
    Check if text matches phone number format XXX-XXX-XXXX.

    Args:
        text: String to check for phone number format

    Returns:
        bool: True if text matches phone number format, False otherwise

    Example:
        >>> is_phone_number("415-555-1234")
        True
        >>> is_phone_number("not-a-phone")
        False
    """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def main() -> None:
    """
    Search for phone numbers in a message string.

    Returns:
        None
    """
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)


if __name__ == '__main__':
    main()
