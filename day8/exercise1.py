class Account:
    def init(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def str(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    def eq(self, other):
        return self.account_number == other.account_number


class SavingsAccount(Account):
    def init(self, account_number, account_holder, balance, interest_rate):
        super().init(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount >= 100:
            super().withdraw(amount)
        else:
            print("Cannot withdraw: Balance would drop below $100.")


class CheckingAccount(Account):
    def init(self, account_number, account_holder, balance, overdraft_limit):
        super().init(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            self._Accountbalance = self.get_balance() - amount
        else:
            print("Overdraft limit exceeded.")
#str → Makes printing an account human-readable.
#eq → Compares two accounts by their account_number.