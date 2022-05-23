class Account:
    """Represent a bank account."""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        pass

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.balance):
            self.balance += -amount
        elif(amount > self.balance):
            self.balance = 0
        pass

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        pass

    def get_balance(self):
        return(self.balance)

    def get_name(self):
        return(str(self.name))