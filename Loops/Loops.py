
"""

# Looping through a list of names and printing each name
names = ["Jatin", "Arjun", "Priya"]

for name in names:
    print(name)

for n in names:
    print(f"Hello {n}!")

# looping through dictionary of students and printing their names and ages

person = {"name": "Jatin", "age": 35, "city": "Mohali"}

for key, value in person.items():
    print(f"{key} : {value}")

# Looping through a range of numbers
for i in range(5):
    print(i) # 0 to 4

for i in range(1, 6):
    print(i)      # 1 to 5
for i in range(0, 10, 2):
    print(i)  # 0 to 8, step 2
for i in range(10, 0, -1):
    print(i) # 10 down to 1    

#while loop
# 
count = 0

while count < 5:
    print(count)
    count += 1        

#break and continue
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    print(number)

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue
    print(number)


names = ["Jatin", "Arjun", "Priya"]

for index, name in enumerate(names):
    print(f"{index} : {name}")


for index, name in enumerate(names,start=1):
    print(f"{index} : {name}")

#nested loops


teams = ["A", "B"]
members = ["Jatin", "Arjun", "Priya"]

for team in teams:
    for member in members:
        print(f"Team {team} — {member}")
"""
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi Jatin"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I am good"}
]

for message in messages:
    if message["role"] == "assistant":
        print(f"Claude said: {message['content']}")
    if message["role"] == "user":
        print(f"User said: {message['content']}")    