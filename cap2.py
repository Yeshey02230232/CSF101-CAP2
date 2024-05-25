import random
class Bank_acc:
    def __init__(self,account_num,password,account_type,balance=0):
        self.account_num =account_num
        self.password = password
        self.account_type= account_type
        self.balance= balance
#This is the basic category for bank accounts.
#It creates an account with a number, password, type, and balance.
    def withdraw(self,amount):
        if amount > self.balance:
            print("INSUFFICIENT FUND!!! PLEASE CHECK YOUR AMOUNT!!")
        else:
            self.balance-= amount
            print(f"Withdraw Nu.{amount}. New balance is NU.{self.balance}")
#If there are enough funds in the account, you can withdraw them using this technique.
    def deposit(self,amount):
        self.balance += amount 
        print(f"Ngultrum deposited= NU.{amount} New balance =NU.{self.balance}")
#This approach allows you to deposit money into your account.
class Business (Bank_acc):
    def __init__ (self,account_num,password,balance=0):
        super(). __init__(account_num,password,"Business Account",balance)
#This is a subclass of Bank_acc that represents business accounts.
#It creates a business account by invoking the superclass initializer and specifying "Business Account" as the account type.
class Saving(Bank_acc):
    def __init__ (self,account_num,password,balance=0):
        super().__init__(account_num,password,"SavingAccount",balance)
#This is a subclass of Bank_acc that represents savings accounts.
#It creates a savings account by invoking the superclass initializer and specifying "Saving Account" as the account type.
def save_acc(Bank_acc):
    with open('Account.txt','a')as f:
        f.write(f"{Bank_acc.account_num},{Bank_acc.password},{Bank_acc.account_type},{Bank_acc.balance}\n")
#This function writes account information to a file called 'Account.txt'.
def load_account():
    Bank_acc={}
    try:
        with open("account.txt","r")as f:
            for line in f:
                account_num,password,account_type,balance=line.strip().split(',')
                balance=float(balance)
                if account_type=='BusinessAccount':
                    Bank_acc[account_num]=Business(account_num,password,balance)
                else:
                    Bank_acc[account_num]=Saving(account_num,password,balance)
    except FileNotFoundError:
        pass
    return Bank_acc
#This function converts the account details from 'account.txt' into a dictionary of account objects.
def creating_acc():
    account_num=str(random.randint(100000000,999999999))
    password =str(random.randint(1000,9999))
    account_type = input("WHICH ACCOUNT DO YOU WANT TO CREATE:\n1.Saving\n2.Business\n---->").capitalize()
    if account_type=='Business':
        Bank_acc=Business(account_num,password)
    else :
        Bank_acc=Saving(account_num,password)
    save_acc(Bank_acc)
    print(f"ACCOUNT CREATED SUCCESFULLY!!! \nACCOUNT NUMBER--->{account_num}\nPASSWORD-->{password}")
    return Bank_acc
#This function converts the account information from 'account.txt' to a dictionary of account objects
def login(Bank_acc):
    account_num= input("PLEASE ENTER YOUR ACCOUNT NUMBER!!!---->")
    password=input("PLEASE ENTER YOUR PASSWORD!!!--->")
    if account_num in Bank_acc and Bank_acc[account_num].password==password:
       print("KUZU ZANGPOLA!! YOUR MONEY UNDER ONE APPLICATION TRUSTED!!\n Succesfully loged in!!")
       return Bank_acc[account_num] 
    else:
        print("PLEASE CHECK YOUR ACCOUNTNUMBER\PASSWORD!!!")
        return None
#This method allows a user to log in by comparing their account number and password to the loaded accounts.
def send_teru(Bank_acc,sender):
    recipient_number = input("Enter recipient account number: ")
    if recipient_number not in Bank_acc:
        print("PLEASE CHECK THE Recipient account!!!")
        return

    amount = float(input("Enter amount to send: "))
    if sender.balance < amount:
        print("PLEASE CHECK YOUR FUND!!")
        return
    
    sender.withdraw(amount)
    Bank_acc[recipient_number].deposit(amount)
    print(f"Sent Nu.{amount} to account {recipient_number}.")
#This function enables a user to transfer money to another account if the recipient exists and the sender has enough funds.
def delete_account(Bank_acc,account):
    account_num = account.account_num
    del Bank_acc[account_num]
    
    with open('accounts.txt', 'w') as f:
        for acc in Bank_acc.values():
            f.write(f"{acc.account_num},{acc.password},{acc.account_type},{acc.balance}\n")
    
    print(f"Account {account_num} deleted successfully.")
#This function deletes an account and modifies its associated file.
def main():
    Bank_acc = load_account()
    while True:
        print("\n---------------WELCOME TO CST STUDENT BANK----------------------------")
        print("\n----------------------------------\n1. Create Account\n2. Login\n3. Exit\n----------------------------------")
        choice = input("Enter choice: ")
        
        if choice == '1':
            creating_acc()
        elif choice == '2':
            account = login(Bank_acc)
            if account:
                while True:
                    print("\n------------------------------------------------------------------\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Send Money\n5. Delete Account\n6. Logout\n-------------------------------------------------------------------")
                    choice = input("Enter choice: ")
                    
                    if choice == '1':
                        print(f"Your balance is Nu.{account.balance}.")
                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif choice == '4':
                        send_teru(Bank_acc,account)
                    elif choice == '5':
                        delete_account(Bank_acc,account)
                        break
                    elif choice == '6':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
#The main function loads current accounts and displays a menu for creating, logging in, and departing.
#Once logged in, users can view their balance, deposit money, withdraw money, send money, delete their account, or log out.
