"""
Penny doubling calculator.

This module calculates the compound growth of starting with 1 penny
and doubling the amount each day for 30 days.
"""


def main() -> None:
    """
    Calculate and display daily totals from penny doubling over 30 days.

    Starting with $0.01 on day 1, the amount doubles each subsequent day.
    Displays a formatted table showing the daily addition and running total.

    Returns:
        None
    """
    start = 0.01
    my_money = 0.01
    print('       :        Start            Add           Total')
    print('----------------------------------------------------')
    print(f"Day  1 :         0.00 + {start:>12,.2f} = {my_money:>13,.2f}")
    for i in range(2, 31):
        start = 2 * start
        print(f"Day {i:>2} : {my_money:>12,.2f} + {start:>12,.2f} = {my_money + start:>13,.2f}")
        my_money += start


if __name__ == '__main__':
    main()
