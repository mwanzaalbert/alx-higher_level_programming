#!/usr/bin/python3
import random
last_digit = abs(number) % 10

if number > 0:
#     print(number, "number is positive")
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    else:
        if last_digit == 0:
            print(f"Last digit of {number} is {last_digit} and is 0")
        else:
            if last_digit < 6 and not 0:
                print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
            else:
                print()
else:
    last_digit = -last_digit
#     print(number, "number is negative")
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
