#!/usr/bin/env python3

""" 
    Ten moduł zmienia liczby z systemu binarnego na liczby w systemie dziesiętnym.

    This module converts numbers from binary to decimal. 
"""

def bin_to_dec(x):  
    result = 0
    y = len(x)-1   
    l = 0
    for i in x:
        if i == '1':
            result += 2**(y-l)
        l += 1
    return result    

if __name__ == '__main__':
    print(bin_to_dec('1011101101'))