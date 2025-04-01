# listing the elements listing is a god removing a listing variable.

# names = ["ram", "shyam", "krishma", "bhagat", "rawan", "sita"]
# words = "ram"
# names.remove(words)


# print(names)

# lists using group of fruits and some objects.

fruits_basket = ["apple", "guava", "pineapple", "mango", "banana", "mango"]

# it counts how many data are presneted of the search in the list
print(fruits_basket.count("mango"))
(fruits_basket.append("peach"))
print(fruits_basket)
print(fruits_basket.index("banana"))
fruits_basket.pop()

fruits_basket.remove("mango")
fruits_basket.remove("mango")

fruits_basket.sort()

fruits_basket.insert(90, "orange")
print(fruits_basket)

length = 0
for i in fruits_basket:
    print(i)
    length = len(i) + length
print(length)
