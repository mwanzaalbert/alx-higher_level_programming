#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1

    if count:
        match(count):
            case 1:
                print(f"{count} argument:")
            case _:
                print(f"{count} arguments:")

                for index, argument in enumerate(sys.argv[1:]):
                    print(f"{index + 1}: {argument}")
    else:
        print(f"{count} arguments.")
