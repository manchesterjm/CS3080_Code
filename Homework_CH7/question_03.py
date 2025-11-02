"""
Bank account simulation.

This module simulates bank account operations including deposits,
withdrawals, and balance tracking with automatic account numbering.
"""

import random


class BankAccount:
    """
    Bank account with deposit, withdrawal, and balance tracking.

    Attributes:
        account_number: Unique account number
        balance: Current account balance
    """

    _account_number = random.randint(3450, 10000)

    def __init__(self):
        """Initialize bank account with unique number and zero balance."""
        self.account_number = BankAccount._account_number
        self.balance = 0
        BankAccount._account_number += 1

    def deposit(self, money: float) -> None:
        """
        Deposit money into account.

        Args:
            money: Amount to deposit

        Returns:
            None
        """
        print(f"Added $ {money:,.2f} to account# {self.account_number}")
        self.balance += money

    def withrawl(self, money: float) -> None:
        """
        Withdraw money from account if sufficient funds available.

        Args:
            money: Amount to withdraw

        Returns:
            None
        """
        if self.balance < money:
            print(f"Account# {self.account_number} lacks funds, terminating withdrawl action")
        else:
            print(f"Removed $ {money:,.2f} from account# {self.account_number}")
            self.balance = self.balance - money

    def __str__(self) -> str:
        """
        Return string representation of account.

        Returns:
            str: Account number and balance
        """
        return f"Account# {self.account_number} has $ {self.balance:>7,.2f}"


def main() -> None:
    """
    Create bank accounts and perform transactions.

    Returns:
        None
    """
    accounts = [BankAccount() for _ in range(2)]

    for account in accounts:
        account.deposit(random.randint(3392, 10000))

    for account in accounts:
        print(account)

    for account in accounts:
        account.withrawl(random.randint(3392, 10000))

    for account in accounts:
        print(account)


if __name__ == '__main__':
    main()
