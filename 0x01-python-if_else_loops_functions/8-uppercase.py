#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            offset = ord('A') - ord('a')
            c = chr(ord(c) + offset)
        print("{}".format(c), end="")
    print()

