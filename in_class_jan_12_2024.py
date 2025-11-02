"""
String right justification demonstration.

This module demonstrates string right justification with custom padding
using asterisks.
"""


def main() -> None:
    """
    Right-justify user input with asterisk padding.

    Prompts the user for their name and displays it right-justified
    with 5 additional spaces of padding using asterisks.

    Returns:
        None
    """
    userinput = input('enter you name : ')
    print('your name will be right justified 5 spaces')
    x = len(userinput)
    print(userinput.rjust(5 + x, '*'))


if __name__ == '__main__':
    main()
