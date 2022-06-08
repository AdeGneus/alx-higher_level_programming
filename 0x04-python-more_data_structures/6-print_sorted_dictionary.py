#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    # [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
