class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def checkBal(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from deposit")
name=input()
dep=int(input())
wth=int(input())
acc = Account(name)
acc.checkBal()
acc.deposit(dep)
acc.checkBal()
acc.withdraw(wth)
acc.checkBal()