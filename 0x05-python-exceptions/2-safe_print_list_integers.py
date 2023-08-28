#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        printed_integers = 0
        i = 0
        while i < x:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
        print()
        return printed_integers
    except IndexError:
        print()
        return printed_integers
