from .Account import Account

class AccountsDAO:

    def __init__(self, start_account_number = 1000):
        self.start_account_number = start_account_number
        self.account_number_to_account_dict = {}
    
    def create_account(self, full_name):
        new_account_number = self._get_new_account_number()
        new_account = Account(full_name, new_account_number)

        self._add_account_to_dict(new_account_number, new_account)
        return new_account_number
    
    # Function to get a new account number.
    # Here a very simple function has been used
    # The logic inside the function can be changed without affecting anything
    def _get_new_account_number(self):
        self.start_account_number += 1
        return self.start_account_number - 1
    
    # Currently all accounts are being stored in a dict
    # In a production environment we'll store the accounts in db
    def _add_account_to_dict(self, account_number, account):
        self.account_number_to_account_dict[account_number] = account
        return
    
    def get_account_details(self, account_number) -> Account:
        return self.account_number_to_account_dict.get(account_number)
