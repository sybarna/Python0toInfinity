lengthe_of = ["def", "abc"]
print(len(lengthe_of))


# find the length of the list "each element inside it too"

# like if "subarna", "katwal" its 2 length in list but what about the naming length, here you go
count = 0
for length in lengthe_of:
    count = len(length) + count

print(f"You have total {count} characters in the list", count)
