# Create a new file called "bank_account.py"
# Define the Account class and its attributes as specified above.

class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

# Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.

    def deposit(self, amount_deposited):
        self.account_balance += amount_deposited
        print(f"Alert!!!. {amount_deposited}Naira as been deposited into your account")

# Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.

    def withdraw(self, withdrawal):
        if self.account_balance >= withdrawal:
            self.account_balance -= withdrawal
            print(f"Debit Alert!!!. {withdrawal}Naira was debited from your account.")
        else:
            print("Sorry. Insufficient funds.")

# Define the check_balance() method. It should return the current account balance.

    def check_balance(self):
        print(f"Good day {self.account_holder}. Your account balance is {self.account_balance}Naira. \n"
              "Thank you, for banking with us.")