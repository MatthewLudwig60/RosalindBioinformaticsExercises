#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:41:37 2021

@author: Matthew
"""
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

data = input('What is your mRNA nucleotide base sequence?')

def split(word):
    return[char for char in word]

def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word

def triplets(letters):
    triplets = []
    for i in range(0, len(letters), 3):
        dummy = []
        dummy.append(letters[i])
        dummy.append(letters[i+1])
        dummy.append(letters[i+2])
        word = join(dummy)
        triplets.append(word)
    return triplets

def amino_acid(triplets):
    AA_sequence = []
    for i in range(len(triplets)):
        for j in range(len(codons)):
            if triplets[i][0] == codons[j]:
                AA_sequence.append(AAs[j])
    return(AA_sequence)
    
def translate(data):
    letters = split(data)
    Triplets = triplets(letters)
    AA_sequence = amino_acid(Triplets)
    Final_sequence = []
    for i in range(len(AA_sequence)):
        if AA_sequence[i] == 'Stop':
            Final_sequence = AA_sequence[0:(i)]
            break
        else:
            Final_sequence.append(AA_sequence[i])
    Final_sequence = join(Final_sequence)
    print(Final_sequence[0])

translate(data)    
    
        
    
