#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(0, len(argv) - 1):
            print(f"{i + 1}: {argv[i + 1]}")
