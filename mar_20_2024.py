"""
Birthday countdown calculator.

This module calculates and displays the number of days remaining until a specific future date.
"""

import datetime


def main() -> None:
    """
    Calculate and display days until a future birthday.

    Computes the time difference between the current date and a target date
    (July 11, 2026) and displays the countdown in days.

    Returns:
        None
    """
    future = datetime.datetime(2026, 7, 11)
    print(f"my birthday {future}")
    now = datetime.datetime.now()
    print(f"time now {now}")
    # Time to that date
    print(f"{(future - now).days} days until my birthday")


if __name__ == '__main__':
    main()
