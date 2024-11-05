class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def bankFees(self):
        fee = 0.05 * self.balance
        self.balance -= fee
        print(f"Bank fees applied (${fee}). New balance: ${self.balance}")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    account1 = BankAccount(12046, "abhishek", 2000)
    account1.deposit(1000)
    account1.withdraw(100)
    account1.bankFees()
    account1.display()
