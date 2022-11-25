# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

data1 = input('What is your first DNA nucleotide base sequence?')
data2 = input('What is your second DNA nucleotide base sequence?')

def split(word):
    return[char for char in word]

letters1 = split(data1)
letters2 = split(data2)

purines = ['A', 'G']
pyrimidines = ['T', 'C']

def ratio(letters1, letters2):
    transitions = 0
    transversions = 0
    for i in range(len(letters1)):
        if letters1[i] != letters2[i]:
            if letters1[i] in purines and letters2[i] in purines:
                transitions += 1
            elif letters1[i] in pyrimidines and letters2[i] in pyrimidines:
                transitions += 1
            else:
                transversions += 1
    ratio = transitions / transversions
    print(ratio)

ratio(letters1, letters2)
                
            






