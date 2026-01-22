class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            self.balance = 0
        else:
            self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposited {amount} successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} successfully.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
