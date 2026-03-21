# Encapsulation within methods example:

from collections import namedtuple

OrderItem = namedtuple("OrderItem", ['name', 'value', 'qty'])

def get_order_total(basket: list[OrderItem], region: str) -> float:

    total: float = 0

    for item in basket:
        total += item.value * item.qty

    total += total * get_tax_rate(region)

    return total

def get_tax_rate(region: str) -> float:
    if region.upper() == "US":
        return 0.07
    
    if region.upper() == "EU":
        return 0.2
    
    else:
        return 0.1
    
basket = [
    OrderItem("item1", 20, 1),
    OrderItem("item2", 30, 1),
    OrderItem("item3", 50, 1)
]

basket_total: float = get_order_total(basket, "EU")
print(basket_total)

# All the logic for tax calculation is contained in a separate function.

# Program to an interface, not an implementation example:

from abc import ABC, abstractmethod

# The Interface (The "Contract")
class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass

# The classes implementing the interface
class EmailSender(MessageSender):
    def send(self, recipient: str, message: str):
        print(f"Sending Email to {recipient}: {message}")

class SMSSender(MessageSender):
    def send(self, recipient: str, message: str):
        print(f"Sending SMS to {recipient}: {message}")

class AlertSystem:
    def __init__(self, sender: MessageSender):
        # We program to the 'MessageSender' interface
        # ie, dependent on the interface not the implementation!
        self.sender = sender

    def notify_user(self, user_contact: str, text: str):
        # We don't care HOW it sends, just that it HAS a .send() method
        self.sender.send(user_contact, text)

# --- Execution ---
# We can swap the implementation easily without changing AlertSystem code
email_alert = AlertSystem(EmailSender())
email_alert.notify_user("dev@example.com", "Server is down!")

sms_alert = AlertSystem(SMSSender())
sms_alert.notify_user("555-0199", "Server is back up!")

# AlertSystem doesn't care about what messaging system is being used
# as long as the system has a send() method.