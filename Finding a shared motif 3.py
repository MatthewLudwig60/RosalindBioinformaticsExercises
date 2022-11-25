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
    # min_string = Parsed_lines[position]
    data_strings = []
    for i in range(len(Parsed_lines)):
        string = ''
        for j in range(len(Parsed_lines[i])):
            string += Parsed_lines[i][j]
        data_strings.append(string)
    possible_motifs = []
    for j in range(len(Parsed_lines[position]), 1, -1): #iterate through possible motif lengths 
        for k in range(0, (len(Parsed_lines[position])-j+1)): #iterate through motif start position in shortest string
            candidate = Parsed_lines[i][k:(k+j)]
            possible_motifs.append(candidate)
            string = ''
            for a in range(len(candidate)):
                string += candidate[a]
            status = True
            for i in range(len(data_strings)):
                if string not in data_strings[i]:
                    status = False
            if status == True:
                print(string)
                break

shared_motif(data)
