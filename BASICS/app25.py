# # # # # DICTIONARY IN PYTHON

# # # # alpha = {
# # # #     "abc": 12,
# # # #     "yzx": 14
# # # # }


# # # # print(["abc" in alpha])


# # # # # looping in dictionary

# # # # students = {"grade1": 41, "grade2": 22, "grade3": 19, "grade4": 85}

# # # # for grades, amount in students.items():
# # # #     print(f"We have {amount} no of students in {grades}")


# # # # for grades in students.keys():
# # # #     print(grades)


# # # # for grades in students.values():
# # # #     print(grades)


# # # # for grades in students.items():
# # # #     print(grades)


# # # # def count_letters(text):
# # # #     result = {}
# # # #     for letter in text:
# # # #         if letter not in result:
# # # #             result[letter] = 0
# # # #         result[letter] += 1
# # # #     return result


# # # # print(count_letters("aaaaa"))

# # # def count(name):
# # #     countings = {}
# # #     for alphabets in name:
# # #         if alphabets not in countings:
# # #             countings[alphabets] = 0
# # #         countings[alphabets] += 1
# # #     return countings


# # # print(count("Subarna"))
# # # same code just to make sure i know all labout dictionaries.

# # alpha = "subarna"
# # store = {}
# # for index in alpha:
# #     if index not in store:
# #         store[index] = 0
# #     store[index] += 1
# # print(store)

# # using while loop to do this chutiyappa question thinking it will make me more confident

# texts = "i love to visit pashupatinath tempzzzzzle, it feels like people are scared to do something unholy there, i feel the environment, the smell of burning dead, the emotionless sightseeyers on another banks admiring its where it all ends and relaxing and giving tribute to others end. A truely creul traditions for people born outside the religion"
# storeme = {}
# i = 0
# while i < len(texts):

#     letter = texts[i]

#     if letter not in storeme:
#         storeme[letter] = 0
#     storeme[letter] += 1
#     i += 1


# print("z" in storeme)
# print(storeme["z"])


# Welcome to the real dictioinary

dictionary = {}
# you can add anythihig to this dictionary with keys and values.
