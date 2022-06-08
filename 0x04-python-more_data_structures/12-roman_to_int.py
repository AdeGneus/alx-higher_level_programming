#!/usr/bin/python3
def roman_to_int(roman_string):
    len_roman_num = len(roman_string)
    sum_num = 0
    rom_num = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
    }
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0
    else:
        for x in range(len_roman_num):
            if rom_num.get(roman_string[x], 00) == 0:
                return 0
            if x is (len_roman_num - 1):
                sum_num += rom_num[roman_string[x]]
            else:
                if rom_num[roman_string[x]] >= rom_num[roman_string[x + 1]]:
                    sum_num += rom_num[roman_string[x]]
                else:
                    sum_num -= rom_num[roman_string[x]]
    return sum_num
