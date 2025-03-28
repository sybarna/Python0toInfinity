# # grouping words with the same length.
collections = ["man", "can", "funny", "runny", "money", "honey", "elephant"]

grouping = {}

for x in collections:
    length = len(x)
    if length not in grouping:
        grouping[length] = [

        ]
    else:
        grouping[length].append(x)

for key, value in grouping.items():
    print(f"length {key} : {value}")


# practicing again.

# # grouping words with same length

# collections = ["car", "far", "carry", "harry", "rakhi"]
# groups = {}

# for i in collections:
#     lengths = len(i)
#     if lengths not in groups:
#         groups[lengths] = []
#         groups[lengths].append(i)
#     else:
#         groups[lengths].append(i)

# for keys, values in groups.items():
#     print(f"length{keys}: {values}")
