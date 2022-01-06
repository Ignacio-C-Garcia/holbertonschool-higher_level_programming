#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string:
        result = 0
        numbers =\
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last_digit = numbers[roman_string[0]]
        for index in roman_string:
            if numbers[index] <= last_digit:
                result += numbers[index]
            else:
                result -= numbers[index]
            last_digit = numbers[index]
        return abs(result)
    return 0
