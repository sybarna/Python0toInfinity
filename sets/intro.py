alpha_set = {1, 2, 1, 2, 34, 2}
print(alpha_set)
# print(alpha_set[0]) we cannot call by indexing in sets. ()
alpha_set.pop()
alpha_set.add(9)
beta_list = [4, 2, 5, 2, 234, 5]
alpha_set.update(beta_list)      # method to add elements in sets()
# throws error if we don't find the removing element in the set()
alpha_set.remove(9)
# doesn't throw error even we don't find out the specific data
alpha_set.discard(9)

for index in alpha_set:
    print(index)

# adding element in sets()

print(9 in alpha_set)
