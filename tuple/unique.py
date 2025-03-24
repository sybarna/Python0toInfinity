# # checking if a tuple contains only unique elements ?
# group = (9, 2, 3, 2, 4, 2, 7, 2, 1, 2, 3, 4, 5, 94, 35, 6, 4, 4, 3, 2, 3)
# istrue = True

# for index in group:
#     if (group.count(index)) > 1:
#         istrue = False
#         break


# if istrue:
#     print("tuple contains only unique data")

# else:
#     print("we find duplicates in tuple")


# GOOGLES APPROACH ?#
group = (9, 2, 3, 2, 4, 2, 7, 2, 1, 2, 3, 4, 5, 94, 35, 6, 4, 4, 3, 2, 3)
isTrue = True
seen = set()

for index in group:
    if index in seen:
        isTrue = False
        break
    seen.add(index)

if isTrue:
    print("uniques")

else:
    print("duplicacy")
