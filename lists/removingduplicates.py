# this code is here to remove all the duplicates elements in lists.
listing = [1, 2, 2, 2, 4, 2, 234, 22, 34, 23, 2, 342,
           2, 3, 1, 1, 2]    # a list withduplicates data

filtered = []
for index in listing:
    if index not in filtered:
        filtered.append(index)


print(filtered)


# with using set : ( we can remove all duplicates when using with set)

bist = [1, 23, 2, 31, 4, 12, 31, 4, 12, 4,
        34, 11, 23, 1, 23, 1, 4, 2, 1, 2, 31, 2]
unique = list(set(bist))
print(unique)
