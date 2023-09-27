class atm:
    total=0
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


obj1=atm()
obj1.total=5000
obj2=atm()
obj2.total=200
l=0
x=int(input("Select the atm...1...or...2...->"))
while(l!=4):
    
    print("__________ATM{}_______".format(x))
    print()
    print("1. Withdrawl\n2. Deposit\n3. Check Balance\n4. Exit")  
    i=int(input("Enter the function required...."))
    if i==1:
        m=int(input("enter the amount need to be withdrawn...."))
        if x==1:
            obj1.total=obj1.withdraw(m,obj1.total) 
        elif x==2:
            obj2.total=obj2.withdraw(m,obj2.total) 
    elif i==2:
        m=int(input("enter the amount need to be deposited....")) 
        if x==1:
            obj1.total=obj1.deposit(m,obj1.total) 
        elif x==2:
             obj2.total=obj2.deposit(m,obj2.total)
    elif i==3:
        if x==1:
            obj1.check_balance(obj1.total)
        elif x==2:
            obj2.check_balance(obj2.total)
    elif i==4:
        l=4
        print("________EXIT___________")
    else:
        print("enter either 1,2,3 or 4.")    



