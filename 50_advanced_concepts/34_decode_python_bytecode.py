# Python code is compiled into bytecode, which is run on the Python virtual machine.
# This bytecode is machine agnostic, and can be run anywhere as long as the Python version is identical.
# The compiled bytecode is stored in the __pycache__ directory.

# The dis library allows you to disassemble the bytecode of your scripts.

import dis 

def count_to_ten():
    for i in range(10):
        print(i)

dis.dis(count_to_ten)