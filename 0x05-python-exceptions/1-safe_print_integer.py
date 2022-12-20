#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        r = True
    except ValueError:
        r = False
    finally:
        return (r)
