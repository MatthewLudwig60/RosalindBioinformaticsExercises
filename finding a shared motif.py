#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:50:48 2021

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
    for i in range(1, len(lines)+1, 2):
        dummy = split(lines[i][0])
        place = []
        for i in range(len(dummy)):
            if dummy[i] != '\n':
                place.append(dummy[i])
        Parsed_lines.append(place)
    return(Parsed_lines)

def shared_motif(data):
    Parsed_lines = parse(data)
    min_length = len(Parsed_lines[0])
    position = 0
    for i in range(len(Parsed_lines)):
        if len(Parsed_lines[i]) < min_length:
            min_length = len(Parsed_lines[i])
            position = i
    min_string = Parsed_lines[position]
    possible_motifs = []
    possible_motifs.append(min_string)
    for i in range(min_length-1, 1, -1): #iterate through possible motif lengths 
        for j in range(0, min_length-i+1): #iterate through motif start position in shortest string
            possible_motifs.append(min_string[j:(j+i)])
    # print(possible_motifs[0][4])
    shared_motifs = []
    for i in range(len(possible_motifs)): #iterate through possible motifs
        counter = 0
        for j in range(len(Parsed_lines)): #iterate through strings
            status = False
            string = Parsed_lines[j]
            # for k in range(0, (len(Parsed_lines[j]) - len(possible_motifs[i]) + 1)): #iterate through start positions of motif in string
            #     dummy = string[k: (k+len(possible_motifs[i]))] #substrings in strings equal in length to a trial motif 
            #     print(dummy)
    #             motif_counter = 0 #number of letters common between a trial motif and a certain dummy
    #             for p in range(len(possible_motifs[i])):
    #                 if possible_motifs[i][p] == dummy[p]:
    #                     counter += 1
    #             if motif_counter == len(possible_motifs[i]): #if joined characters = motif
    #                 status = True  
    #         if status == True:
    #             counter += 1
    #     if counter == len(Parsed_lines):
    #         shared_motifs.append(possible_motifs[i])
    # print(shared_motifs)
                       
shared_motif(data)

