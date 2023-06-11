#banking app
#class based 
#withdrawal and deposit
#write a transaction on a python file

#hints;
#in while True, need input(), classes, open()

import os


class mybank:

    

    def accountLog(self, accName):
        filename = f"account{accName}.txt"
        mode = 'w' if not os.path.exists(filename) else 'a'

        with open(filename, mode) as file:
            if mode == 'w':
                file.write(f"Account: {accName}\n")


    def __init__(self, balance = 0):
        
        self.balance = balance   
        self.last_balance = balance 


    def transactionLog(self, logs, accName):
        self.logs = logs
        self.accountLog(accName)
        with open(f"account{accName}.txt", 'a') as file2:
                file2.write(f"{logs}\n")

    def withdraw(self, amount, accName):
        try:
            amount = float(amount)    
        except Exception:
            print("Please enter NUMBER value")
            amount = 0
        
        if amount > self.last_balance:
            print("Insufficient balance.")    
        else:
            self.balance = self.last_balance - amount
            self.transactionLog(f"Withdrew: {amount}\t\tNew Balance: {self.balance}", accName)
            self.last_balance = self.balance

    def deposit(self, amount, accName):
        try:
            amount = float(amount)
            
        except Exception:
            print("Please enter NUMBER value")
            amount = 0
        
        if amount:
            self.balance = self.last_balance + amount
            self.transactionLog(f"Deposited: {amount}\t\tNew Balance: {self.balance}", accName)
            self.last_balance = self.balance

    def readLastBalance(self, accName):
        filename = f"account{accName}.txt"
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1].strip() if lines else None
                if last_line:
                    balance_index = last_line.rfind("New Balance: ")
                    if balance_index != -1:
                        balance =last_line[balance_index + len('New Balance: '):]
                        return float(balance)
        except FileNotFoundError:
            return None

    def change_transaction(self):
        resume = ''
        while True:
            resume = input("\nChange transaction? [Y, N]: ")

            if resume.lower() not in ['y', 'n']:
                print("Please type Y for yes, N for no")
                continue
            elif resume.lower() == 'y':
                return True
            else:
                print('\nThank you for banking with us')
                return False

        
        

bank = mybank()

print("Welcome to Yourbank")

accName = input("Please Enter your ACCOUNT NAME: ").capitalize()
bank.accountLog(accName)



last_balance = bank.readLastBalance(accName)

if last_balance is not None:
    print(f"Last Balance: {last_balance}")
else:
    last_balance = 0

    print("No transaction history found.")

print(f"What do you want to do today {accName}?")

while True:
    
    transactions = input("\n[D] to Deposit , [W] to Withdraw:  ")

    if transactions.lower() not in ['d','w']:
        print("Please Enter Correct Command") 
        continue

    elif transactions.lower() == 'd':
        amount = input("How much you want to deposit?  ")
        bank.deposit(amount, accName)
        print(f"\nYou deposited ${amount}")
        print(f"Your New Balance is {bank.balance}")
        
        if not bank.change_transaction():
          
            break

    elif transactions.lower() == 'w':
        amount = input("How much you want to withdraw?  ")
        bank.withdraw(amount, accName)
        
        amount = float(amount)
        last_balance = float(last_balance)

        print(f"\nYou withdrew ${amount}")
        print(f"Your New Balance is {bank.balance}")

        if not bank.change_transaction():
               
            break

        if amount > last_balance:
            if not bank.change_transaction():
                break   

        