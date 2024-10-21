#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = sum(int(argument) for argument in sys.argv[1:])
    print("{}".format(total))
