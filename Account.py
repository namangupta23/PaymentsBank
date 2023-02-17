from collections import deque
from datetime import datetime


def _can_make_deposit_or_withdrawal(history):
    today = datetime.today()

    while len(history) > 0 and today.date() != history[0].date():
        history.popleft()

    return len(history) < 3


class Account:

    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.account_balance = 0

        # Stores atmax last 3 deposit times
        self.last_deposit_time = deque([])

        # Stores atmax last 3 withdrawl times
        self.last_withdrawl_time = deque([])
    
    def get_account_balance(self):
        return self.account_balance

    def deposit_amount(self, amount):
        
        deposit_status, deposit_message = self.isDepositAllowed(amount)

        if not deposit_status:
            return deposit_status, deposit_message

        self.account_balance += amount
        self.last_deposit_time.append(datetime.today())

        return True, str(self.account_balance)

    def withdraw_amount(self, amount):
        withdrawl_status, withdrawl_message = self.isWithdrawlAllowed(amount)

        if not withdrawl_status:
            return withdrawl_status, withdrawl_message

        self.account_balance -= amount
        self.last_withdrawl_time.append(datetime.today())
        return True, str(self.account_balance)
    
    def rollback_withdraw(self, amount):
        if len(self.last_withdrawl_time) > 0:
            self.last_withdrawl_time.pop()
        self.account_balance += amount
        return
    
    def isWithdrawlAllowed(self, amount):
        if amount < 1000:
            return False, "Minimum withdrawl amount is 1000"

        if amount > 25000:
            return False, "Maximum withdrawl amount is 25,000"

        if not _can_make_deposit_or_withdrawal(self.last_withdrawl_time):
            return False, "Only 3 withdrawls allowed in a day"

        if self.account_balance - amount < 0:
            return False, "Insufficient Balance"
        
        return True, ""
    
    def isDepositAllowed(self, amount):
        if amount < 500:
            return False, "Minimum deposit amount is 500"

        if amount > 50000:
            return False, "Maximum deposit amount is 50,000"

        if not _can_make_deposit_or_withdrawal(self.last_deposit_time):
            return False, "Only 3 deposits are allowed in a day"

        if self.account_balance + amount > 100000:
            return False, "Account balance can't exceed 1,00,000"
        
        return True, ""
