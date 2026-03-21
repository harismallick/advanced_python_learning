'''
Dependency Injection (DI) is a fancy name for a simple concept: instead of a piece 
of code creating the objects it needs (its dependencies), those objects are 
"injected" or passed in from the outside.

It moves the responsibility of creating an object away from the object that uses it.

The user object being decoupled can now use different consumer objects based on the requirement
'''

class EmailService:
    def send(self, message):
        print(f"Sending Email: {message}")

class SmsService:
    def send(self, message):
        print(f"Sending SMS: {message}")

class UserService:
    def __init__(self, message_service):
        # The dependency is "injected" here
        self.message_service = message_service

    def welcome(self):
        self.message_service.send("Welcome aboard!")

# Now we decide what to use at runtime:

email_tool = EmailService()

user_svc = UserService(email_tool)
user_svc.welcome()

sms_tool = SmsService()
user_svc2 = UserService(sms_tool)
user_svc2.welcome()

# The UserService instance can be instantiated with the email tool or the sms tool
# Without having to hard code these messaging systems into the UserService.
# Both EmailService and SmsService must implement an interface contract for such 
# decoupling and dependency injection to work.