# Bank AC class with 2 attributes

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        return ('Updated Balance after deposit: ',self.balance)

    def withdrawal(self,amount):
        self.balance = self.balance - amount
        return self.balance

# Instantiate class
acct1 = Account('Jose','100')
print(acct1)
