#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:07:49 2021

@author: Matthew
"""
def factorial(n):
    multiplier = 1
    for i in range(1, n+1):
        multiplier = multiplier * i
    return(multiplier)

def permutations(n):
    permutations = []
    digits = [1, 2, 3, 4]
    for i in range(n):
        permutations.append([])
    for i in range(n):
        for j in range(int(factorial(n-1))):
            permutations[i].append([i+1])
        dummy = digits
        dummy.pop(1)
        permutations[i].append(dummy)
    print(permutations)
    
permutations(3)