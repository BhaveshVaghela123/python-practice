
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money Deposited:", amount)
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Money Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


b1 = BankAccount("Bhavesh", 10000)

b1.deposit(2000)
b1.withdraw(3000)

print("Final Balance:", b1.get_balance())
