# finding elements in python

initializing_set = {2, 1, 12, 5, 23, 5, 23, 231, 23}

search = int(input("enter the element to search"))

if (search in initializing_set):
    print("bingo! Lucky draw winner")
else:
    print("Better luck next time")
