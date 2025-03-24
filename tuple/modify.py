# modifying the tuple data // as tuple is considered not mutable i will show you some trick to mutable wheich is called workaround

cloud_computing = ("datascience", "machinelearning")
print("Not modified tuple : {}".format(cloud_computing))


# workaround with list.

loud_computing = list(cloud_computing)
loud_computing.append("blockchain")
cloud_computing = tuple(loud_computing)
print("modified touple: {}".format(cloud_computing))
