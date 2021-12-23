#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    index = 0

    if (argc == 1):
        print('0 arguments.')
    elif (argc == 2):
        print('1 argument:')
    else:
        print('{} arguments:'.format(argc - 1))

    for item in argv[1:]:
        index = index + 1
        print('{}: {}'.format(index, item))
