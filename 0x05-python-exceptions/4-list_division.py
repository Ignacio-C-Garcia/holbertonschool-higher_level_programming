#!/usr/bin/python3
from unittest import result


def list_division(my_list_1, my_list_2, list_length):
    list_results = []
    result = 0
    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except TypeError:
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except IndexError:
            result = 0
            print('out of range')
        finally:
            list_results.append(result)
    return list_results
