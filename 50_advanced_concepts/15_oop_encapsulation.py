# Encapsulation is hiding the internal state of an object and only exposing what
# is necessary to the consumer.
# This helps maintain the integrity of the data contained in the object.

# In Java, you would do this by declaring a class attribute as private.
# In Python, you have to declare the attribute name with a dunder in front.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance  # Controlled access

# Usage
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Output: 1000
# print(account.__balance)    # This will throw an error