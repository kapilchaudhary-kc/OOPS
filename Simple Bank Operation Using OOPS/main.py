#Bank Operation Using OOP

from Bank import Bank

username=input("Enter Your Name:")
pan=input("Enter Your pan:")
address=input("Enter Your address")

b=Bank(username,pan,address)

while True:
    print('Select An Option: ')
    print('1. Deposit\n2. Withdraw\n3. Ministatement\n4. Stop')
    option=int(input(''))
    print('_'*40)

    if option==1:
        amount=float(input('Enter Deposited Amount:'))
        b.deposit(amount)
        print('_'*40)
    elif option==2:
        amount=float(input('Enter Withdrawl Amount:'))
        b.withdraw(amount)
        print('_'*40)
    elif option==3:
        b.ministatement()
        print('_'*40)

    elif option==4:
        print(f'Thanks for using {Bank.bankname}')
        print('_'*40)
        break
    else:
        print('Invalid Option')
        print('_'*40)