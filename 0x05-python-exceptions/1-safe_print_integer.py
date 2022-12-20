#!/usr/bin/python3
def safe_print_integer(value):
    try:
        r = isinstance(value, int)
        if r is True:
            print("{:d}".format(value))
    except ValueError:
        r = isinstance(value, int)
    finally:
        return (r)
