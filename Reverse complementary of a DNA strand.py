#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:30:40 2021

@author: Matthew
"""

import numpy as np
def split(word):
    return[char for char in word]
def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word
data = input('What is your DNA nucleotide sequence?')

def reverse(data):
    letters = split(data)
    num_bases = len(letters)
    reversed_letters = []
    for i in range(num_bases):
        position = num_bases - 1 - i
        reversed_letters.append(letters[position])
    return(reversed_letters)
    
def complementary(letters):
    num_bases = len(letters)
    complementary_letters = []
    for i in range(num_bases):
        if letters[i] == 'A':
            complementary_letters.append('T')
        elif letters[i] == 'T':
            complementary_letters.append('A')
        elif letters[i] == 'G':
            complementary_letters.append('C')
        elif letters[i] == 'C':
            complementary_letters.append('G')
    return complementary_letters

def reverse_complementary(data):
    reversed_letters = reverse(data)
    reversed_complementary_letters = complementary(reversed_letters)
    print(join(reversed_complementary_letters))


print(reverse_complementary(data))
    
    
    