# Class methods require cls or self as the first argument, ie, these methods are coupled to the class.
# Static methods can be invoked without cls or self.

class Employee:
    retirement_age = 65  # Class-level attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Accesses 'cls' to create a new instance
        return cls(name, 2026 - birth_year)
    
    @staticmethod
    def is_work_day(day):
        # No 'self' or 'cls' needed; just a logic check
        return day.weekday() < 5
    



