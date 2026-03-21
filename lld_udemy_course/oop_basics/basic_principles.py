# Implement a class that inherits from two interfaces in Python

from abc import ABC, abstractmethod

class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

# Define class that inherits from two interfaces:

class Duck(Swimmer, Flyer):

    def swim(self):
        print("Ducks can swim.")

    def fly(self):
        print("Ducks can fly.")


test = Duck()
test.swim()
test.fly()


# Inheritance + polymorphism example:

class Animal:
    def breathe(self):
        print("This animal breathes oxygen.")

    def sound(self):
        print("This animal makes sound.")

class Cat(Animal):
    def sound(self):
        print("Cat says meow.")

cat = Cat()
cat.sound() # The behaviour of this method is modified
cat.breathe() # This method is inherited from the parent


# Example of composition relationship between classes:
import random

class Account:
    def __init__(self, account_num: int, account_name: str):
        self.account_num = account_num
        self.account_name = account_name

    def __str__(self):
        return f"{self.account_name} {self.account_num}"

class Bank:
    __accounts: list[Account] = []

    def create_account(self, holder_name: str):
        acc_number = random.randint(100, 999)
        account = Account(acc_number, holder_name)
        self.__accounts.append(account)

    @property
    def get_accounts(self) -> list[Account]:
        return self.__accounts
    

bank = Bank()
bank.create_account("John Doe")
bank.create_account("Jane Goody")

accounts = bank.get_accounts
for account in accounts:
    print(account)

# In this example, if we delete the bank object, then all accounts get deleted too.