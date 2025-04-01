# # # # functions in python
# # # def funky(a, b):
# # #     print(f"Funcky duncky {a}")
# # #     print(f"wow what an amazing language we are free to fuck it up {b} ")


# # # a = input("enter value for a")
# # # b = input("enter value for b")
# # # funky(a, b)


# # # return type function in python
# # def returtype(value):
# #     return f"hi {value}"


# # pritingvalue = returtype(9)
# # print(pritingvalue)

# # incrementing using functions.

# def incre(a, b):
#     return a + b


# print(incre(2, 4))


# passing multiple values in function

def multifunction(*alabama):
    total = 1
    for number in alabama:
        total *= number
    return (total)


print(multifunction(1, 2, 2, 2, 3, 34, 4))
