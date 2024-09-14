for i, letter in enumerate(list(chr(index) for index in range(ord("A"), ord('Z') + 1))[::-1]):
    if i % 2 == 0:
        print("{:s}".format(letter.lower()), end='')
    else:
        print("{:s}".format(letter), end='')
