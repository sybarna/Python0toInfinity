datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(datas[:3])


# printing first three element

mystring = "python"
print(mystring[2:10])
print(mystring[2:4])
# printing out from index 2 to index 10 "If theres no element in the index it will print nothing"

print(datas[:-1])

# printing out only the last elements


print(datas[1::3])
print(datas[2:])

print(datas[::-1])
print(mystring[::-1])

print(mystring[-3:])


subdatas = datas[1:7:2]
print(subdatas)

print(datas[:-3])
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
filtr_tuple1 = tuple_1[::-2]
print(filtr_tuple1)
