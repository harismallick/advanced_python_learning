import logging

# Its good practice to create different loggers for different modules.
# Otherwise, multiple modules will end up sharing the same root logger
# This can create unexpected behaviour with logging event not being written to file

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Format the string
logging_format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# Provide filepath for logging
logging_file = logging.FileHandler("employee.log")
logging_file.setFormatter(logging_format)

# Configure logger
logger.addHandler(logging_file)

class Employee:
    def __init__(self, firstname: str, lastname: str):
        self.first = firstname
        self.last = lastname

        logger.info(f"Created employee: {self.fullname} - {self.email}")

    @property
    def email(self) -> str:
        return f"{self.first.lower()}_{self.last.lower()}@email.com"
    
    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
def main() -> None:

    emp1 = Employee('John', 'Doe')
    emp2 = Employee('Jane', 'Doe')

if __name__ == "__main__":
    main()