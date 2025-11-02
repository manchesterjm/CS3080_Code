"""
Name repetition and age calculator.

This module prompts for user name and age, displays the name five times,
and calculates age after 5 years.
"""


def main() -> None:
    """
    Get user name and age, display name repeatedly and calculate future age.

    Returns:
        None
    """
    name = input('Please, enter your name: ')
    age = int(input('Please, enter you age: '))
    newage = age + 5
    print(f'{name} {name} {name} {name} {name}')
    print(f'Your age after 5 years: {newage}')


if __name__ == '__main__':
    main()
