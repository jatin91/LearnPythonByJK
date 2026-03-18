#In real apps you constantly need to read and write files — config files, data files, logs, exported reports. This is how Python does it.
"""
# How to read a file in Python

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#The better way — with statement
#Manually closing files is easy to forget. Use with instead — it closes automatically:

with open("data.txt","r") as file:
    content=file.read()
    print(content)

# Lets read a file line by line — useful for large files

with open("data.txt","r") as file:
    for line in file:
        print(line.strip())  
        print(line.strip())     


#Reading all lines into a list

with open("data.txt","r") as file:
    lines=file.readlines()
    print(lines)    # list of lines with newline characters
    print(lines[0].strip())
    lines = [line.strip() for line in lines]  # remove newlines
    print(lines)    # list of lines without newlines



#How to write to a file in Python

with open("output.txt", "w") as file:
    file.write("Hello Jatin\n")
    file.write("This is line 2\n")

#Appending to a file — use "a" mode instead of "w"

with open("outputAppend.txt", "a") as file:
    file.write("This line is added via using append mode \n")


# "r"   # read only — file must exist
# "w"   # write — creates new, overwrites existing
# "a"   # append — adds to end, creates if not exists
# "r+"  # read and write — file must exist


#File Handling error :

try:
    with open("missingFile.txt", "r") as file:
        content1 = file.read()
except FileNotFoundError:
    print("file does not exist")
except PermissionError:
    print("no permission to read this file")    


# working with file paths

import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "data.txt")

print(current_dir)
print(file_path)

with open(file_path, "r") as file:
    print(file.read())
#  os.getcwd() gets your current working directory. os.path.join() builds a path correctly for any operating system — Windows uses '\', Linux uses '/'. This handles it automatically.


#Checking if a file exists before opening

import os

if os.path.exists("data1.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("file not found")

"""
import json
import os

def save_conversation(messages, filename="conversation.json"):
    with open(filename, "w") as file:
        json.dump(messages, file, indent=2)
    print("conversation saved")

def load_conversation(filename="conversation.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi Jatin"}
]

save_conversation(messages)
loaded = load_conversation()
print(loaded)