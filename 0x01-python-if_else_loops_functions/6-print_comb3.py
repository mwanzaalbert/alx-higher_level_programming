#!/usr/bin/python3

for i in range(1, 10):
    for j in range(i+1, 10):
        if i == 1 and j == 2:
            print("{}, {}".format(i-1, j-1), end=", ")
        else:
            print("{}, {}".format(i, j), end="")
            if i != 8 or j != 9:
                print(", ", end="")
            else:
                print("")
