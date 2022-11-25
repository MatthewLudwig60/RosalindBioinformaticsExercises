#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:00:02 2021

@author: Matthew
"""

data = input('What is your AA sequence?')

codons = ['UUU', 'UUC', 'UUA', 'UUG', 'UCU', 'UCC', 'UCA', 'UCG', 'UAU', 'UAC', 'UAA', 'UAG',
          'UGU', 'UGC', 'UGA', 'UGG', 'CUU', 'CUC', 'CUA', 'CUG', 'CCU', 'CCC', 'CCA', 'CCG',
          'CAU', 'CAC', 'CAA', 'CAG', 'CGU', 'CGC', 'CGA', 'CGG', 'AUU', 'AUC', 'AUA', 'AUG',
          'ACU', 'ACC', 'ACA', 'ACG', 'AAU', 'AAC', 'AAA', 'AAG', 'AGU', 'AGC', 'AGA', 'AGG',
          'GUU', 'GUC', 'GUA', 'GUG', 'GCU', 'GCC', 'GCA', 'GCG', 'GAU', 'GAC', 'GAA', 'GAG',
          'GGU', 'GGC', 'GGA', 'GGG']

AAs = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', 'Stop', 'Stop', 'C', 'C', 'Stop',
       'W', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R',
       'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R', 'V',
       'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']

def split(word):
    return[char for char in word]

def num_mRNA(data):
    letters = split(data)
    total = 1
    for i in range(len(letters)):
        counter = 0
        for j in range(len(AAs)):
            if letters[i] == AAs[j]:
                counter +=1
        total = total * counter
    total = total * 3 #for 3 different stop codons
    output = total % 1000000
    print(output)

num_mRNA(data)
