list_marks = [1, 2, 2, 2, 42, 4, 23, 25, 3, 42, 32, 8]
# here the list is contanimated
list_marks = set(list_marks)

# print(list_marks)

# # now given two sets : a & b find semmetric difference without using functions.
a = {1, 2, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8}


# c = a.union(b)
# a = c.difference(a)
# b = c.difference(b)

# print(a, b)


# googles way.


not_inB = {x for x in a if x not in b}
not_inA = {x for x in b if x not in a}

print(not_inB.union(not_inA))
