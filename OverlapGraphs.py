#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:55:13 2021

@author: Matthew
"""

data = input('What is your input data?')

def split(word):
    return[char for char in word]

def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word

bases = ['A', 'C', 'G', 'T']

def parse(data):
    letters = split(data)
    breakers = []
    for i in range(len(letters)-1):
        if letters[i] == '\n' and letters[i-1] not in bases or letters[i] == '\n' and letters[i+1] not in bases: 
            breakers.append(i)
    lines = []
    for i in range(len(breakers)+1):
        if i == 0:
            line = join(letters[0:breakers[0]])
        elif i == len(breakers):
            line = join(letters[(breakers[i-1]+1):(-1)])
            line.append(letters[-1])
            line = join(line)
        else:
            line = join(letters[(breakers[i-1]+1):breakers[i]])
        lines.append(line)
    tags = []
    sequences = []
    for i in range(1, len(lines)+1, 2):
        sequences.append(lines[i])
    # tags.append(lines[0])
    for i in range(0, len(lines), 2):
        chars = split(lines[i][0])
        chars = chars[1: len(chars)]
        dummy = join(chars)
        tags.append(dummy)
    return(tags, sequences)


def prefix_suffix_gen(string, length):
    chars = list(string)
    prefix_suffix = []
    prefix = ''
    suffix = ''
    for i in range(length):
        prefix += chars[i]
    for i in range((len(chars)-length), len(chars)):
        suffix += chars[i]
    
    prefix_suffix.append(prefix)
    prefix_suffix.append(suffix)
    return(prefix_suffix)


tags, sequences = parse(data)
substrings = []

for i in range(len(sequences)):
    substrings.append(prefix_suffix_gen(sequences[i][0], 3))

pairs = []
for i in range(len(substrings)): #iterate through strings
    for j in range(len(substrings)): #iterate through all other strings
        if substrings[i][1] == substrings[j][0]:
            pairs.append([i, j])

final_pairs = []
for i in range(len(pairs)):
    if pairs[i] not in final_pairs:
        if pairs[i][0] != pairs[i][1]:
            final_pairs.append(pairs[i])

for i in range(len(final_pairs)):
    print(f'{tags[final_pairs[i][0]][0]} {tags[final_pairs[i][1]][0]}')
    
                
        


