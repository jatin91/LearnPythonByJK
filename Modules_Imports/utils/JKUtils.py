#Modules and Imports
#As your code grows you cannot keep everything in one file. Modules are how Python lets you split code across files and reuse it.

#Creating a module is as simple as creating a .py file with some code in it. For example, lets create a file called math_utils.py with the following content:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b        
#Now we can import this module in another file and use its functions:
def greet(name):
    return f"Hello {name}"

def add(a, b):
    return a + b

def is_adult(age):
    return age >= 18

PI = 3.14159

import JKUtils as helpers

#print(helpers.greet("Jatin"))
#print(helpers.add(10, 20))
#print(helpers.is_adult(35))
#print(helpers.PI)

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b