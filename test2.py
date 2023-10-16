class Account:
    def __init__(self, acc_name, password, balance):
        self.acc_name = acc_name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance after depositing {amount} is Rs{self.balance}.")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"New balance after withdrawing {amount} is Rs{self.balance}.")
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        print(f"Balance is {self.balance}.")
    
class Manager:
    dict = {}
    def new_acc(self):
        username = input("enter the username...")
        password = input("enter the password...")
        deposit = float(input("enter the deposit..."))
        dict[username] = Account(username, password, deposit)

    def Login(self):
        username = input("enter the username...")
        for i in dict:
            
