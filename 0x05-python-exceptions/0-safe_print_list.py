#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""

    length = 0
    for i in my_list:
        try:
            length += 1
            print("{}".format(i), end="")
        except IndexError:
            break
    print("")
    return length
