#A list is an ordered collection of items. Items can be of any type — strings, integers, floats, booleans, even other lists.
"""
names = ["Jatin", "Arjun", "Priya"]
numbers = [10, 20, 30, 40]
mixed = ["Jatin", 35, True, 5.11]

print(names)
print(numbers)
print(mixed)
print(type(names))
print(type(numbers))
print(type(mixed))

#Accessing items — Indexing
#Every item in a list has a position number called an index. Index always starts at 0, not 1.

names = ["Jatin", "Arjun", "Priya"]
print( "Indexing")
print(names[0])   # Jatin
print(names[1])   # Arjun
print(names[2])   # Priya

#Negative indexing
#Python lets you count from the end using negative numbers:
#Useful when you do not know how long a list is but you always want the last item.
print("Negative indexing")
print(names[-1])  # Priya  — last item
print(names[-2])  # Arjun  — second from last

#Slicing — getting a portion of a list
#How slicing actually works
#The full slicing syntax is:
#list[start:stop:step]

#start — where to begin
#stop — where to end
#step — how many positions to jump each time


print("Slicing ")
print(names[0:2])  # Jatin, Arjun
print(names[1:3])  # Arjun, Priya
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30] — index 1 up to but not including 3
print(numbers[:3])    # [10, 20, 30] — from start up to index 3
print(numbers[2:])    # [30, 40, 50] — from index 2 to end
print(numbers[::3])   # [10, 30, 50] — every second item

#Changing items
#Lists are mutable — you can change them after creating:

print("Changing items")
names = ["Jatin", "Arjun", "Priya"]
names[1] = "Rahul"
print(names)   # ["Jatin", "Rahul", "Priya"]

#Adding items
#You can add items to a list using the append() method:
print("Adding items")

names = ["Jatin", "Arjun", "Priya"]
names.append("Rahul")        # adds to the end
print(names)

names.insert(1, "Vikram")    # adds at specific position
print(names)

names.extend(["Neha", "Pooja"])  # adds multiple items
print(names)
names = ["Jatin", "Arjun"]

names.append(["Priya", "Rahul"])
print(names)
#append adds the entire list as a single item — so you end up with a list inside a list. extend unpacks the items and adds them individually.

#Removing items
#You can remove items using the remove() method:
names = ["Jatin", "Arjun", "Priya", "Rahul"]

names.remove("Arjun")    # removes by value, it removes the first occurrence of the value in the list. If there are multiple occurrences, only the first one will be removed.
print(names)

#names.remove("Arjun")    # Wrong valueremoves by value
#print(names)

names.pop()              # removes last item
print(names)

names.pop(0)             # removes item at specific index IMP You tell it where to remove. Key difference — it gives back the removed item so you can use it.
print(names)

del names[0]             # another way to delete by index
print(names)

del names
print(names)  # NameError — names no longer exists


#Checking if something exists in a list
names = ["Jatin", "Arjun", "Priya", "Rahul"]
if "Arjun" in names:
    print("Arjun is in the list")
else:
    print("Arjun is not in the list")

if "Arjun1" in names:
    print("Arjun1 is in the list")
else:
    print("Arjun1 is not in the list")

#Useful list information

    numbers = [10, 20, 30, 40, 50]

print(len(numbers))    # 5 — how many items
print(sum(numbers))    # 150 — total of all numbers
print(min(numbers))    # 10 — smallest
print(max(numbers))    # 50 — largest



# Sorting lists
numbers = [40, 10, 50, 20, 30]

numbers.sort()              # sorts in place, ascending by default
print(numbers)

numbers.sort(reverse=True)  # sorts descending
print(numbers)

names = ["Priya", "Jatin", "Arjun"]
names.sort()                # alphabetical
print(names)


#Copying a list — the trap everyone falls into
original = [1, 2, 3,5,6,7,8,9,10]
copy = original         # this is NOT a copy

copy.append(4)
print(original)         # [1, 2, 3, 4] — original changed too
#Both variables point to the same list in memory. To make a real independent copy:
copy = original.copy()
copy = original[1:2]       # slicing also works
print(copy)             # [1, 2, 3] — original is unchanged
#Try both — confirm original does not change when you modify the copy.


"""
students = [
    ["Jatin", 35, "Mohali"],
    ["Arjun", 28, "Delhi"],
    ["Priya", 30, "Mumbai"]
]

print(students[0])        # first student — full row
print(students[0][0])     # first student's name
print(students[1][2])     # second student's city


# Real time AI chatbot conversation example using lists
conversation = []

conversation.append("Hello Claude")
conversation.append("How can I help you?")
conversation.append("Tell me about Python")

print(conversation)
print(f"Total messages: {len(conversation)}")
print(f"Last message: {conversation[-1]}")