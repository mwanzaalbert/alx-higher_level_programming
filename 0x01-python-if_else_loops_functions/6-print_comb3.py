#!/usr/bin/python3

for i in range(10):
    for j in range(i+1, 10):
        if i == 0 and j == 1:
            print("01", end=", ")
        else:
            print("{}{}".format(i, j), end="")
            if i != 8 or j != 9:
                print(", ", end="")
            else:
                print("")
