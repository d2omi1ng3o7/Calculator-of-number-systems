#!/usr/bin/env python3

""" 
    Ten moduł zmienia liczby z systemu szesnastkowego na liczby w systemie binarnym.

    This module converts numbers from hexadecimal to binary numbers.
"""
from . import dec_to_hex_bin_oct

numbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}

def hex_to_bin(x):
    result = ''
    if x == '':
        return '0'
    for i in x:
        number = numbers[i]
        y = dec_to_hex_bin_oct.dec_to_hex_bin_oct(number, 2)
        for i in range(4):
            if len(y) < 4:
                y = '0' + y
            else:
                break
        result += y
    return result

 
if __name__ == '__main__':
    print(hex_to_bin('B4F'))