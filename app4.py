# prime number. // easy peasy
import math
for number in range(2, 100):
    issquare = True
    sqroot = math.isqrt(number)
    for sumber in range(2, sqroot+1):
        if number == 2 or number == 3:
            break
        elif number % sumber == 0:
            issquare = False
            break

    if issquare:
        print(number)
