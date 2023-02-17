from .AccountsDAO import AccountsDAO

class PaymentsBank:
    
    def __init__(self, accounts_dao: AccountsDAO):
        self.accounts_dao = accounts_dao
    
    
    def create(self, full_name):
        return self.accounts_dao.create_account(full_name)
    
    def deposit(self, account_number, amount):
        account = self.accounts_dao.get_account_details(account_number)

        if not account:
            return "Account not found"

        _, deposit_message = account.deposit_amount(amount)
        return deposit_message
    
    def withdraw(self, account_number, amount):
        account = self.accounts_dao.get_account_details(account_number)

        if not account:
            return "Account not found"
        
        _, withdraw_message = account.withdraw_amount(amount)
        return withdraw_message
    
    def balance(self, account_number):
        account = self.accounts_dao.get_account_details(account_number)

        if not account:
            return "Account not found"

        return account.get_account_balance()
    
    def transfer(self, source_account_number, target_account_number, amount):
        source_account = self.accounts_dao.get_account_details(source_account_number)
        
        if not source_account:
            return "Source Account not found"
        
        target_account = self.accounts_dao.get_account_details(target_account_number)

        if not target_account:
            return "Target Account not found"
        
        if source_account_number == target_account_number:
            return "Source and Target account number can't be same"
        
        withdraw_status, withdraw_message = source_account.isWithdrawlAllowed(amount)

        if not withdraw_status:
            # Withdrawl failed
            return f"{withdraw_message} for account {source_account_number}"
        
        deposit_status, deposit_message = target_account.isDepositAllowed(amount)

        if not deposit_status:
            # Depoit failed
            return f"{deposit_message} for account {target_account_number}"
        
        source_account.withdraw_amount(amount)
        target_account.deposit_amount(amount)
        return "Successfull"
        


        
        


        
        
     

