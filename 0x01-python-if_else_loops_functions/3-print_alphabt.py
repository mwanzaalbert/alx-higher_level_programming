#!/usr/bin/python3
for i in range(97, 97+26):
    if chr(i) != 'q' and chr(i) != 'e':
        print( str.format(chr(i)), end="")
