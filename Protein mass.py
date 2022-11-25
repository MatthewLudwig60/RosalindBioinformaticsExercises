#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:31:21 2021

@author: Matthew
"""
Weighted_masses = [['A',   71.03711], 
                   ['C',   103.00919],
                   ['D',   115.02694],
                   ['E',   129.04259],
                   ['F',   147.06841],
                   ['G',   57.02146],
                   ['H',   137.05891],
                   ['I',   113.08406],
                   ['K',   128.09496],
                   ['L',   113.08406],
                   ['M',   131.04049],
                   ['N',   114.04293],
                   ['P',   97.05276],
                   ['Q',   128.05858],
                   ['R',   156.10111],
                   ['S',   87.03203],
                   ['T',   101.04768],
                   ['V',   99.06841],
                   ['W',   186.07931],
                   ['Y',   163.06333]]

def split(word):
    return[char for char in word]

data = input('What is your AA sequence?')
letters = split(data)
def protein_mass(letters):
    total = 0
    for i in range(len(letters)):
        for j in range(len(Weighted_masses)):
            if letters[i] == Weighted_masses[j][0]:
                total += Weighted_masses[j][1]
    print(round(total, 3))
protein_mass(data)
    
    
        