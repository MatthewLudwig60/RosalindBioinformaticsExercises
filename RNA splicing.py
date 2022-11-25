#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:14:51 2021

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

data = input('What is your input data?')

def split(word):
    return[char for char in word]

def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word

def bubble_sort(list1, list2):
    swapped = True
    while(swapped == True):
        swapped = False
        for i in range(0, (len(list1) - 1)):
            if list1[i] > list1[i + 1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
                temp2 = list2[i]
                list2[i] = list2[i+1]
                list2[i+1] = temp2
                swapped = True                
    return([list1, list2])

bases = ['A', 'C', 'G', 'T']

def splice(data):
    letters = split(data)
    breakers = []
    for i in range(len(letters)-1):
        if letters[i] == '\n' and letters[i-1] not in bases or letters[i] == '\n' and letters[i+1] not in bases: 
            breakers.append(i)
    DNA_sequence = letters[breakers[0]+1:breakers[1]]
    print(len(DNA_sequence))
    introns = []
    for i in range(3, len(breakers)+1, 2):
        if i == len(breakers):
            line = letters[(breakers[i-1]+1):(-1)]
            line.append(letters[-1])
        else:
            line = letters[(breakers[i-1]+1):breakers[i]]
        introns.append(line)
    locations = []
    for i in range(len(introns)): #iterate through introns 
        for j in range(0, (len(DNA_sequence)-len(introns[i]))): #iterate through location intron could be in DNA sequence
            if DNA_sequence[j] == introns[i][0]: 
                status = True
                for k in range(0, len(introns[i])): #iterate through length of intron
                    if DNA_sequence[j+k] != introns[i][k]:
                        status = False
                if status == True: #if the substring is found from i in the string
                    locations.append(j)
    locations, introns = bubble_sort(locations, introns)
    spliced_DNA = []
    for i in range(len(locations)):
        if i == 0:
            spliced_DNA.append(DNA_sequence[0:locations[0]])
        elif i == len(locations)-1:
            spliced_DNA.append(DNA_sequence[(locations[i-1]+ len(introns[i-1])):locations[i]])
            spliced_DNA.append(DNA_sequence[(locations[i]+len(introns[i])):-1])
            spliced_DNA.append(DNA_sequence[-1])
        else:
            spliced_DNA.append(DNA_sequence[(locations[i-1] + len(introns[i-1])):locations[i]])
    spliced_string = []
    for i in range(len(spliced_DNA)):
        for j in range(len(spliced_DNA[i])):
            spliced_string.append(spliced_DNA[i][j])
    return(spliced_string)

def transcribe(data):
    letters = split(data)
    for i in range(len(letters)):
        if letters[i] == 'T':
            letters[i] = 'U'
    word = join(letters)
    return(word)

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
    return(Final_sequence[0])



def RNA_splicing(data):
    string = splice(data)
    mRNA = transcribe(string)
    AA_sequence = translate(mRNA[0])
    print(AA_sequence)


RNA_splicing(data)
