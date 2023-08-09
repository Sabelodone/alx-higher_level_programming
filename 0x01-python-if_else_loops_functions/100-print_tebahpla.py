#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - 32)), end="")
    if c % 2 == 0:
        c -= 1
    else:
        c += 1
