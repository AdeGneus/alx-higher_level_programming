#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary == {} or a_dictionary is None:
        return None
    return sorted(a_dictionary)[-1]
