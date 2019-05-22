#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:16:53 2018

@author: carlosponce
"""


def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    for i in L:
        if i % 2 == 0:
            return i
    raise ValueError('findAnEven called with no even numbers')
            
l = [1,1,1,1,1]

x = findAnEven(l)
print(x)