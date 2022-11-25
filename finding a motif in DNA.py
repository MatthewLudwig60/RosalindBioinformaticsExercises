#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:44:24 2021

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
    breaker = 0
    for i in range(len(letters)-1):
        if letters[i] == '\n':
            breaker = i
    lines = []
    lines.append(letters[0:breaker])
    dummy = letters[(breaker+1):-1] + [letters[-1]]
    lines.append(dummy)
    return(lines)

def substring(data):
    lines = parse(data)
    string = lines[0]
    sub = lines[1]
    locations = []
    for i in range(0, (len(string)-len(sub))):
        if string[i] == sub[0]:
            status = True
            for j in range(0, len(sub)):
                if string[i+j] != sub[j]:
                    status = False
            if status == True: #if the substring is found from i in the string
                locations.append(i+1)
    output = ''
    for i in range(len(locations)):
        output += f'{locations[i]} '
    print(output)
substring(data)
                