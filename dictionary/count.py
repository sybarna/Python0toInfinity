# string : input
# count how many character is present in the string and display with key element side by side the numbers of time its been present there

name = "subarna"
store = {}
for x in range(len(name)):

    if name[x] not in store:
        store[name[x]] = 1
    else:

        store[name[x]] += 1


print(store)
