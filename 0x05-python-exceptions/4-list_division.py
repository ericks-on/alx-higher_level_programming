#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = []
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            type_a = isinstance(a, int)
            type_b = isinstance(b, int)
            if False in [type_a, type_b]:
                #check for float
                float_a = isinstance(a, float)
                float_b = isinstance(b, float)
                if type_a is False and type_b is False:
                    if float_a is True and float_b is True:
                        ans = a / b
                        result.append(ans)
                    else:
                        print("Wrong type")
                        result.append(0)
                elif type_a is False and type_b is True:
                    if float_a is True:
                        ans = a / b
                        result.append(ans)
                    else:
                        print("Wrong type")
                        result.append(0)
                elif type_b is False and type_a is True:
                    if float_a is True:
                        ans = a / b
                        result.append(ans)
                    else:
                        print("Wrong type")
                        result.append(0)
            elif b == 0:
                print("division by 0")
                result.append(0)
            else:
                ans = a / b
                result.append(ans)
    except IndexError:
        for n in range(i, list_length):
            print("out of range")
            result.append(0)
    finally:
        return (result)
