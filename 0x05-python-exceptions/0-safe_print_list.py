#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("\n", end="")
        n = x
    except IndexError:
        print("\n", end="")
        n = i
    finally:
        return (n)
