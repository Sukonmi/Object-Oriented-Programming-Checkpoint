# Create a new file called "bank_account.py"
# Define the Account class and its attributes as specified above.

class Account:
    def __init__(self, account_number, account_holder,  account_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance

# Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.

    def deposit(self, amount_deposited):
        self.account_balance += amount_deposited
        print(f"Alert!!!. {amount_deposited}Naira as been deposited into your account")

# Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.

    def withdraw(self, withdrawal_amount):
        if self.account_balance >= withdrawal_amount:
            self.account_balance -= withdrawal_amount
            print(f"Debit Alert!!!. {withdrawal_amount}Naira was debited from your account.")
        else:
            print("Sorry. Insufficient funds.")

# Define the check_balance() method. It should return the current account balance.

    def check_balance(self):
        print(f"Good day, {self.account_holder}. Your account balance is {self.account_balance}Naira. \n"
              "Thank you, for banking with us.")

# Create an instance of the Account class, and assign it to a variable called "my_account".
# Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
# Test the program by creating multiple instances of the class and performing different transactions on them.

my_account = Account("0155085830", "Ayomide Daniel")

my_account.deposit(100000)
my_account.withdraw(50000)
my_account.check_balance()

account2 = Account("1234567890", " Mr. Kester")
account3 = Account("0987654321", "Samuel Okon")
account4 = Account("1234509876", "Mac Donald")
account5 = Account("0987612354", "Alhaji Kaybee")

account2.deposit(20000)
account3.check_balance()
account4.withdraw(300000)
account5.deposit(250000)
account5.withdraw(100000)
account5.check_balance()