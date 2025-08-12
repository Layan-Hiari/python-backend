class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        
        self.balance = balance    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"{self.owner}'s current balance: ${self.balance}")

        
account1 = BankAccount("mozan", 10)

account1.display_balance()  

account1.deposit(50)        
account1.withdraw(30)       
account1.withdraw(200)      
account1.display_balance()  

