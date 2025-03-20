# validating a username using a fucntion and branching a if statements.

def validate(usename):
    if (len(usename) < 3):
        print("Invalid usename: must be imposter")


user = input("enter usename")

validate(user)


def even_num_Checker(num):
    if (num % 2 == 0):
        return True
    else:
        return False


numnber = int(input("enter a number"))

print("the number is even" if even_num_Checker(
    numnber) else "the number is odd")


print("a" > "A")
