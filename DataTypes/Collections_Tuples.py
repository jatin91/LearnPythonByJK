"""

Why would you want something you cannot change
Some data should never be modified. For example:

GPS coordinates of a fixed location
Days of the week
RGB color values
Database column names

If you use a list, someone could accidentally modify it. A tuple protects that data permanently.

"""
#Tuples
#A tuple is like a list but it is immutable — you cannot change it after creating.
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed = ("Jatin", 35, True)

colors = ("red", "green", "blue")

print(colors[0])    # red
print(colors[-1])   # blue
print(colors[1:3])  # ("green", "blue")

#Tuples are immutable meaning you cannot change them after creating. This is a key difference from lists. If you try to change an item in a tuple, you will get an error:
colors = ("red", "green", "blue")
colors[0] = "yellow"   # TypeError — tuple does not support item assignment
colors.append("black") # AttributeError — tuple has no append


#tuples have some of the same methods as lists, but not all. For example, you can use count() and index() with tuples, but not append() or remove().
colors = ("red", "green", "blue")

print(len(colors))           # 3
print("red" in colors)       # True
print(colors.count("red"))   # 1 — how many times value appears
print(colors.index("green")) # 1 — position of value

#   If you need to modify a tuple, you can convert it to a list, make the changes, and then convert it back to a tuple:
colors_tuple = ("red", "green", "blue")
colors_list = list(colors_tuple)    # tuple to list
colors_list.append("yellow")        # now you can modify
colors_tuple = tuple(colors_list)   # back to tuple
print(colors_tuple)

#Real world use — functions returning multiple values
#When a function needs to return more than one value it uses a tuple:
#Python automatically packs multiple return values into a tuple. The unpacking on the last two lines is the clean way to handle it.
def get_user():
    name = "Jatin"
    age = 35
    return name, age

result = get_user()
print(result)         # ("Jatin", 35)
print(result[0])      # Jatin

name, age = get_user()
print(name)           # Jatin
print(age)            # 35