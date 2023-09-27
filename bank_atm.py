class atm:
    def withdraw(self,cash,total):
        if cash<total:
            total=total-cash
            print("Processing request for the withdrawl of ",cash," rupees.")
            print("Withdrawl success and cash after withdrawl is ",total)
            print("_______________________")
            return total
        else:
            print("Insufficient balance.")
            print("_______________________")
    def deposit(self,cash,total):
        total+=cash
        print("New Balance is ",total)
        print("_______________________")
        return total
    def check_balance(self,total):
        print("Balance is ",total)
        print("_______________________")

total=5000
obj=atm()
l=int(input("Enter 0 to enter into the atm...."))
while(l!=4):
    print("__________ATM__________")
    print()
    print("1. Withdrawl\n2. Deposit\n3. Check Balance\n4. Exit")  
    i=int(input("Enter the function required...."))
    if i==1:
        m=int(input("enter the amount need to be withdrawn...."))
        total=obj.withdraw(m,total)   
    elif i==2:
        m=int(input("enter the amount need to be deposited....")) 
        total=obj.deposit(m,total)  
    elif i==3:
        obj.check_balance(total)
    elif i==4:
        l=4
        print("________EXIT___________")
    else:
        print("enter either 1,2,3 or 4.")    
