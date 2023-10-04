
class Atm:       
    def __init__(self):
        pass

    def withdraw(self,acc,amount):
        #ab=int(input("enter the amount need to be withdrawn..."))
        if amount < acc.balance:
            acc.balance = acc.balance - amount
            print(f"Processing request for the withdrawl of {amount} rupees.")#
            print("Withdrawl success and cash after withdrawl is ",acc.balance)
            print("_______________________")
        else:
            print("Insufficient balance.")
            print("_______________________")

    def deposit(self,acc,amount):
        #aa=int(input(name,", enter the amount need to be deposited..."))
        acc.balance += amount
        print("New Balance is ",acc.balance)
        print("_______________________")
        
    def check_balance(self,acc):
        print("Balance is ", acc.balance)
        print("_______________________")

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

k=int(input("enter the total number of atm's available..."))
lst_acc=[Atm() for i in range(k)]

        
