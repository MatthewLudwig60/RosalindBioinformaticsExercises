#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:55:27 2021

@author: Matthew
"""
def Fibonacci_rabbits(n, k, m):
    terms = [1, 1]
    for i in range(n-2):
        births = terms[-2]
        if i >= n -m-2:
            deaths = terms[-m]
        else:
            deaths = 0
        new_term = terms[-1] + (k * births) - deaths
        terms.append(new_term)
    print(terms)
Fibonacci_rabbits(94, 1, 17)