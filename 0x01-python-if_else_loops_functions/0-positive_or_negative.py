#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
else:
    if number == 0:
        print(f"{number} is zero")
    else:
        if number < 0:
            print(f"{number} is negative")
        else:
            print()