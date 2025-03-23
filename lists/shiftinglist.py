# # Write a program to rotate a list to the left by 2 positions.

# list = [1, 2, 3, 4, 5, 6, 9]
# bist = []
# for i in range(2):
#     bist.append(list[0])
#     list.pop(0)

# list = list + bist

# print(list)


# the abouve method was my way without any piroor knowledge of slicing

# lets do with slicing
list = [1, 2, 3, 4, 5, 6]

list = list[2:] + list[:2]

print(list)
