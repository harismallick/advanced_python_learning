import requests

type Number = int | float

def add(a: Number, b: Number) -> Number:
    return a + b

def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError
    return a / b


class UserManager:
    def __init__(self) -> None:
        self.users: dict[str, str] = {}

    def add_user(self, username: str, email: str) -> bool:
        if username.lower() in self.users:
            raise ValueError("User already exists")
        
        self.users[username.lower()] = email
        return True
    
    def get_user(self, username: str) -> str:
        return self.users.get(username.lower(), "")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Example function to test mocking in pytest:

def get_weather(city: str):
    response = requests.get(f"https://api.weather.com/v1/{city}")

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")