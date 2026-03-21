# Tutorial source: https://www.youtube.com/watch?v=RwH2UzC2rIo

from typing import Any, NewType, TypedDict
name: str = "John"
age: int = 38

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# type User = dict[str, str | int | RGB | None]   # Not specific enough for individual key-value pairs

# Use TypedDict to ensure individual k-v pairs are of the desired type
# However, this method of type hinting does not support default values and runtime validation
class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int | None
    fav_color: RGB | None

def create_user(
        first_name: str, 
        last_name: str, 
        age: int | None = None,
        fav_color: RGB | None = None    
    # ) -> dict[str, Any]: # simplified typing
    ) -> User:             # More complex types can be defined elsewhere, similar to TypeScript
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    person: User = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "fav_color": fav_color
    }

    return person

person1: User = create_user("John", "Doe", 35, RGB((50,50,50)))

print(person1)

# A typing solution that supports default values, dataclasses:

from dataclasses import dataclass

@dataclass
class User2:
    first_name: str
    last_name: str
    email: str
    age: int | None = 35
    fav_color: RGB | None = None

def create_user2(
        first_name: str, 
        last_name: str, 
        age: int | None = None,
        fav_color: RGB | None = None    
    # ) -> dict[str, Any]: # simplified typing
    ) -> User2:             # More complex types can be defined elsewhere, similar to TypeScript
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    # Instantiate an instance of the dataclass:
    person: User2 = User2(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color
    )

    return person

person2: User2 = create_user2("John", "Doe", 37, RGB((50,50,50)))
person3: User2 = create_user2("Jane", "Goody", 33, RGB((150,50,70)))

print(person2)
# Can use dot notation with dataclass objects:
print(person2.first_name)
print(person2.email)

# Generic typing in Python

import random

people: list[User2] = [person2, person3]

def random_choice[T](items: list[T]) -> T:  # Very similar syntax to Typescript
    return random.choice(items)

random_selected: User2 = random_choice(people)
print("Randomly selected person:")
print(random_selected)

# Third party libraries like requests, pandas, etc use their own types
# Mypy will not check types correctly for 3rd party libraries by default
# Need to install that library's types into your venv for Mypy to work correctly
# For example: pip3 install types-requests for the requests library
# The pip install command generally follows the above syntax for a library

# Dataclasses cannot do validation checks in real time on the data
# use Pydantic for this.