sentence = "my name is subarna subarna katwal"

words = sentence.split()

store = {}

for x in words:
    if x not in store:
        store[x] = 1
    else:
        store[x] += 1

print(store)
