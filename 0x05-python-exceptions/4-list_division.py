#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = []
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            int_a = isinstance(a, int)
            int_b = isinstance(b, int)
            float_a = isinstance(a, float)
            float_b = isinstance(b, float)
            if int_a is False and float_a is False:
                print("wrong type")
                result.append(0)
            elif int_b is False and float_b is False:
                print("wrong type")
                result.append(0)
            elif b == 0:
                print("division by 0")
                result.append(0)
            else:
                q = a / b
                result.append(q)
    except IndexError:
        for n in range(i, list_length):
            print("out of range")
            result.append(0)
    finally:
        return (result)
