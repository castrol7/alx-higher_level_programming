#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    length = len(roman_string)

    for i, char in enumerate(roman_string):
        value = roman_numerals.get(char, 0)

        if i == length - 1 or roman_numerals.get(roman_string[i + 1], 0) <= value:
            result += value
        else:
            result -= value

    return result
