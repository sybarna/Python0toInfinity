# my python first app in python
import math
campridge = "Capitalism"
print(campridge.upper())
# uppercasing the string stored in campridge


# counting the length of the string
print(len(campridge))

# replacing the characters
print(campridge.replace("a", "x"))

first = "subarna"
last = "katwal"

print(first.capitalize())
print(first + " " + last)  # string contcatenation.

# formatted string
formatted_string = f"{first} {last}"
print(formatted_string)


formatted_string2 = f"{len(first)} + 4"
print(formatted_string2)


# methods in string
methods_string = "my name is atmaramtukaram"
print(methods_string.capitalize())
print(methods_string.lower())

print(methods_string.upper())
print(methods_string.find("atma"))
print(methods_string.replace("atma", "bhoot"))

print("pro" in methods_string)
print("atma" in methods_string)


# numbers in python

# interger float and complex number / experiosn withimaginary numbers.

x = 123
y = 1.232
z = 2 + 3j


# division in python.
print(x / 3)  # this will give the result in floating point.
print(x // 3)  # this will give the result in interger double slash //
print(x % 3)
print((x - 120) ** 2)

# rounding this numbers.
print(round(8.5))
print(abs(-23))

print(math.sqrt(2))
print(math.ceil(3.1))  # gives the ceiling
print(math.factorial(3))

print(math.floor(2.9))  # gives the floor of the number


print(abs(-3))
