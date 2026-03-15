name = "Jatin"
age = 35
city = "Mohali"
country = "India"
profession = "developer in training"
print(name)
print(age)
print(city)
print(country)
print(profession)
print(type(name))
print(type(age))
print(type(city))
print(type(country))
print(type(profession))


country = 12.3
print(country)

print(type(country))

age = 25
name = "Jatin"

# this like is going to give error because we cannot add string and integer together.
#print(age + name)

# this is conversion of age to string.
print(name + " is " + str(age) + " years old")

# some other examples of type conversion
num1 = 10
num2 = 20.5
print(num1 + num2)  # this will give 30.5 because num2 is a float
print(float(num1) + num2)  # this will also give 30.5

#Cleaner way to do the same thing
#There is a better way to mix variables and text in Python called f-strings. Used everywhere in real code:

print(f"{name} is {age} years old") 