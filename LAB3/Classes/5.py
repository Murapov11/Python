class Account:
    def __init__(self,_owner,_balance):
        self.owner = _owner
        self.balance = _balance
    def withdrawal(self):
        x = int(input())
        if (self.balance - x < 0):
            print('withdrawal cannot happen!')
        else:
            self.balance -= x
            print(f'{self.owner} ! Your balance after withdrawal {self.balance}')
    def deposit(self):
        x = input()
        self.balance += x
        print (f'{self.owner} ! Your balance after deposit {self.balance}')
p1 = Account('Yerkhan', 500)
p1.withdrawal()