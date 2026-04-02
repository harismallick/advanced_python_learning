from main import add, divide, UserManager, is_prime, get_weather
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.fixture # fixture is some initialisation code that is run before every test using the fixture function
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@test.com") == True
    assert user_manager.get_user("john_doe") == "john@test.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@test.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "john@test.com")


# Running parameterised tests to automatically tests an array of inputs

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False)
])
def test_is_prime(num: int, expected: bool):
    assert is_prime(num) == expected

# Mocking example:

def test_get_weather(mocker):
    # Mock the request.get() function:
    mock_get = mocker.patch("main.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "temperature": 25,
        "condition": "sunny"
    }

    # Call function:
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")