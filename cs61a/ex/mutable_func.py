def make_withdraw(balance):
    def withdraw(amount):
        #nonlocal balance
        balance.extend([amount])
        return balance
    return withdraw
withdraw=make_withdraw([100])
print(withdraw(25))