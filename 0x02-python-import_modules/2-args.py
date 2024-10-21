#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    match(count):
        case 0:
           print(f"{count} arguments.")
        case 1:
            print(f"{count} argument:")
        case _:
            print(f"{count} arguments:")

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
