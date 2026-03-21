# Higher order functions take in other functions as arguments and execute them
# with other passed-in parameters.
# wrapper functions are also built in this way.

def validate(data, *validators):
    for validator in validators:
        if not validator(data):
            return False
    return True

# Validators
is_non_empty = lambda x: bool(x)
is_alpha = lambda x: x.isalpha()

# Validate input
input_data1 = "Python"
is_valid1 = validate(input_data1, is_non_empty, is_alpha)
print(is_valid1)  # Output: True

input_data2 = ""
is_valid2 = validate(input_data2, is_non_empty, is_alpha)
print(is_valid2)  # Output: False