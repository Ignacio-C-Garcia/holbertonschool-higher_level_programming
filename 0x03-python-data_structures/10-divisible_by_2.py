#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    if my_list:
        for number in my_list:
            if number % 2 == 0:
                result_list = result_list + [True]
            else:
                result_list = result_list + [False]
        return result_list
