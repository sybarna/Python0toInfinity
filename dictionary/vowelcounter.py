# counting the number of vowel here in python

greeting = "how are you boyaaah ? "
store = {}
vowels = ['a', 'e', 'i', 'o', 'u']
for x in range(len(greeting)):
    if greeting[x].lower() in vowels:
        if greeting[x] not in store:
            store[greeting[x]] = 1
        else:
            store[greeting[x]] += 1

print(store)
