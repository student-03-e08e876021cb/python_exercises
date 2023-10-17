class Account:
    def __init__(self, username, password, balance):
        self.username = username
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
    acc_list = []
    
    def new_acc(self):
        username = input("enter the username...")
        password = input("enter the password...")
        deposit = int(input("enter the initial money need to be initiated..."))
        Manager.acc_list.append(Account(username, password,deposit))

    def login(self):    
        flag = 0
        while flag == 0:
            username = input("enter the username...")
            for i,acc in enumerate(Manager.acc_list):
                if username == acc.username:
                    acc_no = i
                    flag =1 
                    break
        password = input("enter the password...")
        while password != Manager.acc_list[acc_no].password:
            password = input("enter the password...")
            
        while True:
            selection = int(input("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Logout\nselection is..."))
            if selection == 1:
                amount = int(input("enter the money need to be deposited..."))
                Manager.acc_list[acc_no].deposit(amount)
            elif selection == 2:
                amount = int(input("enter the money need to be withdrawn..."))
                Manager.acc_list[acc_no].withdraw(amount)
            elif selection == 3:
                Manager.acc_list[acc_no].check_balance()
            elif selection == 4:
                print("Logged Out")
                break
            else:
                print("Invalid selection")


print("Welcome to the ATM")
while True:
    selection = int(input("1.New User\n2.Login\n3.Exit\nEnter the option..."))
    manage = Manager()
    if selection == 1:
        manage.new_acc()
    elif selection == 2:
        manage.login()
    elif selection == 3:
        break
    else:
        print("enter a valid option.")
