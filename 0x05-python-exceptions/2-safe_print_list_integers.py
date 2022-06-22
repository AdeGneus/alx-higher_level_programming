#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers"""

    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            length += 1
        except (ValueError, TypeError):
            continue
    print("")
    return length