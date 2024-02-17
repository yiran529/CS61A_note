class Account:
    interest=0.01
    def __init__(self,acount_holder):
        self.balance=0
        self.holder=acount_holder
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds!')
        else:
            self.balance-=amount
mike=Account('Mike')
mike.withdraw(10)
mike.deposit(100)
print(mike.balance)
john=Account('John')
Account.interest=1
print(john.interest)
class CheckingAccount(Account):
    withdraw_fee=1
    interest=0.04
    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_fee)
    def check(self):
        if self.balance>50:
            print('wii')
        else:
            print('naa')
j=CheckingAccount('John')
j.deposit(100)
j.withdraw(10)
print(j.balance)
j.balance=100
print(j.balance)
j.check()
j.withdraw(60)
j.check()