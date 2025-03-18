# # # # fundamentals of progarmming.


# # # # Else if conditions.
# # # temperature = 30

# # # if temperature == 30:
# # #     print("you are enjoying this weather")
# # #     print("seems you are on the right place today ")

# # # elif temperature > 30:
# # #     print("its preety hot here")

# # # else:
# # #     print("how about you change loccation")


# # # # another example.

# # # x = input("whats your age :")
# # # x = int(x)
# # # if x < 13:
# # #     print("child spotted")
# # # elif x >= 13 & x <= 19:
# # #     print("you have become a teenager")
# # # else:
# # #     print("you are now an adult")

# # # shortcut = 1
# # # message = "kodomo" if shortcut < 3 else "omai mo hontoni kodomo"
# # # print(message)
# # # alpha = input("enter value for alpha : ")
# # # message = ord(alpha)
# # # # ternary operators
# # # if message == 3 and message != 0:
# # #     print("you just passed infant")
# # # elif message >= 3 and message <= 100:
# # #     print("hehehe hoho hahahahah")

# # # else:
# # #     print("shitty coder")

# # # jack

# # name = input("enter name :")
# # if name == "jack" or "mack":
# #     print("pakc")


# # & and or operators
# alpha = True
# beta = False

# message = "pingo" if alpha and beta == True else "bingo"
# print(message)

# value_x = int(input("value for x "))
# value_y = int(input("value for y "))

# if value_x > value_y and value_x < 10 and not value_x == 9:
#     print("bingo")


# Age checker
# age must be between 18 and 30
age = int(input("enter your age : "))
if 18 <= age < 30:
    print("you are qualified")
