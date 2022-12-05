#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        my_bool = []
        for i, num in enumerate(my_list):
            if num % 2 == 0:
                my_bool.append(True)
            else:
                my_bool.append(False)
        return my_bool
