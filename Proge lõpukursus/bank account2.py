class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        elif amount < 0:
            return False
        else:
            self.balance -= amount
            return True

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

    def get_balance(self):
        return(self.balance)

    def get_name(self):
        return(self.name)

    def transfer(self, target, amount, fee=0.01):
        try:
            if self.name == target.name:
               fee = fee/2
        except:
            return False
        if self == target:
            fee = 0
        if(self.withdraw(amount + fee*amount) == True):
            target.deposit(amount)
            return True

kook1 = BankAccount("keek", 100)
kook2 = BankAccount("keeks", 100)
kook1.transfer(kook2, 10, 0.002)
print(kook2.balance,kook1.balance)