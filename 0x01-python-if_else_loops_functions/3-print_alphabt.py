#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if letter is not ord('q') and letter is not ord('e'):
        print(chr(letter), end='')