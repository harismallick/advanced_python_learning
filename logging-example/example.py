import logging
from employee import Employee

# There are 5 different levels of logging given the level of severity:
# DEBUG: Detailed information, relevant for diagnosing problems
# INFO: Confirmation that things are working as expected
# WARNING: An indication that something unexpected happened, or will happen but
#           the software is still working as expected
# ERROR: Due to a serious problem, the software has not been able to perform some function
# CRITICAL: A serious error, indicating that the program itself cannot continue to run.

# By default, the logging module will ONLY report levels warning, error and critical
# This behaviour can be changed by altering the logging config:

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='example.log',
#     format='%(asctime)s:%(levelname)s:%(message)s'
#     )
# Now everything from severity level debug and higher will be logged.
# By default, the log file is created in append mode.
# The format parameter allows you to set a template for each logging event.

# Custom logger for this module:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Format the string
logging_format = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# Provide filepath for logging
logging_file = logging.FileHandler("example.log")
# The logger and the file handler can be different log levels:
logging_file.setLevel(logging.ERROR)
logging_file.setFormatter(logging_format)

# If you also want log messages in the terminal, setup a stream handler:
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging_format)

# Configure logger
logger.addHandler(logging_file)
logger.addHandler(stream_handler)
# Now, debug and info logs will be shown in the terminal but not written to log file
# Levels Error and above will be shown in the terminal AND written to the log file.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")

def main() -> None:
    num1 = 10
    num2 = 5

    add_result = add(num1, num2)
    # print(f"{num1} + {num2} = {add_result}")
    logger.debug(f"{num1} + {num2} = {add_result}")

    sub_result = subtract(num1, num2)
    # print(f"{num1} - {num2} = {sub_result}")
    logger.debug(f"{num1} - {num2} = {sub_result}")

    mul_result = multiply(num1, num2)
    # print(f"{num1} * {num2} = {mul_result}")
    logger.debug(f"{num1} * {num2} = {mul_result}")

    div_result = divide(num1, num2)
    # print(f"{num1} / {num2} = {div_result}")
    logger.debug(f"{num1} / {num2} = {div_result}")

    emp1 = Employee("hakuna", 'matata')
    # Employee objects are logged in the logger for the employee module!
    # As the logger for this class exists in the employee namespace.
    # Thus logging isolation resulting in better troubleshooting.

    # force error to log:
    divide(5, 0)

if __name__ == "__main__":
    main()

# mCoding video on advanced logging techniques to checkout for complex usecases:
# https://www.youtube.com/watch?v=9L77QExPmI0
# It covers creating custom loggers using the dictConfig method of the logging library
# All 4 core components can be configured using dicts: filters, formatters, handlers and loggers