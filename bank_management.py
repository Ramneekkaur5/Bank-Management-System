import pandas as pd
import matplotlib.pyplot as plt
import sys


def menu():
    password=input("Enter password:")

    if password=='hr123':
        print("Login successful!")
        print() 
        print("***********************************************************")
        print("              BANK MANAGEMENT SYSTEM")
        print("***********************************************************")
        print()
        print("      1.Details of existing Account")
        print("      2.Deposit Money")
        print("      3.Withdraw Money")
        print("      4.Check Balance")
        print("      5.Add a New Account")
        print("      6.Delete Account")
        print("      7.Exit")
        print("**********************************************************")
    else:
        print("Invalid Password")
        sys.exit()
  


menu()

def bankcsv():
    print('Details Of Existing Accounts')
    print()
    print()
    df=pd.read_csv("C:\\Users\\RANVIR\\Ramneek.csv",index_col=0)
    print(df)

    print("**************THANK YOU*************")

def dm():
    df=pd.read_csv("C:\\Users\\RANVIR\\Ramneek.csv",index_col="Account no")
    accno=int(input(" Enter your account no:"))
    detail=df.loc[accno,:]
    print(detail)
    m=int(input("ENTER AMOUNT TO DEPOSIT:"))
    balance=int(input("ENTER YOUR CURRENT BALANCE:"))
    rows_to_update=[accno]
    cols_to_update=['updated balance']
    values=[balance+m]
    print()
    print("AMOUNT SUBMITTED")
    print()
    print()
    print("YOUR BALANCE IS UPDATED:")
    L=input("PRESS ENTER TO SHOW YOUR BALANCE")
    g=df.loc[rows_to_update, cols_to_update]=values
    details=df.loc[accno,:]
    print(details)

    print("**************THANK YOU*************")



def wm():
    df=pd.read_csv("C:\\Users\\RANVIR\\Ramneek.csv",index_col="Account no")
    accno=int(input(" Enter your account no:"))
    detail=df.loc[accno,:]
    print(detail)
    m=int(input("ENTER AMOUNT TO WITHDREW:"))
    balance=int(input("ENTER YOUR CURRENT BALANCE:"))
    rows_to_update=[accno]
    cols_to_update=['updated balance']
    values=[balance-m]
    print()
    print("AMOUNT SUCESSFULLY WITHDRAWN")
    print()
    print()
    print("YOUR BALANCE IS UPDATED:")
    L=input("PRESS ENTER TO SHOW YOUR BALANCE")
    g=df.loc[rows_to_update, cols_to_update]=values
    details=df.loc[accno,:]
    print(details)
    print("**************THANK YOU*************")
    

def cb():
   
    accno=int(input("Enter your account no:"))
    print()
    print()
    print("Your Account Details are:")
    print()
    print()
    df=pd.read_csv("C:\\Users\\RANVIR\\Ramneek.csv",index_col="Account no")
    detail=df.loc[accno,:]
    print(detail)
    print("**************THANK YOU*************")
   

def add_acc():
        
        name=input("ENTER YOUR NAME:")
        age=int(input("ENTER YOUR AGE:"))
        gender=input("ENTER YOUR GENDER:")
        city=input("ENTER YOUR CITY:")
        balance=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:"))
        df=pd.read_csv(("C:\\Users\\RANVIR\\Ramneek.csv"),index_col="Account no")
        new_index=df.index.max()+1
        df.loc[new_index] = [name,age,gender,city,balance,]
        print(df)
        print("**************THANK YOU*************")
        
        
        


def da():
    print("For Deleting Account")
    df=pd.read_csv(("C:\\Users\\RANVIR\\Ramneek.csv"),index_col="Account no")
    acc=int(input("ENTER YOUR ACCOUNT NUMBER:"))
    df.drop(acc,axis=0,inplace=True)
    print("DELETING ACCOUNT PLEASE WAIT...")
    print()
    print("ACCOUNT DELETED")
    print()
    VV=input("PRESS ENTER TO SHOW NEW TABLE")
    print()
    print(df)
    print("**************THANK YOU*************")



                
inp=int(input("ENTER YOUR CHOICE:"))
if inp==1:
    print("EXISTING ACCOUNTS DETAILS ARE:")
    print()
    bankcsv()
    print()
elif inp==2:
    dm()
elif inp==3:
    wm()
elif inp==4:
    cb()
elif inp==5:
    add_acc()
elif inp==6:
    da()
elif inp==7:
    print("Successfully logged out..")
    sys.exit
    
else:
    print('invalid option')
            

