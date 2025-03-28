# creating a single dictionary using 2 lists one of them is key and other is values.

keys = [1, 2, 3, 4, 5, 6]
values = ["ram", "shyam", "sita", "gita", "ramesh", "gita"]
connections = {}


# for length in range(len(keys)):
#     connections[keys[length]] = values[length]

# print(connections)


# googles way.

connections = dict(zip(keys, values))
print(connections)
