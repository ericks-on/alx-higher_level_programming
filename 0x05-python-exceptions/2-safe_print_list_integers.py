#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        r = 0
        for i in range(x):
            member = my_list[i]
            val = isinstance(member, int)
            if val is True:
                r += 1
                print("{:d}".format(member), end="")
            else:
                continue
        print("\n", end="")
        return (r)
    except IndexError:
        raise IndexError
