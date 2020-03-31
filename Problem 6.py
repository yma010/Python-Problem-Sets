# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:27:07 2019

@author: Marvin

Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.

"""
def sumDigits(N):
    if N == 0:
        return 0
    else:
        return N % 10 + sumDigits(N // 10)