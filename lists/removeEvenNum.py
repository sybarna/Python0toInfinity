# removing even numbers from list
random_numbers = [948, 320, 715, 449, 827, 593, 283, 687, 181, 330,
                  641, 420, 107, 251, 234, 193, 358, 659, 863, 385,
                  142, 701, 618, 378, 122, 674, 208, 972, 950, 536,
                  614, 845, 264, 335, 912, 870, 448, 934, 765, 705,
                  892, 993, 109, 281, 911, 734, 622, 148, 236, 499,
                  378, 222, 817, 332, 601, 928, 310, 371, 185, 423,
                  791, 471, 506, 968, 156, 352, 287, 912, 318, 199,
                  498, 110, 763, 773, 479, 284, 621, 837, 144, 753,
                  831, 101, 416, 315, 680, 438, 264, 501, 386, 996,
                  665, 719, 889, 395, 300, 734, 580, 671, 405, 600]


# ask input
# print("enter collection of number to filter them out")

# for i in range(5):
#     value = int(input())
#     if value % 2 != 0:
#         store.append(value)


filtered_numbers = []

for index in range(len(random_numbers)):
    if random_numbers[index] % 2 != 0:
        filtered_numbers.append(random_numbers[index])
print(filtered_numbers)


print("there were {} even numbers here".format(
    len(random_numbers) - len(filtered_numbers)))
