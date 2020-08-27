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

# Basic Operators
print("====================================")
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 5 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello " * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print("====================================")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")