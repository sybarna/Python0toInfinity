# nestedlooping

for i in range(7):
    for j in range(i, 7):
        print(i, j, end="")

    print()


for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


# now here caomes the home vs away challenge in a match created through descions.

teams = ["ARG", "BRA", "USA", "GER", "NEP", "IND", "FRC", "GER"]

for home in teams:
    for away in teams:
        if home == away:
            print(f"{home} vs {away}")
