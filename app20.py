# # counting the number of dedicated alphabet in a string


# name = "subarna"
# print(name.count("a"))


# print("arna" in name)


# formated string with conversion degree and celcious

def tempConversion(temp):
    return (temp - 32) * 5/9


for x in range(0, 101, 10):
    print("{:5} F  | {:>5.2f} C".format(x, tempConversion(x)))
