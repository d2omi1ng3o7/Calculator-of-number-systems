#!/usr/bin/env python3

""" 
    Ten moduł zmienia liczby z systemu ósemkowego na liczby w systemie binarnym.

    This module converts numbers from octal to binary. 
"""

from . import dec_to_hex_bin_oct

numbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
}

def oct_to_bin(x):
    result = '' 
    if x == '':
        return '0'
    for i in x:
        number = numbers[i]
        y = dec_to_hex_bin_oct.dec_to_hex_bin_oct(number, 2)
        for i in range(3):
            if len(y) < 3:
                y = '0' + y
            else:
                break
        result += y
    return result

 
if __name__ == '__main__':
    print(oct_to_bin('247'))