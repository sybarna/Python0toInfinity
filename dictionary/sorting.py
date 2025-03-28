# # # sorting disctionary

# collection = {
#     "bus": "1",
#     "sus": "2",
#     "dus": "5",
#     "lus": "3",
#     "mus": "4"
# }

# # for values in collection.items():
# #     print(values)


# # # converting dictionay into list

# # listcollection = list(collection.items())

# sorted_coll = dict(sorted(collection.items(), key=lambda item: item[1]))

# print(sorted_coll)

store = {
    "books": 10,
    "copies": 20,
    "pencils": 5

}


arranged_store = dict(sorted(store.items(), key=lambda item: (item[1])))
print(arranged_store)
