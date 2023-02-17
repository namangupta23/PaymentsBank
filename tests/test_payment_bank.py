from ..AccountsDAO import AccountsDAO
from ..PaymentsBank import PaymentsBank

accounts_dao = AccountsDAO()
payments_bank = PaymentsBank(accounts_dao)
    
def test_create():
    assert payments_bank.create("Amit Dugal") == 1000
    assert payments_bank.balance(1000) == 0

    assert payments_bank.create("Naman Gupta") == 1001
    assert payments_bank.create("Gauri Kalla") == 1002
    assert payments_bank.create("Ashi Mathur") == 1003
    
def test_deposit():
    
    # Deposit 1 for 1000
    assert payments_bank.deposit(1000, 500) == "500" 
    
    # Deposit 2 for 1000
    assert payments_bank.deposit(1000, 1000) == "1500"

    assert payments_bank.deposit(1000, 100) == "Minimum deposit amount is 500"

    assert payments_bank.deposit(1000, 60000) == "Maximum deposit amount is 50,000"

    # Deposit 3 for 1000
    assert payments_bank.deposit(1000, 10000) == "11500"

    assert payments_bank.deposit(1000, 5000) == "Only 3 deposits are allowed in a day"

    # Account Balance more than 1,00,000
    assert payments_bank.deposit(1003, 50000) == "50000"
    assert payments_bank.deposit(1003, 50000) == "100000"
    assert payments_bank.deposit(1003, 50000) == "Account balance can't exceed 1,00,000"


def test_balance():
    assert payments_bank.balance(1000) == 11500

def test_withdraw():

    assert payments_bank.withdraw(1000, 500) == "Minimum withdrawl amount is 1000"
    # No change in balance check
    assert payments_bank.balance(1000) == 11500

    assert payments_bank.withdraw(1000, 50000) == "Maximum withdrawl amount is 25,000"
    # No change in balance check
    assert payments_bank.balance(1000) == 11500

    assert payments_bank.withdraw(1000, 20000) == "Insufficient Balance"
    # No change in balance check
    assert payments_bank.balance(1000) == 11500

    # Withdrawl 1 for 1000
    assert payments_bank.withdraw(1000, 1000) == "10500"
    
    # Withdrawl 2 for 1000
    assert payments_bank.withdraw(1000, 1900) == "8600"

    # Withdrawl 3 for 1000
    assert payments_bank.withdraw(1000, 1000) == "7600"

    assert payments_bank.withdraw(1000, 5000) == "Only 3 withdrawls allowed in a day"
    # No change in balance check
    assert payments_bank.balance(1000) == 7600

def test_transfer():
    # Deposit 1 for 1001
    assert payments_bank.deposit(1001, 50000) == "50000"

    # Withdrawl 1 for 1001 and Deposit 1 for 1002 and check balance of both
    assert payments_bank.transfer(1001, 1002, 5000) == "Successfull"
    assert payments_bank.balance(1001) == 45000
    assert payments_bank.balance(1002) == 5000

    # Withdrawl 2 for 1001 and Deposit 2 for 1002 and check balance of both
    assert payments_bank.transfer(1001, 1002, 5000) == "Successfull"
    assert payments_bank.balance(1001) == 40000
    assert payments_bank.balance(1002) == 10000

    # Withdrawl 3 for 1001 and Deposit 4 for 1000 and check no withdrawl or deposit is made
    assert payments_bank.transfer(1001, 1000, 10000) == "Only 3 deposits are allowed in a day for account 1000"
    assert payments_bank.balance(1001) == 40000
    assert payments_bank.balance(1000) == 7600

    # Withdrawl 3 for 1001 and Desposit 3 for 1002 and check balance of both
    assert payments_bank.transfer(1001, 1002, 10000) == "Successfull"
    assert payments_bank.balance(1001) == 30000
    assert payments_bank.balance(1002) == 20000

    # Withdrawl 4 for 1001 and check no withdrawl or deposit is made
    assert payments_bank.transfer(1001, 1002, 5000) == "Only 3 withdrawls allowed in a day for account 1001"
    assert payments_bank.balance(1001) == 30000
    assert payments_bank.balance(1002) == 20000

    # check no withdrawl or deposit is made
    assert payments_bank.transfer(1001, 1002, 500) == "Minimum withdrawl amount is 1000 for account 1001"
    assert payments_bank.balance(1001) == 30000
    assert payments_bank.balance(1002) == 20000
    
    # check no withdrawl or deposit is made
    assert payments_bank.transfer(1001, 1002, 55000) == "Maximum withdrawl amount is 25,000 for account 1001"
    assert payments_bank.balance(1001) == 30000
    assert payments_bank.balance(1002) == 20000

    assert payments_bank.transfer(1003, 1003, 5000) == "Source and Target account number can't be same"

def test_invalid_account():
    assert payments_bank.deposit(10000, 500) == "Account not found"

    assert payments_bank.balance(10000) == "Account not found"

    assert payments_bank.withdraw(10000, 500) == "Account not found"

    assert payments_bank.transfer(10000, 1000, 500) == "Source Account not found"

    assert payments_bank.transfer(1003, 10004, 1000) == "Target Account not found"
    assert payments_bank.balance(1003)