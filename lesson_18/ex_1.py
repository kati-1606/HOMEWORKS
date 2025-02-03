# Exercise: Bank Account Hierarchy

# Create a hierarchy of classes representing different types of bank accounts.

# Start  with a base class called BankAccount.
# Then, create two subclasses, SavingsAccount and CheckingAccount.
# Each subclass should inherit from the BankAccount class.

# ● TheBankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance

# ● TheSavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.

# ● TheCheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdraw ${amount}. New balance is ${self.balance}.")

    def get_balance(self):
        return self.balance


class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0 :
            raise ValueError("Deposit amount must be greater than zero.")
        interest = amount * (self.interest_rate / 100)
        self.balance += amount + interest
        print(f"Deposited ${amount} with ${interest} interest. New balance is ${self.balance}.")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.balance:
            self.balance -= (amount + self.overdraft_fee)
            print(f"Overdraft! Withdrawn ${amount} with ${self.overdraft_fee} overdraft fee. New balance is ${self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance is ${self.balance}.")

savings = SavingAccount("SA123", 1000, 5)  # 5% interest rate
checking = CheckingAccount("CA123", 500, 35)  # $35 overdraft fee

savings.deposit(100)
print(savings.get_balance())

checking.withdraw(600)
print(checking.get_balance())
