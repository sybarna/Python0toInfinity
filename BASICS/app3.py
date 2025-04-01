# prime number.
import math
number = int(input("enter a number to check prime numbers :"))

isprime = True

if number < 2:
    print("not a prime number")
elif number == 2 or number == 3:
    print("prime number spotted")

else:
    sqroot_number = math.isqrt(number)
    for numb in range(2, sqroot_number+1):
        if number % numb == 0:
            isprime = False
            break

if isprime == True:
    print("prime number spotted")

else:
    print("not a prime number")
