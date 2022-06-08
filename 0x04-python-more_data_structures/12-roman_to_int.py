#!/usr/bin/python3
def roman_to_int(roman_string):
    len_roman_num = len(roman_string)
    sum_num = 0
    roman_num_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
    }
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0
    else:
        for x in range(len_roman_num):
            if x is (len_roman_num - 1):
                sum_num += roman_num_dict[roman_string[x]]
            else:
                if roman_num_dict[roman_string[x]] >= roman_num_dict[roman_string[x + 1]]:
                    sum_num += roman_num_dict[roman_string[x]]
                else:
                    sum_num -= roman_num_dict[roman_string[x]]
    return sum_num
