#!/usr/bin/python3

for x in range(ord('Z'), ord('A') - 1, -1):
    (print(chr(x).lower(), end="") if x % 2 == 0
     else print(chr(x), end=""))

# for i, letter in enumerate(list(
#     chr(index) for index in range(ord("A"),
#                                   ord('Z') + 1))[::-1]):
#     if i % 2 == 0:
#         print("{:s}".format(letter.lower()), end='')
#     else:
#         print("{:s}".format(letter), end='')
