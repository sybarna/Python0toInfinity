# learning out return type and non return type functions in py
def returntype(aalu):
    balu = aalu + aalu
    return balu


kauliflower = returntype("masu") + "kera"
print(kauliflower)


# the above program is for return type function.
# the below program is going for non return type function


def nonreturntuype(i_do_myself):
    print(i_do_myself)
    return "lado"


print("this is what it printed", nonreturntuype(9))
