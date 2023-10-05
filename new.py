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
        return acc

    def deposit(self,acc,amount):
        acc.balance += amount
        print(f"New Balance is {acc.balance}")
        print("_______________________")
        return acc
        
    def check_balance(self,acc):
        print(f"Balance is {acc.balance}")
        print("_______________________")

class Account:
    def __init__(self,name,balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        
usernames = ['Raju', 'Jacob', 'Kate']
balances = [10000, 34000, 12500]
passwords = ["raju1567", "jac007", "kate111"]

## Creating accounts
accountList = [Account(usernames[i], balances[i], passwords[i]) for i in range(len(usernames))]

## Creating an Atm object
atm = Atm()

print("******* Welcome to ATM ********")
print("_______________________________")
print()

while True:
    selection = int(input("Enter your selection: \n\n1. Login to your account\n2. Exit\n"))
    if selection == 1:
        uname = input("Enter your username : ")
        while uname not in usernames:
            uname = input("Enter a correct username : ")

        ## Acquiring the required account fron accountList
        for idx, acc in enumerate(accountList):
            if acc.name == uname:
                userAcc = acc
                userAccIdx = idx

        passw = input("Enter your password : ")
        while userAcc.password != passw:
            passw = input("Enter the correct password : ")

        while True:
            option = int(input("Enter your selection : \n\n1. Withdraw\n2. Deposit\n3. Check balance\n4. Logout\n"))
            if option == 1:
                amount = float(input("Enter the amout to withdraw : "))
                accountList[userAccIdx] = atm.withdraw(userAcc, amount)

            elif option == 2:
                amount = float(input("Enter the amount to deposit: "))
                accountList[userAccIdx] = atm.deposit(userAcc, amount)
            elif option == 3:
                atm.check_balance(userAcc)
            elif option == 4:
                print("\nLogging out of the account!\n")
                break
            else:
                print("Enter a valid option!")
                continue

    elif selection == 2:
        print("Exiting ATM application!")
        break
    else:
        print("Enter a valid option!")
        continue

	

        
