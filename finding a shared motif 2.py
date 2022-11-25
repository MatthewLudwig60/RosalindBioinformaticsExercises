#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:00:27 2021

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
    for i in range(len(Parsed_lines)): #iterate through strings
        string_motifs = [Parsed_lines[i]] 
        for j in range(len(Parsed_lines[i])-1, 1, -1): #iterate through possible motif lengths 
            for k in range(0, (len(Parsed_lines[i])-j+1)): #iterate through motif start position in shortest string
                string_motifs.append(Parsed_lines[i][k:(k+j)])
        possible_motifs.append(string_motifs)
    shared_motifs = []
    for i in range(len(possible_motifs[position])): #iterate through possible motifs for shortest string
        overall_status = True
        for j in range(len(Parsed_lines)): #iterate through all strings
            if possible_motifs[position][i] not in possible_motifs[j]:
                overall_status = False
        if overall_status == True:
            shared_motifs.append(possible_motifs[position][i])
        if overall_status == False and len(shared_motifs) > 0:
            break
    print(shared_motifs)
            
                
            
            
        
    

shared_motif(data)
