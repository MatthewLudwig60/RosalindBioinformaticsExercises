#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:09:12 2021

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
bases = ['A', 'T', 'G', 'C']
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
    for i in range(len(lines)):
        dummy = split(lines[i][0])
        place = []
        for i in range(len(dummy)):
            if dummy[i] != '\n':
                place.append(dummy[i])
        place = join(place)
        Parsed_lines.append(place)
    return(Parsed_lines)
    
def GC_content(data):
    Parsed_lines = parse(data)
    GC_content = 0
    highest_GC = 0
    for i in range(1, (len(Parsed_lines)+1), 2):
        line = Parsed_lines[i][0]
        letters = split(line)
        total = len(letters)
        counter = 0
        for j in range(len(letters)):
            if letters[j] == 'G' or letters[j] == 'C':
                counter += 1
        content = (counter / total) * 100
        if content > GC_content:
            GC_content = content
            highest_GC = Parsed_lines[i-1][0]
    print(highest_GC)
    print(GC_content)

GC_content(data)
        
        
    
    
    
        
        