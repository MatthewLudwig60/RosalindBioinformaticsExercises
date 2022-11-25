#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:26:20 2021

@author: Matthew
"""
data = input('What are your genotype values?')

def split(word):
    return[char for char in word]

def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word

def data_prep(data):
    values = split(data)
    breakers = []
    for i in range(len(values)):
        if values[i] == ' ':
            breakers.append(i)
    k = int(join(values[0:breakers[0]])[0])
    m = int(join(values[(breakers[0]+1):breakers[1]])[0])
    dummy = values[(breakers[1]+1):-1] + [values[-1]]
    n = int(join(dummy)[0])
    return([k, m, n])

def probability(data):
    input_list = data_prep(data)
    k = input_list[0]
    m = input_list[1]
    n = input_list[2]
    
    numerator = k*(k-1) + 2*k*m + m*n + 0.75*m*(m-1) + 2*k*n
    denominator = (k+m+n) * (k+m+n-1)
    
    print(round((numerator / denominator), 5))
    
probability(data)



    