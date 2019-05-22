#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:55:37 2018

@author: carlosponce
"""
def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    numbers = '123456789'
    sumdigits = 0
    try:
        for i in s:
            if i in numbers:
                sumdigits += int(i)
        return sumdigits
    except TypeError:
        print('Input was not a string')
        

s = '123'
x = sumDigits(s)
print(x)

