# Create a class called BankAccount to represent a basic bank account.
# The class should have the following attributes:
#  1. owner: The name of the account owner.
#  2. balance: The current balance of the account.

#  Implement the following methods:
#  1. __init__(self, owner, balance): Initializes the BankAccount object with the
#  owner's name and initial balance. Ensure that the balance is a non-negative
#  integer.
#  2. get_balance(self): Returns the current balance of the account.
#  3. deposit(self, amount): Adds the specified amount to the account balance.
#  Ensure that the amount is a positive integer.
#  4. withdraw(self, amount): Subtracts the specified amount from the account
#  balance. Ensure that the amount is a positive integer and does not exceed the
#  current balance.

#  Additionally, use @property and @attribute.setter to encapsulate the balance
#  attribute and enforce validation rules

class BankAccount:
    def __init__(self, owner, balance):
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("Balance must be a non-negative integer.")
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Balance must be a non-negative integer.")
        self._balance = value

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        print(f"Deposited ${amount}. New balance is ${self._balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f"Withdraw ${amount}. New balance is ${self._balance}.")

account = BankAccount("Alice", 500)
print(f"Account owner: {account.owner}, Balance: ${account.get_balance()}")

account.deposit(100)

account.withdraw(50)

account.withdraw(600)




