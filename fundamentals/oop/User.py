class User():

    def __init__(self, name, amount):
        self.name = name
        self.account_balance = amount
        
    # def display_user_balance(self, amount):

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def transfer_money(self, amount, User):
        self.account_balance = self.account_balance - amount
        name.account_balance = name.account_balance + amount
        return name.account_balance()

kyle = User('kyle', 100)
kyle.name = "kyle"
print(kyle.name)

kyle.make_deposit(100)
kyle.make_deposit(100)
kyle.make_deposit(100)
kyle.make_withdrawl(100)
print(kyle.account_balance)

dan = User("Dan", 100)
print(dan.name)
dan.make_deposit(50)
dan.make_deposit(50)
dan.make_withdrawl(50)
dan.make_withdrawl(20)
print(dan.account_balance)

mike = User('Mike', 100)
print(mike.name)
mike.make_deposit(500)
mike.make_withdrawl(100)
mike.make_withdrawl(100)
mike.make_withdrawl(100)
print(mike.account_balance)