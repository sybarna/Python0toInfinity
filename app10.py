# principles of code reuse.
# create a lucky number generator game.

def findingLuckNo(name):
    lucky = len(name) * 3
    print("your lucky number is: ", lucky)


alpha = input("enter yoru name")
beta = input("your girlfriend name")

findingLuckNo(alpha)
findingLuckNo(beta)
