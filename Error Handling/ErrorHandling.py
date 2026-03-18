"""
#Error handling lets you catch that crash and decide what to do instead.
numbers = [1, 2, 3]
print(numbers[10])   # IndexError — program crashes here
print("this never runs")

# to Fix this, we can use a try-except block:
numbers = [1, 2, 3]

try:
    print(numbers[10])
except:
    print("something went wrong")

print("program continues")

#Catching specific exceptions
#Catching every error with a bare except is bad practice — you hide bugs you did not expect. Always catch specific exceptions:


numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:
    print("index does not exist")


#You can also catch multiple exceptions in one except block:
try:
    age = int(input("Enter age: "))
    print(10 / age)
except ValueError:
    print("that is not a number")
except ZeroDivisionError:
    print("age cannot be zero")




try:
    age = int(input("Enter age: "))
except ValueError:
    print("not a number")
else:
    print(f"age is {age}")   # runs only if no exception
finally:
    print("always runs")     # runs no matter what   

#else — runs when try block succeeded with no errors
#finally — runs always, error or not. Used for cleanup — closing files, closing database connections


#Getting the error details

numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError as e:
    print(f"Error: {e}")

def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    if age > 150:
        raise ValueError("age is not realistic")
    return age

try:
    age = int(input("Enter age: "))
    print(set_age(age))
except ValueError as e:
    print(f"Invalid: {e}")

#Real work example of error handling: via clauding API calls. You can get all kinds of errors — network errors, unexpected response structure, etc. You can catch them and decide what to do instead of crashing your program:
def call_api(user_message):
    try:
        response = get_api_response(user_message)
        return response["content"][0]["text"]
    except KeyError:
        return "unexpected response structure"
    except ConnectionError:
        return "could not connect to API"
    except Exception as e:
        return f"something went wrong: {e}"
    finally:
        print("API call attempt completed")    

try:
    data = get_data()
    try:
        result = process(data)
    except ValueError:
        result = default_value
except ConnectionError:
    print("could not get data")
"""
class InvalidAgeError(Exception):
    pass

class EmptyNameError(Exception):
    pass

def create_user(name, age):
    if not name:
        raise EmptyNameError("name cannot be empty")
    if age < 0:
        raise InvalidAgeError("age cannot be negative")
    return {"name": name, "age": age}

try:
    user = create_user("", 25)
except EmptyNameError as e:
    print(f"Name error: {e}")
except InvalidAgeError as e:
    print(f"Age error: {e}")

IndexError      # list index out of range
KeyError        # dictionary key not found
TypeError       # wrong type operation
ValueError      # right type wrong value
FileNotFoundError  # file does not exist
ZeroDivisionError  # dividing by zero
NameError       # variable not defined
AttributeError  # method does not exist on type