#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:26:20 2021

@author: Matthew
"""

data1 = input('What is your first DNA nucleotide base sequence?')
data2 = input('What is your second DNA nucleotide base sequence?')

def split(word):
    return[char for char in word]

letters1 = split(data1)
letters2 = split(data2)

def Hamming_distance(letters1, letters2):
    counter = 0
    for i in range(len(letters1)):
        if letters1[i] != letters2[i]:
            counter += 1
    print(counter)

Hamming_distance(letters1, letters2)
        