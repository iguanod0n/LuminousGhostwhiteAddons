# This is how we commenting in Python
# Hello, World!
print("Hello, World!")

# Variables & Types
print("====================================")
mystring = "Hello"
myfloat = 10.0
myint = 69

if mystring == "Hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 69:
    print("Integer: %d" % myint)

# Lists
print("====================================")
# appending
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = []
strings.append("Hello")
strings.append("World")
names = ["John", "Eric", "Jessica"]

second_name = None

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
