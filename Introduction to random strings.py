#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:16:57 2021

@author: Matthew
"""
import numpy as np 

def split(word):
    return[char for char in word]

data = input('What is your DNA nucleotide base sequence?')
letters = split(data)
bases = ['A', 'T', 'G', 'C']
base_counter = [0, 0, 0, 0]
for i in range(len(letters)):
    for j in range(len(bases)):
        if letters[i] == bases[j]:
            base_counter[j] += 1

GC_data = input('What is your GC content data?')
GC_values = GC_data.split(' ')
for i in range(len(GC_values)):
    GC_values[i] = float(GC_values[i])
output_values = ''
for i in range(len(GC_values)):
    G_prob = (GC_values[i]) / 2
    A_prob = (1 - GC_values[i]) / 2
    probabilities = [A_prob, A_prob, G_prob, G_prob]
    multiplier = 1
    for j in range(len(base_counter)):
        multiplier = multiplier * (probabilities[j]**base_counter[j])
    output = round(np.log10(multiplier), 3)
    output_values += f'{output} '

print(output_values)
    
            