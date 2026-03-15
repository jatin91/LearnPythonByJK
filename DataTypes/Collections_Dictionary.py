
# Example of a dictionary
person = {
    "name": "Jatin",
    "age": 35,
    "city": "Mohali"
}
"""
#Dictionaries
#A list stores items by position. A dictionary stores items by name.
#Instead of asking "give me item at index 2" you ask "give me the value for key name".

# Example of a dictionary
person = {
    "name": "Jatin",
    "age": 35,
    "city": "Mohali"
}

print(person["name"])   # Jatin
print(person["age"])    # 35

#Invalid key

print(person["country"])   # KeyError: 'country'

# Example of a dictionary
person = {
    "name": "Jatin",
    "age": 35,
    "city": "Mohali"
}
#get() never throws an error. If key does not exist it returns None or a default you provide. In real apps always use get() over direct access — it is safer.
print(person.get("country"))           # None
print(person.get("country", "India"))  # India — default value


#Adding items
#If you want to add a new key-value pair to the dictionary, you can simply assign a value to a new key:
#Same syntax for both. If key exists it updates, if not it creates.
person["country"] = "India"    # adds new key
person["age"] = 36             # updates existing key
print(person)

#Removing items
person.pop("city")      # removes by key, returns the value
del person["country"]   # removes by key, returns nothing
print(person)

print("name" in person)     # True
print("salary" in person)   # False

#Iterating over a dictionary
person = {
    "name": "Jatin",
    "age": 35,
    "city": "Mohali"
}

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
#The third one — items() — is the most used in real code because you get both key and value together.
for key, value in person.items():
    print(f"{key} : {value}")



person = {
    "name": "Jatin",
    "age": 35,
    "address": {
        "city": "Mohali",
        "state": "Punjab",
        "country": "India"
    }
}

print(person["address"]["city"])     # Mohali
print(person["address"]["country"])  # India
print(person.get("address", {}).get("city"))  # Mohali
print(person.items())

"""

users = [
    {"name": "Jatin", "age": 35, "city": "Mohali"},
    {"name": "Arjun", "age": 28, "city": "Delhi"},
    {"name": "Priya", "age": 30, "city": "Mumbai"}
]

print(users[0])              # first user — full dictionary
print(users[0]["name"])      # first user's name
print(users[1]["city"])      # second user's city
print(users.__getitem__(2)["age"])  # third user's age using __getitem__ method

person = {"name": "Jatin", "age": 35}

print(len(person))       # 2 — number of keys
print(person.keys())     # all keys
print(person.values())   # all values
print(person.items())    # all key value pairs

person.clear()           # removes everything
print(person)            # {}