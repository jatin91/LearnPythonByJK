#Modules and Imports
#As your code grows you cannot keep everything in one file. Modules are how Python lets you split code across files and reuse it.
"""
import JKUtils

print(JKUtils.add(5, 3))        # 8
print(JKUtils.subtract(5, 3))   # 2


# Inbuilt Modules
#Python comes with a lot of built in modules that you can import and use. For example, the math module provides mathematical functions:

import math
import random
import datetime
import os
import json
import sys

import math

print(math.pi)           # 3.14159...
print(math.sqrt(16))     # 4.0
print(math.ceil(4.3))    # 5 — rounds up
print(math.floor(4.9))   # 4 — rounds down
print(math.pow(2, 10))   # 1024.0 — 2 to the power 10


import random

print(random.randint(1, 100))        # random integer between 1 and 100
print(random.choice(["a", "b", "c"])) # random item from list
print(random.random())               # random float between 0 and 1

names = ["Jatin", "Arjun", "Priya"]
random.shuffle(names)
print(names)                         # list in random order


import datetime

now = datetime.datetime.now()
print(now)                           # current date and time
print(now.year)                      # just the year
print(now.month)                     # just the month
print(now.day)                       # just the day
print(now.strftime("%d-%m-%Y"))      # formatted as string

import sys

print(sys.version)      # Python version running
print(sys.platform)     # operating system
#sys.exit()              # stops the program immediately


from math import sqrt, pi

print(sqrt(25))   # no need to write math.sqrt
print(pi)         # no need to write math.pi

import datetime as dt
import random as rnd

now = dt.datetime.now()
print(rnd.randint(1, 100))
"""

from utils.JKUtils import multiply, divide
from utils.string_helpers import capitalise_all, join_words

print(multiply(10, 5))
print(divide(20, 4))
print(capitalise_all(["jatin", "arjun", "priya"]))
print(join_words(["Python", "AI", "Agents"], " → "))