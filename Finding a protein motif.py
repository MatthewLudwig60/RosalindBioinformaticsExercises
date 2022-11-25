#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:00:20 2021

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
    Parsed_lines = []
    for i in range(1, len(lines)):
        dummy = split(lines[i][0])
        place = []
        for i in range(len(dummy)):
            if dummy[i] != '\n':
                place.append(dummy[i])
        Parsed_lines.append(place)
    Parsed_line = ''
    for i in range(len(Parsed_lines)):
        for j in range(len(Parsed_lines[i])):
            Parsed_line += Parsed_lines[i][j]
    return(Parsed_line)

Permitted_AAs = ['F', 'L', 'S', 'Y', 'C', 'W', 'H', 'Q', 'R', 'I', 'M', 'N', 'K', 'V', 'A', 'D', 'E','G', 'T']
Permitted_motifs = []
Either_OR = ['S', 'T']
for i in range(len(Permitted_AAs)):
    for j in range(len(Permitted_AAs)):
        for k in range(len(Either_OR)):
            Permitted_motifs.append(f'N{Permitted_AAs[i]}{Either_OR[k]}{Permitted_AAs[j]}')

# N{P}[ST]{P}

def motif_finder(data):
    indexes = []
    Parsed_line = parse(data)
    for i in range(len(Permitted_motifs)):
        if Permitted_motifs[i] in Parsed_line:
            indexes.append(str(Parsed_line.index(Permitted_motifs[i])+1))
    sorted_status = False
    while sorted_status == False:
        counter = 0
        for i in range(len(indexes)-1):
            if float(indexes[i]) > float(indexes[i+1]):
                temp = indexes[i]
                indexes[i] = indexes[i+1]
                indexes[i+1] = temp
                counter += 1
        if counter == 0:
            sorted_status = True
    # print(indexes)
    # repeat_indexes = []
    # for i in range(len(indexes)-1):
    #     if indexes[i] == indexes[i+1]:
    #         repeat_indexes.append(i)
    # print(repeat_indexes)
    # final_indexes = []
    # for i in range(len(indexes)):
    #     if i not in repeat_indexes:
    #         final_indexes.append(indexes[i])
    string = ''
    for i in range(len(indexes)):
        string += f'{indexes[i]} '
    print(string)
        
        

motif_finder(data)
