#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_results = []
    try:
        for index in range(list_length):
            try:
                list_results.append(my_list_1[index] / my_list_2[index])
            except ZeroDivisionError:
                list_results.append(0)
                print('division by 0')
            except TypeError:
                print('wrong type')
                list_results.append(0)
    except IndexError:
        print('out of range')
        list_results.append(0)
    finally:
        return list_results
