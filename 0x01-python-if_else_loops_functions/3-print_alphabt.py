#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if chr(letter) not in ["q", "e"]:
        print("{}".format(chr(letter)), end='')
