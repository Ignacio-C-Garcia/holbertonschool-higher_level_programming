#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    sum_result = 0

    for number in argv[1:]:
        sum_result += int(number)

    print('{}'.format(sum_result))
