# #creating a calculator app

def pro(result, second):
    return result * second


def sub(result, second):
    return result - second


def add(result, second):
    return result + second


def div(result, second):
    return result / second


# istrue = True
# while istrue:

#     alpha = input("enter a number")
#     while alpha != "":
#         sign = input("enter a sign")
#         result = pro(alpha) if sign == "*"  else sub(alpha) if  sign == "-" else add(alpha) if  sign == "+" else  div(alpha) if sign == "/" else  pow(alpha) if sign == ("^") else None
first = int(input(""))
sign = input("")
issign = True
while sign in ["/", "*", "-", "+"]:

    second = int(input(""))  # asks everytime input if sign is entered

    if sign == "*":
        first = (pro(first, second))
        print(first)

    elif sign == "/":
        first = (div(first, second))
        print(first)
    elif sign == "+":
        first = (add(first, second))
        print(first)
    elif sign == "-":
        first = (sub(first, second))
        print(first)
    else:
        None

    # ask every time sign input until and unless sign == none / something otther
    sign = input("")
