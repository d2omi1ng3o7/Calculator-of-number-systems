#!/usr/bin/env python3

""" 
    Ten moduł zmienia liczby z systemu dziesiętnego na liczby w systemie binarnym, ósemkowym i szestnaskowym.

    This module converts numbers from decimal to binary, octal, and hexadecimal. 
"""

numbers = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
}

def dec_to_hex_bin_oct(x, y, result=''): 
    try:
        x = int(x)
    except:
        return '0'
    if (x >= 0 and x <= 15) and x < y:
        result += numbers[x]
        return result[::-1]
    else:
        result += numbers[x % y]
        x = x // y
        return dec_to_hex_bin_oct(x, y, result)

if __name__ == '__main__':
    print(dec_to_hex_bin_oct(46, 16))