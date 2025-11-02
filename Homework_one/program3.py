"""
Descending star triangle pattern generator.

This module creates a descending triangle pattern using asterisks
based on user input.
"""


def main() -> None:
    """
    Get user input and print descending star triangle pattern.

    Returns:
        None
    """
    int_num = int(input('Please, enter the value of n: '))
    if int_num <= 0:
        print('Invalid Input')
    else:
        for i in range(0, int_num):
            for _ in range(0, int_num - i):
                print('* ', end='')
            print()


if __name__ == '__main__':
    main()
