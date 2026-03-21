# In the case of inheritance and multiple interlinked parent and child classes,
# what is the method resolution order?

# Starts from the child class where the method is being invoked.
# Moves up the inheritance heirarchy until Python finds the method to invoke.
# If a class inherits from multiple other classes, then the search priority will be 
# from left to right, the order in which the inheritance declaration was written.

# Uses the C3 linearisation algorithm to do this.
# Use the __mro__ builtin method to get the method resolution order for a particular class

# class A:
#     def greet(self):
#         print("Hello from A")

# class B:
#     def greet(self):
#         print("Hello from B")

# class C(A, B):
#     pass

# c = C()
# c.greet()  # Output: Hello from A
# print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# The diamond problem

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Output: Hello from C
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)