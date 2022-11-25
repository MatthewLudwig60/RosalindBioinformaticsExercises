#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:11:03 2021

@author: Matthew
"""

import numpy as np 

data1 = input('What is your first DNA nucleotide base sequence?')
data2 = input('What is your second DNA nucleotide base sequence?')

def split(word):
    return[char for char in word]

letters1 = split(data1)
letters2 = split(data2)

def motif_finder(letters1, letters2):
    indices = np.zeros(len(letters2))
    for j in range(len(letters1)):
        if letters1[j] == letters2[0]:
            indices[0] = j+1
            break
    for i in range(1, len(letters2)):
        temp = []
        for j in range(len(letters1)):
            if letters1[j] == letters2[i] and j > indices[i-1]:
                temp.append((j+1))
        indices[i] = temp[0]
    output = ''
    for i in range(len(indices)):
        output += f'{str(int(indices[i]))} '
    print(output)
    
motif_finder(letters1, letters2)

            


