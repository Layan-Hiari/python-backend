class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account_a = BankAccount("Eira", 100)
account_b = BankAccount("Sorin")

account_a.deposit(50)
account_a.withdraw(30)

account_b.deposit(200)
account_b.withdraw(250)  # won't withdraw, insufficient funds

print(account_a.get_balance())  # 120
print(account_b.get_balance())  # 200
