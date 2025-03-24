numbers = (9, 2, 3, 2, 4, 2, 7, 2, 1, 2, 3, 4, 5, 94, 35, 6, 4, 4, 3, 2, 3)
whichnumtocount = int(input(
    "enter a number to find how many time its repeated in tuple"))
counted = numbers.count(whichnumtocount)
print("the number is repeated for {}".format((counted)))
