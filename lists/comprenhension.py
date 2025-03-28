# # # # # # # # comprenhension practice in python

# # # # # # # a = 2
# # # # # # # b = ['ragav' if a % 2 == 0 else 'binit']
# # # # # # # print(b)

# # # # # # # listing out even nunbers from 1 to 100 using list comprenhension


# # # # # # # even = [x for x in range(100) if x % 2 == 0]

# # # # # # # print (even)
# # # # # # # a little more advance level list comprenhension

# # # # # # # store square numbers for 1 to 10 inclusive

# # # # # # # store = [x*x for x in range(11)]
# # # # # # # print(store)


# # # # # # # converting into the uppercase


# # # # # # words = ['bhairav', 'kapaldev', 'sitafal', 'mitha']

# # # # # # Uwords = [x.upper() for x in words]
# # # # # # print(Uwords)


# # # # # # # x for x in ragnge (XYZ)   the firs x means the values to be provided. the second x is the iternation (i) we use in every looping


# # # # # # filter_words = [x for x in words if len(x) < 6]
# # # # # # print(filter_words)


# # # # # # # (1,1), (2,4), (3,9), (4,16), (5,25), (6, 36)... (10, 100)

# # # # # # format_svaing = [(x, x*x) for x in range(11)]

# # # # # # for x in format_svaing:
# # # # # #     print(x)


# # # # # # print multiples of 3 in tuple

# # # # # # multi3 = [x for x in range(20) if x % 3 == 0]
# # # # # # print(multi3)


# # # # # # list of list

# # # # # # nested list

# # # # # list = [[2, 3], [3, 4], [5, 6]]
# # # # # openingnesting = [elements for sublist in list for elements in sublist]
# # # # # print(openingnesting)


# # # # matrix = [["apple", "banana"], ["cherry", "date"], ["fig", "grape"]]


# # # # flattned = [x for x in matrix for x in x]
# # # # print(flattned)


# # # # squaring odd numbers

# # # squares = [x*x for x in range(10) if x % 2 != 0]

# # # print(squares)


# # words = ["hello", "world", "python", "programming"]

# # reversedwords = [x[::-1] for x in words]
# # print(reversedwords)


# # dictionary list comprenhesnion
# listing = [{x: x*x} for x in range(5)]
# print(listing)


# finding out all the palindrome form a string

words = ["madam", "hello", "racecar", "world"]

palin = [x for x in words if x[::-1] == x]
print(palin)
