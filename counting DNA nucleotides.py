#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:10:30 2021

@author: Matthew
"""

def split(word):
    return[char for char in word]
data = input('What is your DNA nucleotide sequence?')
def base_counter(data):
    letters = split(data)
    num_a = 0
    num_t = 0
    num_g = 0
    num_c = 0
    for i in range(len(letters)):
        if letters[i] == 'A':
            num_a += 1
        elif letters[i] == 'T':
            num_t += 1
        elif letters[i] == 'G':
            num_g += 1
        elif letters[i] == 'C':
            num_c += 1
    print(num_a, num_c, num_g, num_t)
base_counter(data)