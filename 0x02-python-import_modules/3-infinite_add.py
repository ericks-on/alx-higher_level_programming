#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    total = 0
    for arg in av[1:]:
        total = total + int(arg)
    print("{}".format(total))
