# finding union intersection and difference of two sets.

set1 = {1, 34, 3, 2, 12, 5, 235, 2, 34, 112, 1}
set2 = {2, 34, 6, 23, 4, 2, 1, 46, 2, 34, 2}


intersection = set()


for index in set1:
    if index in set2:
        intersection.add(index)
print("Intersection of the set1 and set2 is: {}".format(intersection))


union = set1.union(set2)
print(union)


difference = set1.difference(set2)
print(difference)

print(len(set1))
