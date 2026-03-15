# Here we are creating a function 
def greet():
# Indentation is important in Python. The code inside the function must be indented. ideally 4 spaces should be used for indentation inside the function.    
    print("Hello")
    print("Welcome")
# The code inside the function will only execute when we call the function. Until then it will not execute. So we can have multiple functions in our code and we can call them whenever we want to execute the code inside them. 
print("I am outside the function")

# Now we are calling the function to execute the code inside it.
#greet()


# this is the method with parameters. We can pass parameters to the function and use them inside the function. Parameters are like variables that we can use inside the function. 
# We can pass any number of parameters to the function and use them as needed.
def greet(name):
    print(f"Hello {name}")

#greet("Jatin")
#greet('100%')


def greet(name, city):
    print(f"Hello {name}, you are from {city}")

#greet("Jatin", "Mohali")
#greet("Arjun", "Delhi")

# this will give error because we are not passing the required parameters to the function.
#greet("Jatin")

# we are going to give default value to the city parameter. So if we do not pass the city parameter, it will take the default value "Unknown".
def greet(name, city="Unknown"):
    print(f"Hello {name}, you are from {city}")

#greet("Jatin", "Mohali")
#greet("Arjun", "Delhi")
#greet("Jatin")


#Functions that return values
def add(a, b):
    return a + b

result = print(f"result of adding 2 fields= {add(10, 5)}")
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

x = add(10, 5)
y = multiply(x, 7)

print(y)