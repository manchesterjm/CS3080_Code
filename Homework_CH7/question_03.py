import random

class BankAccount:
    
    _account_number = random.randint(3450, 10000)
    
    def __init__(self):
        self.account_number = BankAccount._account_number
        self.balance = 0
        BankAccount._account_number += 1
        
    def deposit(self, money):
        print(f"Added $ {money:,.2f} to account# {self.account_number}")
        self.balance += money
        
    def withrawl(self, money):
        print(f"Account# {self.account_number} lacks funds, terminating withdrawl action" if self.balance < money else f"Removed $ {money:,.2f} from account# {self.account_number}")
        self.balance = (self.balance if self.balance < money else self.balance - money)

    def __str__(self):
        return f"Account# {self.account_number} has $ {self.balance:>7,.2f}"
    
accounts = [BankAccount() for _ in range(2)]

[account.deposit(random.randint(3392, 10000)) for account in accounts]
    
for account in accounts: print(account)

[account.withrawl(random.randint(3392, 10000)) for account in accounts]
#accounts[0].withrawl(accounts[0].balance - accounts[0].balance/3), accounts[1].withrawl(accounts[1].balance + 1)

for account in accounts: print(account)