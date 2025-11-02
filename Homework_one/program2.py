"""
Leap year calculator.

This module determines if a given year is a leap year based on standard rules:
- Divisible by 4 is a leap year
- Unless divisible by 100 (not a leap year)
- Unless also divisible by 400 (is a leap year)
"""


def main() -> None:
    """
    Get year from user and determine if it is a leap year.

    Returns:
        None
    """
    input_year = int(input('Please, enter the (in YYYY format): '))
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print('This is a leap year')
        else:
            print('This is not a leap year')
    elif input_year % 4 == 0:
        print('This is a leap year')
    else:
        print('This is not a leap year')


if __name__ == '__main__':
    main()
