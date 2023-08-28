#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        while printed_elements < x:
            print("{}".format(my_list[printed_elements]), end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print("")
        return printed_elements
