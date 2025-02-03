# Define a class named """BankAccount""" with an """__init__""" method
# that initializes two instance variables: """account_holder""" and """balance""".

# The class has methods like """deposit""" and """withdraw""",
# each of which takes an amount as an argument and updates the account balance accordingly.
# These methods also include checks for valid input and available funds.

# The """get_balance""" method allows you to retrieve the account balance.

# We create an Object of the """BankAccount""" class called """account1""" with an initial balance of $1000.

# We deposit $500 and withdraw $200 from the account and print the account information.


class BankAccount:

    def __init__(self, account_holder, balance):
        self.holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount <=0 :
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdraw ${amount}. New balance is ${self.balance}.")

    def get_balance(self):
        return self.balance

account1 = BankAccount("John", 1000)

account1.deposit(500)
account1.withdraw(200)

print(f"Account holder: {account1.holder}")
print(f"Final balance: ${account1.get_balance()}")





