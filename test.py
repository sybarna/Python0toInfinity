# # # # # x = 0
# # # # # while x < 5:
# # # # #     print("the values of x are: " + str(x))
# # # # #     x += 1


# # # # product = 1
# # # # while x < 10:
# # # #     product = product * x
# # # #     x = x + 1


# # # # while loop inside if statment ? thought the loop will not come outside but think what in python its differentwhile loop can come outside if there's an if statment
# # # x = 4
# # # if x != 0:
# # #     while x % 2 == 0:
# # #         print(x)
# # #         x /= 2

# # # lets create a multiplication table to complete this looping confusion in python

# # def multiplication(x, limit):
# #     init = 1
# #     while init <= limit:
# #         print(f"{x} * {init} = {x * init}")
# #         init += 1


# # input_forX = int(input("enter a number to find its multiplication table"))
# # input_forL = int(input("how long should be the multiplication table ?"))

# # multiplication(input_forX, input_forL)


# # stopping an infinite while loop

# isTrue = True
# while isTrue:
#     print("alpha")
#     break


# inputing in reverse
name = "chandani"
beta = ""


for i in name:
    beta = str(i) + beta

print(beta)
