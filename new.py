class atm:       
    def __init__(self):
        pass

    def withdraw(self,name,balance):
        ab=int(input("enter the amount need to be withdrawn..."))
        if ab<balance:
            balance=balance-ab
            print(name,", Processing request for the withdrawl of ",ab," rupees.")
            print("Withdrawl success and cash after withdrawl is ",balance)
            print("_______________________")
        else:
            print(name,", Insufficient balance.")
            print("_______________________")

    def deposit(self,name,balance):
        aa=int(input(name,", enter the amount need to be deposited..."))
        balance+=aa
        print("New Balance is ",balance)
        print("_______________________")
        
    def check_balance(self,name,balance):
        print(name,", Balance is ",balance)
        print("_______________________")

class account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

k=int(input("enter the total number of atm's available..."))
lst=[]
for i in range(k):
    lst.append("obj_{}".format(i+1))

for i in range(k):
    lst[i]=atm()
lst_acc=[]
a=0
while(a!=2):
    print("1. Select atm and continue operation...\n2. Exit ATM")
    h=int(input("Enter operation..."))
    if h==1:
        s=int(input("enter the atm from which operation need to be performed..."))
        l=0
        while(l!=4):    
            
            print("__________ATM{}_______".format(s))
            print()
            print("0. New account\n1. Login\n2. Exit")  
            i=int(input("Enter the function required...."))
            if i==0:
                zz=input("enter the name of the user...")
                zx=input("enter the initial amount need to be deposited...")
                zc=input("enter the username...")
                k=len(lst_acc)
                lst_acc.append(zc)
                lst_acc[k]=account(zz,zx)
            elif i==1:
                zv=input("enter the username...")
                sss=0
                while sss!=2:
                    if zv in lst_acc:
                        print("1.Deposit\n2.Withdraw\n3.Balance\n4.Log out")
                        zb=int(input("enter the option..."))
                        zn=lst_acc.index(zv)
                        if zb==1:
                            lst[s-1].deposit(lst_acc[zn].name,lst_acc[zn].balance)
                        elif zb==2:
                            lst[s-1].withdraw(lst_acc[zn].name,lst_acc[zn].balance)
                        elif zb==3:
                            lst[s-1].balance(lst_acc[zn].name,lst_acc[zn].balance)
                        elif zb==4:
                            sss=2
                            print(zv," successfully logged out.")
                        else:
                            print("enter either 1,2or 3")
                    else:
                        sss=2
                        print("enter correct username.")
            elif i==2:
                l=4
                print("EXIT")
            else:
                print("enter either 1,2 or 3.")

    elif h==2:
        a=2
        print("________EXITING_ATM______")
    else:
        print("either enter 1 or 2.")

        
