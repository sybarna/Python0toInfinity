indexed = ((23, 42, 34, 2, 34, 2, 34, 23, 4, 2, 989898), (2, 34, 22, 31, 31, 231),
           (234, 23, 42, 3, 42, 234, 2, 123, 989898), (989898, 54, 5, 234, 1231, 123, 123), (23))

cowboy_saver = []

for i, indexing in enumerate(indexed):
    if isinstance(indexing, (tuple, list)) and 989898 in indexing:
        save = indexing.index(989898)

        cowboy_saver.append((i, save))


supercowboy_saver = tuple(cowboy_saver)
print(supercowboy_saver)
