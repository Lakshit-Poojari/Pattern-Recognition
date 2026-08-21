class Account:

    @staticmethod
    def welcome():
        print("Welcome to bank")

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount", amount, "Debited from your account")
            print("Balance is", self.balance)
        else:
            print("Insufficient Amount")

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Amount", amount, "Credited to your account")
        print("Balance is", self.balance)

    def bal(self):
        return self.balance

Account.welcome()

a1 = Account("Lakshit", 5000)

a1.credit(500)
a1.debit(6000)

print(a1.bal())