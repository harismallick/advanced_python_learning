from operator import attrgetter

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}({self.age})"

users = [User("Alice", 30), User("Bob", 25), User("Charlie", 35)]

# Sort by age
sorted_users = sorted(users, key=attrgetter("age"))
print(sorted_users)
# Output: [Bob(25), Alice(30), Charlie(35)]

# As the name suggests, use attrgetter to retrive particular attributes from a class

# attrgetter also works for nested attributes, when you need to get an attribute of a class inside a class:

# Define nested classes
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
class Company:
    def __init__(self, city, name):
        self.city = city
        self.name = name

class Person:
    def __init__(self, name, age, address, company):
        self.name = name
        self.age = age
        self.address = address
        self.company = company

# Sample data
people = [
    Person("Alice", 30, Address("New York", "NY"), Company("Company ABC", "Philadelphia")),
    Person("Bob", 25, Address("Chicago", "IL"), Company("Company 2", "Nashville")),
    Person("Charlie", 35, Address("Los Angeles", "CA"), Company("Company 3", "Miami"))
]

# Get sort_key from frontend
# sort_key = "address.city"
# sort_key = "company.name"
sort_key = "address.city"

# Sort based on the dynamic key
sorted_people = sorted(people, key=attrgetter(sort_key))

print([person.name for person in sorted_people])  # Example Output: ['Bob', 'Charlie', 'Alice']