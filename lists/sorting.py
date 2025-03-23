# # this is a sorting in list without using the sort function.
# arraytoSort = ["1", "2", "23", "99", "80", "48"]
# pappu = len(arraytoSort)
# for index in range(pappu):
#     for index in range(pappu-1):
#         temp = ""
#         if (arraytoSort[index] > arraytoSort[index + 1]):
#             temp = arraytoSort[index]
#             arraytoSort[index] = arraytoSort[index+1]
#             arraytoSort[index+1] = temp
# # print(arraytoSort)


# user input the list and we do the sroting now without any help from google.


listing = []

# adds the user assigned values to the list.


def addinglist(values):
    listing.append(values)

# ask user to insert the values 5 times


# we have commented out from here
print("enter the 5 values for your list")

for i in range(5):
    value = input()
    addinglist(value)


# sorting function

def wesort(listing):
    print("before sort: {}".format(listing))
    for jindex in range(len(listing)):
        for index in range(len(listing) - 1):
            if (listing[index] > listing[index+1]):
                temp = listing[index]
                listing[index] = listing[index+1]
                listing[index+1] = temp
    print("after sort: {}".format(listing))


wesort(listing)
