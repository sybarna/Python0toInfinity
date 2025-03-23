listing = [1, 23, 2, 2, 34, 2, 34, 7, 6, 34, 532, 3, 242, 12, 3, 1]
listing = list(set(listing))
print(listing)
# greatest = 0
# second = 0
# upgraded with suggestion from internet

greatest = second = float('-inf')
for index in range(len(listing)):

    if greatest < listing[index]:
        second = greatest
        greatest = listing[index]

print(second)
