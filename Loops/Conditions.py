age = 35

if age >= 18:
    print("adult")
else:
    print("minor")


#Multiple conditions
score = 75

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Fail")


x = 10
y = 20

print(x == y)   # equal to
print(x != y)   # not equal to
print(x > y)    # greater than
print(x < y)    # less than
print(x >= y)   # greater than or equal
print(x <= y)   # less than or equal

age = 25
has_id = True

if age >= 18 and has_id:
    print("entry allowed")

if age < 18 or age > 60:
    print("special assistance needed")

if not has_id:
    print("no entry without ID")


age = 25
member = True

if age >= 18:
    if member:
        print("full access")
    else:
        print("limited access")
else:
    print("no access")    



age = 20
status = "adult" if age >= 18 else "minor"
print(status)


# These are all falsy — treated as False
0
""          # empty string
[]          # empty list
{}          # empty dictionary
None        # no value

# Everything else is truthy — treated as True
name = ""
skills = []

if name:
    print("name exists")
else:
    print("name is empty")

if skills:
    print("has skills")
else:
    print("no skills yet")


role = "admin"

match role:
    case "admin":
        print("full access")
    case "editor":
        print("can edit content")
    case "viewer":
        print("read only")
    case _:
        print("unknown role")