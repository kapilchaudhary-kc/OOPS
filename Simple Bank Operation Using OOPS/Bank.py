#Bank Operation Using OOP

class Bank():
    bankname="Bank"
    branch="B1"

    #create Bank Account
    def __init__(self, username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0

    #Deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        #confirmation message
        print(f'{amount} deposited successfully')
    
    #Withdraw
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            print(f'{amount} withdrawal done.')
        else:
            #Rejection message
            print('insufficient balance')
    
    #Ministatement
    def ministatement(self):
        print(f'Balance in your account is:{self.balance}')

print(f'Welcome to {Bank.bankname},{Bank.branch}')