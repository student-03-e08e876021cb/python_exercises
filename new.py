class Atm:       
    def __init__(self):
        pass

    def withdraw(self,acc,amount):
        if amount < acc.balance:
            acc.balance = acc.balance - amount
            print(f"Processing request for the withdrawl of {amount} rupees.")#
            print(f"Withdrawl success and cash after withdrawl is {acc.balance}")
            print("_______________________")
        else:
            print("Insufficient balance.")
            print("_______________________")

    def deposit(self,acc,amount):
        #aa=int(input(name,", enter the amount need to be deposited..."))
        acc.balance += amount
        print(f"New Balance is {acc.balance}")
        print("_______________________")
        
    def check_balance(self,acc):
        print(f"Balance is {acc.balance}")
        print("_______________________")

class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

no_atm = int(input("enter the total number of atm's available..."))
lst_atm = [Atm() for i in range(no_atm)]
a = 0
while(a!=5):
    print("1. Select Atm\n2. Exit")
    option = int(input("enter the option selected"))
    
    if option == 1:
        choose_atm = int(input("enter the atm..."))
        lst_atm[choose_atm-1] == Atm()
        print("1.New Account\n2.Deposit\n3.Withdraw\n4.Change ATM")
        operation_selected = int(input("Enter the operation selected."))
        b=0
        if operation_selected == 1:
            name = input("Enter the name of the user...")
            balance = int(input("enter the initial deposit..."))
            username = input("enter the username prefered...")
            username = Account(name,balance)
        elif operation_selected == 2:
            user = input("enter the username...")
            deposit = int(input("Enter the money need to be deposited"))
            lst_atm


    elif option == 2:
        a = 5
        print("EXIT")    
    else:
        print("enter either 1 or 2")

        
